import requests
from requests.auth import HTTPBasicAuth
from flask import current_app
from werkzeug.exceptions import NotFound
from datetime import datetime

from jobs.models.query_jobs_result import QueryJobsResult
from jobs.models.query_jobs_request import QueryJobsRequest
from jobs.models.query_jobs_response import QueryJobsResponse
from jobs.models.job_metadata_response import JobMetadataResponse
from jobs.models.task_metadata import TaskMetadata
from jobs.models.failure_message import FailureMessage


def abort_job(id):
    """
    Abort a job by ID

    :param id: Job ID
    :type id: str

    :rtype: None
    """
    url = '{cromwell_url}/{id}/abort'.format(
        cromwell_url=_get_base_url(), id=id)
    response = requests.post(url, auth=_get_user_auth())
    if response.status_code == NotFound.code:
        raise NotFound(response.json()['message'])


def update_job_labels(id, body):
    """
    Update labels on a job.

    :param id: Job ID
    :type id: str
    :param body:
    :type body: dict | bytes

    :rtype: UpdateJobLabelsResponse
    """
    return 'update job labels'


def get_job(id):
    """
    Query for job and task-level metadata for a specified job

    :param id: Job ID
    :type id: str

    :rtype: JobMetadataResponse
    """
    url = '{cromwell_url}/{id}/metadata'.format(
        cromwell_url=_get_base_url(), id=id)
    response = requests.get(url, auth=_get_user_auth())
    job = response.json()
    submission = _parse_datetime(job.get('submission'))
    start = _parse_datetime(job.get('start'))
    end = _parse_datetime(job.get('end'))
    failures = None
    if job.get('failures'):
        failures = [FailureMessage(failure=job['failures'][0]['message'])]
    tasks = [format_task(task[0]) for task in job.get('calls').values()]
    return JobMetadataResponse(
        id=id,
        name=job.get('workflowName'),
        status=job.get('status'),
        submission=submission,
        start=start,
        end=end,
        inputs=job.get('inputs'),
        outputs=job.get('outputs'),
        labels=job.get('labels'),
        failures=failures,
        tasks=tasks)


def format_task(task):
    return TaskMetadata(
        job_id=task.get('jobId'),
        execution_status=task.get('executionStatus'),
        start=_parse_datetime(task.get('start')),
        end=_parse_datetime(task.get('end')),
        stderr=task.get('stderr'),
        stdout=task.get('stdout'),
        inputs=task.get('inputs'),
        return_code=task.get('returnCode'))


def query_jobs(body):
    """
    Query jobs by various filter criteria. Returned jobs are ordered from newest to oldest submission time.

    :param body:
    :type body: dict | bytes

    :rtype: QueryJobsResponse
    """
    query = QueryJobsRequest.from_dict(body)
    query_url = _get_base_url() + '/query'
    query_params = format_query_json(query)
    response = requests.post(
        query_url, json=query_params, auth=_get_user_auth())
    results = [format_job(job) for job in response.json()['results']]
    # Reverse so that newest jobs are listed first
    results.reverse()
    return QueryJobsResponse(results=results)


def format_query_json(query):
    query_params = []
    if query.start:
        query_params.append({'start': query.start})
    if query.end:
        query_params.append({'end': query.end})
    if query.name:
        query_params.append({'name': query.name})
    if query.statuses:
        statuses = [{'status': s} for s in set(query.statuses)]
        query_params.extend(statuses)
    return query_params


def format_job(job):
    start = _parse_datetime(job.get('start'))
    end = _parse_datetime(job.get('end'))
    return QueryJobsResult(
        id=job.get('id'),
        name=job.get('name'),
        status=job.get('status'),
        submission=start,
        start=start,
        end=end)


def _parse_datetime(date_string):
    # Handles issue where some dates in cromwell do not contain milliseconds
    # https://github.com/broadinstitute/cromwell/issues/2743
    if not date_string:
        return None
    try:
        formatted_date = datetime.strptime(date_string,
                                           '%Y-%m-%dT%H:%M:%S.%fZ')
    except ValueError:
        try:
            formatted_date = datetime.strptime(date_string,
                                               '%Y-%m-%dT%H:%M:%SZ')
        except ValueError:
            return None
    return formatted_date


def _get_base_url():
    return current_app.config['cromwell_url']


def _get_user_auth():
    return HTTPBasicAuth(current_app.config['cromwell_user'],
                         current_app.config['cromwell_password'])
