# coding: utf-8

from __future__ import absolute_import
from jobs.models.failure_message import FailureMessage
from jobs.models.job_status import JobStatus
from jobs.models.task_metadata import TaskMetadata
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class JobMetadataResponse(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, name=None, status=None, submission=None, start=None, end=None, inputs=None, outputs=None, labels=None, tasks=None, failures=None):
        """
        JobMetadataResponse - a model defined in Swagger

        :param id: The id of this JobMetadataResponse.
        :type id: str
        :param name: The name of this JobMetadataResponse.
        :type name: str
        :param status: The status of this JobMetadataResponse.
        :type status: JobStatus
        :param submission: The submission of this JobMetadataResponse.
        :type submission: datetime
        :param start: The start of this JobMetadataResponse.
        :type start: datetime
        :param end: The end of this JobMetadataResponse.
        :type end: datetime
        :param inputs: The inputs of this JobMetadataResponse.
        :type inputs: object
        :param outputs: The outputs of this JobMetadataResponse.
        :type outputs: object
        :param labels: The labels of this JobMetadataResponse.
        :type labels: object
        :param tasks: The tasks of this JobMetadataResponse.
        :type tasks: List[TaskMetadata]
        :param failures: The failures of this JobMetadataResponse.
        :type failures: List[FailureMessage]
        """
        self.swagger_types = {
            'id': str,
            'name': str,
            'status': JobStatus,
            'submission': datetime,
            'start': datetime,
            'end': datetime,
            'inputs': object,
            'outputs': object,
            'labels': object,
            'tasks': List[TaskMetadata],
            'failures': List[FailureMessage]
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'status': 'status',
            'submission': 'submission',
            'start': 'start',
            'end': 'end',
            'inputs': 'inputs',
            'outputs': 'outputs',
            'labels': 'labels',
            'tasks': 'tasks',
            'failures': 'failures'
        }

        self._id = id
        self._name = name
        self._status = status
        self._submission = submission
        self._start = start
        self._end = end
        self._inputs = inputs
        self._outputs = outputs
        self._labels = labels
        self._tasks = tasks
        self._failures = failures

    @classmethod
    def from_dict(cls, dikt):
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The JobMetadataResponse of this JobMetadataResponse.
        :rtype: JobMetadataResponse
        """
        return deserialize_model(dikt, cls)

    @property
    def id(self):
        """
        Gets the id of this JobMetadataResponse.
        The identifier of the job

        :return: The id of this JobMetadataResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this JobMetadataResponse.
        The identifier of the job

        :param id: The id of this JobMetadataResponse.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this JobMetadataResponse.
        The name of the job

        :return: The name of this JobMetadataResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this JobMetadataResponse.
        The name of the job

        :param name: The name of this JobMetadataResponse.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def status(self):
        """
        Gets the status of this JobMetadataResponse.

        :return: The status of this JobMetadataResponse.
        :rtype: JobStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this JobMetadataResponse.

        :param status: The status of this JobMetadataResponse.
        :type status: JobStatus
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")

        self._status = status

    @property
    def submission(self):
        """
        Gets the submission of this JobMetadataResponse.
        Submission datetime of the job in ISO8601 format with milliseconds

        :return: The submission of this JobMetadataResponse.
        :rtype: datetime
        """
        return self._submission

    @submission.setter
    def submission(self, submission):
        """
        Sets the submission of this JobMetadataResponse.
        Submission datetime of the job in ISO8601 format with milliseconds

        :param submission: The submission of this JobMetadataResponse.
        :type submission: datetime
        """
        if submission is None:
            raise ValueError("Invalid value for `submission`, must not be `None`")

        self._submission = submission

    @property
    def start(self):
        """
        Gets the start of this JobMetadataResponse.
        Start datetime of the job in ISO8601 format with milliseconds

        :return: The start of this JobMetadataResponse.
        :rtype: datetime
        """
        return self._start

    @start.setter
    def start(self, start):
        """
        Sets the start of this JobMetadataResponse.
        Start datetime of the job in ISO8601 format with milliseconds

        :param start: The start of this JobMetadataResponse.
        :type start: datetime
        """

        self._start = start

    @property
    def end(self):
        """
        Gets the end of this JobMetadataResponse.
        End datetime of the job in ISO8601 format with milliseconds

        :return: The end of this JobMetadataResponse.
        :rtype: datetime
        """
        return self._end

    @end.setter
    def end(self, end):
        """
        Sets the end of this JobMetadataResponse.
        End datetime of the job in ISO8601 format with milliseconds

        :param end: The end of this JobMetadataResponse.
        :type end: datetime
        """

        self._end = end

    @property
    def inputs(self):
        """
        Gets the inputs of this JobMetadataResponse.
        Map of input keys to input values

        :return: The inputs of this JobMetadataResponse.
        :rtype: object
        """
        return self._inputs

    @inputs.setter
    def inputs(self, inputs):
        """
        Sets the inputs of this JobMetadataResponse.
        Map of input keys to input values

        :param inputs: The inputs of this JobMetadataResponse.
        :type inputs: object
        """

        self._inputs = inputs

    @property
    def outputs(self):
        """
        Gets the outputs of this JobMetadataResponse.
        Map of output keys to output values

        :return: The outputs of this JobMetadataResponse.
        :rtype: object
        """
        return self._outputs

    @outputs.setter
    def outputs(self, outputs):
        """
        Sets the outputs of this JobMetadataResponse.
        Map of output keys to output values

        :param outputs: The outputs of this JobMetadataResponse.
        :type outputs: object
        """

        self._outputs = outputs

    @property
    def labels(self):
        """
        Gets the labels of this JobMetadataResponse.
        Custom job labels with string values

        :return: The labels of this JobMetadataResponse.
        :rtype: object
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """
        Sets the labels of this JobMetadataResponse.
        Custom job labels with string values

        :param labels: The labels of this JobMetadataResponse.
        :type labels: object
        """

        self._labels = labels

    @property
    def tasks(self):
        """
        Gets the tasks of this JobMetadataResponse.

        :return: The tasks of this JobMetadataResponse.
        :rtype: List[TaskMetadata]
        """
        return self._tasks

    @tasks.setter
    def tasks(self, tasks):
        """
        Sets the tasks of this JobMetadataResponse.

        :param tasks: The tasks of this JobMetadataResponse.
        :type tasks: List[TaskMetadata]
        """

        self._tasks = tasks

    @property
    def failures(self):
        """
        Gets the failures of this JobMetadataResponse.

        :return: The failures of this JobMetadataResponse.
        :rtype: List[FailureMessage]
        """
        return self._failures

    @failures.setter
    def failures(self, failures):
        """
        Sets the failures of this JobMetadataResponse.

        :param failures: The failures of this JobMetadataResponse.
        :type failures: List[FailureMessage]
        """

        self._failures = failures

