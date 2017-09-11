# coding: utf-8

from __future__ import absolute_import
from jobs.models.job_query_result import JobQueryResult
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class JobQueryResponse(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, results=None):
        """
        JobQueryResponse - a model defined in Swagger

        :param results: The results of this JobQueryResponse.
        :type results: List[JobQueryResult]
        """
        self.swagger_types = {
            'results': List[JobQueryResult]
        }

        self.attribute_map = {
            'results': 'results'
        }

        self._results = results

    @classmethod
    def from_dict(cls, dikt):
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The JobQueryResponse of this JobQueryResponse.
        :rtype: JobQueryResponse
        """
        return deserialize_model(dikt, cls)

    @property
    def results(self):
        """
        Gets the results of this JobQueryResponse.

        :return: The results of this JobQueryResponse.
        :rtype: List[JobQueryResult]
        """
        return self._results

    @results.setter
    def results(self, results):
        """
        Sets the results of this JobQueryResponse.

        :param results: The results of this JobQueryResponse.
        :type results: List[JobQueryResult]
        """
        if results is None:
            raise ValueError("Invalid value for `results`, must not be `None`")

        self._results = results

