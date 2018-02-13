# coding: utf-8

from __future__ import absolute_import
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class AuthenticationCapability(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, required=None, client_id=None, scopes=None):
        """
        AuthenticationCapability - a model defined in Swagger

        :param required: The required of this AuthenticationCapability.
        :type required: bool
        :param client_id: The client_id of this AuthenticationCapability.
        :type client_id: str
        :param scopes: The scopes of this AuthenticationCapability.
        :type scopes: List[str]
        """
        self.swagger_types = {
            'required': bool,
            'client_id': str,
            'scopes': List[str]
        }

        self.attribute_map = {
            'required': 'required',
            'client_id': 'client_id',
            'scopes': 'scopes'
        }

        self._required = required
        self._client_id = client_id
        self._scopes = scopes

    @classmethod
    def from_dict(cls, dikt):
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AuthenticationCapability of this AuthenticationCapability.
        :rtype: AuthenticationCapability
        """
        return deserialize_model(dikt, cls)

    @property
    def required(self):
        """
        Gets the required of this AuthenticationCapability.
        Whether or not authentication is required

        :return: The required of this AuthenticationCapability.
        :rtype: bool
        """
        return self._required

    @required.setter
    def required(self, required):
        """
        Sets the required of this AuthenticationCapability.
        Whether or not authentication is required

        :param required: The required of this AuthenticationCapability.
        :type required: bool
        """
        if required is None:
            raise ValueError("Invalid value for `required`, must not be `None`")

        self._required = required

    @property
    def client_id(self):
        """
        Gets the client_id of this AuthenticationCapability.
        OAuth 2.0 client ID

        :return: The client_id of this AuthenticationCapability.
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """
        Sets the client_id of this AuthenticationCapability.
        OAuth 2.0 client ID

        :param client_id: The client_id of this AuthenticationCapability.
        :type client_id: str
        """

        self._client_id = client_id

    @property
    def scopes(self):
        """
        Gets the scopes of this AuthenticationCapability.
        OAuth 2.0 requested scopes

        :return: The scopes of this AuthenticationCapability.
        :rtype: List[str]
        """
        return self._scopes

    @scopes.setter
    def scopes(self, scopes):
        """
        Sets the scopes of this AuthenticationCapability.
        OAuth 2.0 requested scopes

        :param scopes: The scopes of this AuthenticationCapability.
        :type scopes: List[str]
        """

        self._scopes = scopes

