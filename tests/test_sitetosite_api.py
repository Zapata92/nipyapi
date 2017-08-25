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
from nipyapi.swagger_client.apis.sitetosite_api import SitetositeApi


class TestSitetositeApi(unittest.TestCase):
    """ SitetositeApi unit test stubs """

    def setUp(self):
        self.api =nipyapi.swagger_client.apis.sitetosite_api.SitetositeApi()

    def tearDown(self):
        pass

    def test_get_peers(self):
        """
        Test case for get_peers

        Returns the available Peers and its status of this NiFi
        """
        pass

    def test_get_site_to_site_details(self):
        """
        Test case for get_site_to_site_details

        Returns the details about this NiFi necessary to communicate via site to site
        """
        pass


if __name__ == '__main__':
    unittest.main()
