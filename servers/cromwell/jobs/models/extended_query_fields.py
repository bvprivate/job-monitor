# coding: utf-8

from __future__ import absolute_import
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class ExtendedQueryFields(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, project_id=None, submission=None, user_id=None):
        """
        ExtendedQueryFields - a model defined in Swagger

        :param project_id: The project_id of this ExtendedQueryFields.
        :type project_id: str
        :param submission: The submission of this ExtendedQueryFields.
        :type submission: datetime
        :param user_id: The user_id of this ExtendedQueryFields.
        :type user_id: str
        """
        self.swagger_types = {
            'project_id': str,
            'submission': datetime,
            'user_id': str
        }

        self.attribute_map = {
            'project_id': 'projectId',
            'submission': 'submission',
            'user_id': 'userId'
        }

        self._project_id = project_id
        self._submission = submission
        self._user_id = user_id

    @classmethod
    def from_dict(cls, dikt):
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ExtendedQueryFields of this ExtendedQueryFields.
        :rtype: ExtendedQueryFields
        """
        return deserialize_model(dikt, cls)

    @property
    def project_id(self):
        """
        Gets the project_id of this ExtendedQueryFields.
        Returns only jobs with the specified project ID. If specified by the /capabilities endpoint, this field is required for all query requests. 

        :return: The project_id of this ExtendedQueryFields.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """
        Sets the project_id of this ExtendedQueryFields.
        Returns only jobs with the specified project ID. If specified by the /capabilities endpoint, this field is required for all query requests. 

        :param project_id: The project_id of this ExtendedQueryFields.
        :type project_id: str
        """

        self._project_id = project_id

    @property
    def submission(self):
        """
        Gets the submission of this ExtendedQueryFields.
        Returns only jobs with an equal or later submission datetime. 

        :return: The submission of this ExtendedQueryFields.
        :rtype: datetime
        """
        return self._submission

    @submission.setter
    def submission(self, submission):
        """
        Sets the submission of this ExtendedQueryFields.
        Returns only jobs with an equal or later submission datetime. 

        :param submission: The submission of this ExtendedQueryFields.
        :type submission: datetime
        """

        self._submission = submission

    @property
    def user_id(self):
        """
        Gets the user_id of this ExtendedQueryFields.
        Returns only jobs with the specified user ID. 

        :return: The user_id of this ExtendedQueryFields.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """
        Sets the user_id of this ExtendedQueryFields.
        Returns only jobs with the specified user ID. 

        :param user_id: The user_id of this ExtendedQueryFields.
        :type user_id: str
        """

        self._user_id = user_id

