import connexion
from flask import current_app
from werkzeug.exceptions import BadRequest
from datetime import datetime
from dateutil.tz import tzlocal
from dsub.providers import google
from dsub.providers import local
from dsub.providers import stub
from jobs.models.failure_message import FailureMessage
from jobs.models.job_metadata_response import JobMetadataResponse
from jobs.models.query_jobs_request import QueryJobsRequest
from jobs.models.query_jobs_response import QueryJobsResponse
from jobs.models.query_jobs_result import QueryJobsResult
from dsub_client import ProviderType
import job_statuses
import job_ids

_DEFAULT_PAGE_SIZE = 64
_MAX_PAGE_SIZE = 64


def provider_type():
    return current_app.config['PROVIDER_TYPE']


def client():
    return current_app.config['CLIENT']


def abort_job(id):
    """Abort a job by API Job ID.

    Args:
        id (str): Job ID to be aborted

    Returns: None
    """
    project_id, job_id, task_id = job_ids.api_to_dsub(id, provider_type())
    provider = _get_provider(project_id)
    client().abort_job(provider, job_id, task_id)


def get_job(id):
    """Get a job's metadata by API Job ID.

    Args:
        id (str): Job ID to get

    Returns:
        JobMetadataResponse: Response containing relevant metadata
    """
    project_id, job_id, task_id = job_ids.api_to_dsub(id, provider_type())
    provider = _get_provider(project_id)
    job = client().get_job(provider, job_id, task_id)
    submission, start, end = _parse_job_datetimes(job)

    return JobMetadataResponse(
        id=id,
        name=job['job-name'],
        status=job_statuses.dsub_to_api(job['status']),
        submission=submission,
        start=start,
        end=end,
        inputs=job['inputs'],
        outputs=_job_to_api_outputs(job),
        labels=_job_to_api_labels(job),
        failures=_get_failures(job))


def query_jobs(body):
    """
    Query jobs by various filter criteria.

    Args:
        body (dict): The JSON request body.

    Returns:
        QueryJobsResponse: Response containing results from query
    """
    query = QueryJobsRequest.from_dict(body)
    if not query.page_size:
        query.page_size = _DEFAULT_PAGE_SIZE
    query.page_size = min(query.page_size, _MAX_PAGE_SIZE)

    jobs, next_page_token = client().query_jobs(
        _get_provider(query.parent_id), query)
    results = [_query_result(j, query.parent_id) for j in jobs]
    return QueryJobsResponse(results=results, next_page_token=next_page_token)


def _query_result(job, project_id=None):
    submission, start, end = _parse_job_datetimes(job)
    return QueryJobsResult(
        id=job_ids.dsub_to_api(project_id, job['job-id'], job.get('task-id')),
        name=job['job-name'],
        status=job_statuses.dsub_to_api(job['status']),
        submission=submission,
        start=start,
        end=end,
        labels=_job_to_api_labels(job))


def _get_failures(job):
    if (job['status'] == job_statuses.DsubStatus.FAILURE
            and job['status-message'] and job['last-update']):
        return [
            FailureMessage(
                failure=job['status-message'], timestamp=job['last-update'])
        ]
    else:
        return None


def _parse_job_datetimes(job):
    # TODO(https://github.com/googlegenomics/dsub/issues/74): Use 'start-time'
    # for start via dsub instead of create-time
    submission = _parse_datetime(job['create-time'])
    start = _parse_datetime(job['create-time'])
    end = _parse_datetime(job['end-time'])
    return submission, start, end


def _parse_datetime(date):
    # TODO(https://github.com/googlegenomics/dsub/issues/77): remove conditional
    # parsing by provider and date type (dsub should always return a datetime
    # object in the python API). This format is specific to dsub
    # https://github.com/googlegenomics/dsub/blob/master/dsub/providers/google.py#L1324
    # TODO(https://github.com/googlegenomics/dsub/issues/77): remove NA check
    if not date or date == 'NA':
        return None
    if (isinstance(date, datetime)):
        return date
    elif provider_type() == ProviderType.GOOGLE:
        return datetime.strptime(date, '%Y-%m-%d %H:%M:%S').replace(
            tzinfo=tzlocal())
    return datetime.strptime(date, '%Y-%m-%d %H:%M:%S.%f').replace(
        tzinfo=tzlocal())


def _job_to_api_labels(job):
    # Put any dsub specific information into the labels. These fields are
    # candidates for the common jobs API
    labels = job['labels'].copy() if job['labels'] else {}
    if 'status-detail' in job:
        labels['status-detail'] = job['status-detail']
    if 'last-update' in job:
        labels['last-update'] = job['last-update']
    if 'user-id' in job:
        labels['user-id'] = job['user-id']
    return labels


def _job_to_api_outputs(job):
    outputs = job['outputs'].copy() if job['outputs'] else {}
    # https://cloud.google.com/genomics/v1alpha2/pipelines-api-troubleshooting#pipeline_operation_log_files
    # TODO(https://github.com/googlegenomics/dsub/issues/75): drop this
    # workaround once the pipelines API and dsub support returning all log files
    if job['logging'] and job['logging'].endswith('.log'):
        base_log_path = job['logging'][:-4]
        outputs['log-controller'] = '{}.log'.format(base_log_path)
        outputs['log-stderr'] = '{}-stderr.log'.format(base_log_path)
        outputs['log-stdout'] = '{}-stdout.log'.format(base_log_path)
    return outputs


def _get_provider(parent_id=None):
    if provider_type() == ProviderType.GOOGLE:
        if not parent_id:
            raise BadRequest('missing required field parentId')
        return google.GoogleJobProvider(False, False, parent_id)
    elif provider_type() == ProviderType.LOCAL and not parent_id:
        return local.LocalJobProvider()
    elif provider_type() == ProviderType.STUB and not parent_id:
        return stub.StubJobProvider()
    else:
        raise BadRequest(
            'parentId can only be specified for the google dsub provider')
