# coding: utf-8

"""
    NiFi Rest Api

    The Rest Api provides programmatic access to command and control a NiFi instance in real time. Start and                                              stop processors, monitor queues, query provenance data, and more. Each endpoint below includes a description,                                             definitions of the expected input and output, potential response codes, and the authorizations required                                             to invoke each service.

    OpenAPI spec version: 1.2.0
    Contact: dev@nifi.apache.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import nipyapi
from nipyapi.swagger_client.rest import ApiException
from nipyapi.swagger_client.apis.controllerservices_api import ControllerservicesApi


class TestControllerservicesApi(unittest.TestCase):
    """ ControllerservicesApi unit test stubs """

    def setUp(self):
        self.api =nipyapi.swagger_client.apis.controllerservices_api.ControllerservicesApi()

    def tearDown(self):
        pass

    def test_clear_state(self):
        """
        Test case for clear_state

        Clears the state for a controller service
        """
        pass

    def test_get_controller_service(self):
        """
        Test case for get_controller_service

        Gets a controller service
        """
        pass

    def test_get_controller_service_references(self):
        """
        Test case for get_controller_service_references

        Gets a controller service
        """
        pass

    def test_get_property_descriptor(self):
        """
        Test case for get_property_descriptor

        Gets a controller service property descriptor
        """
        pass

    def test_get_state(self):
        """
        Test case for get_state

        Gets the state for a controller service
        """
        pass

    def test_remove_controller_service(self):
        """
        Test case for remove_controller_service

        Deletes a controller service
        """
        pass

    def test_update_controller_service(self):
        """
        Test case for update_controller_service

        Updates a controller service
        """
        pass

    def test_update_controller_service_references(self):
        """
        Test case for update_controller_service_references

        Updates a controller services references
        """
        pass


if __name__ == '__main__':
    unittest.main()
