# coding: utf-8

from __future__ import absolute_import
from jobs.models.display_field import DisplayField
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class BulkLabelField(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, default=None, display_field=None):
        """
        BulkLabelField - a model defined in Swagger

        :param default: The default of this BulkLabelField.
        :type default: str
        :param display_field: The display_field of this BulkLabelField.
        :type display_field: DisplayField
        """
        self.swagger_types = {
            'default': str,
            'display_field': DisplayField
        }

        self.attribute_map = {
            'default': 'default',
            'display_field': 'displayField'
        }

        self._default = default
        self._display_field = display_field

    @classmethod
    def from_dict(cls, dikt):
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The BulkLabelField of this BulkLabelField.
        :rtype: BulkLabelField
        """
        return deserialize_model(dikt, cls)

    @property
    def default(self):
        """
        Gets the default of this BulkLabelField.

        :return: The default of this BulkLabelField.
        :rtype: str
        """
        return self._default

    @default.setter
    def default(self, default):
        """
        Sets the default of this BulkLabelField.

        :param default: The default of this BulkLabelField.
        :type default: str
        """

        self._default = default

    @property
    def display_field(self):
        """
        Gets the display_field of this BulkLabelField.

        :return: The display_field of this BulkLabelField.
        :rtype: DisplayField
        """
        return self._display_field

    @display_field.setter
    def display_field(self, display_field):
        """
        Sets the display_field of this BulkLabelField.

        :param display_field: The display_field of this BulkLabelField.
        :type display_field: DisplayField
        """
        if display_field is None:
            raise ValueError("Invalid value for `display_field`, must not be `None`")

        self._display_field = display_field
