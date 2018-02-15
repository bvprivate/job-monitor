# coding: utf-8

from __future__ import absolute_import
from jobs.models.authentication_capability import AuthenticationCapability
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class CapabilitiesResponse(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, authentication=None, display_fields=None, common_labels=None, extended_query_fields=None):
        """
        CapabilitiesResponse - a model defined in Swagger

        :param authentication: The authentication of this CapabilitiesResponse.
        :type authentication: AuthenticationCapability
        :param display_fields: The display_fields of this CapabilitiesResponse.
        :type display_fields: object
        :param common_labels: The common_labels of this CapabilitiesResponse.
        :type common_labels: List[str]
        :param extended_query_fields: The extended_query_fields of this CapabilitiesResponse.
        :type extended_query_fields: List[str]
        """
        self.swagger_types = {
            'authentication': AuthenticationCapability,
            'display_fields': object,
            'common_labels': List[str],
            'extended_query_fields': List[str]
        }

        self.attribute_map = {
            'authentication': 'authentication',
            'display_fields': 'displayFields',
            'common_labels': 'commonLabels',
            'extended_query_fields': 'extendedQueryFields'
        }

        self._authentication = authentication
        self._display_fields = display_fields
        self._common_labels = common_labels
        self._extended_query_fields = extended_query_fields

    @classmethod
    def from_dict(cls, dikt):
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The CapabilitiesResponse of this CapabilitiesResponse.
        :rtype: CapabilitiesResponse
        """
        return deserialize_model(dikt, cls)

    @property
    def authentication(self):
        """
        Gets the authentication of this CapabilitiesResponse.

        :return: The authentication of this CapabilitiesResponse.
        :rtype: AuthenticationCapability
        """
        return self._authentication

    @authentication.setter
    def authentication(self, authentication):
        """
        Sets the authentication of this CapabilitiesResponse.

        :param authentication: The authentication of this CapabilitiesResponse.
        :type authentication: AuthenticationCapability
        """

        self._authentication = authentication

    @property
    def display_fields(self):
        """
        Gets the display_fields of this CapabilitiesResponse.
        Fields on QueryJobsResult returned from POST /jobs/query populated on some or all jobs. The fields are mapped to their display names, in order of importance. Extended fields and labels can be included, such as 'label.foo' or 'extendedFields.userId' 

        :return: The display_fields of this CapabilitiesResponse.
        :rtype: object
        """
        return self._display_fields

    @display_fields.setter
    def display_fields(self, display_fields):
        """
        Sets the display_fields of this CapabilitiesResponse.
        Fields on QueryJobsResult returned from POST /jobs/query populated on some or all jobs. The fields are mapped to their display names, in order of importance. Extended fields and labels can be included, such as 'label.foo' or 'extendedFields.userId' 

        :param display_fields: The display_fields of this CapabilitiesResponse.
        :type display_fields: object
        """

        self._display_fields = display_fields

    @property
    def common_labels(self):
        """
        Gets the common_labels of this CapabilitiesResponse.
        Common labels which are present on most jobs returned

        :return: The common_labels of this CapabilitiesResponse.
        :rtype: List[str]
        """
        return self._common_labels

    @common_labels.setter
    def common_labels(self, common_labels):
        """
        Sets the common_labels of this CapabilitiesResponse.
        Common labels which are present on most jobs returned

        :param common_labels: The common_labels of this CapabilitiesResponse.
        :type common_labels: List[str]
        """

        self._common_labels = common_labels

    @property
    def extended_query_fields(self):
        """
        Gets the extended_query_fields of this CapabilitiesResponse.
        Fields on ExtendedQueryFields which are queryable

        :return: The extended_query_fields of this CapabilitiesResponse.
        :rtype: List[str]
        """
        return self._extended_query_fields

    @extended_query_fields.setter
    def extended_query_fields(self, extended_query_fields):
        """
        Sets the extended_query_fields of this CapabilitiesResponse.
        Fields on ExtendedQueryFields which are queryable

        :param extended_query_fields: The extended_query_fields of this CapabilitiesResponse.
        :type extended_query_fields: List[str]
        """

        self._extended_query_fields = extended_query_fields

