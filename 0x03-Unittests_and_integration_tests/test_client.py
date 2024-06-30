#!/usr/bin/env python3
""" This script is a unitest module for testing utils.py """
import unittest
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
from parameterized import parameterized
from unittest.mock import patch, Mock, PropertyMock
from urllib.error import HTTPError


class TestGithubOrgClient(unittest.TestCase):
    """ This instance shall rep a class for testin test_client.py """
    @parameterized.expand([
        ("google"),
        ("abc")
        ])
    @patch('client.get_json', return_value={"payload": True})
    def test_org(self, org_name, mock_get_json):
        """ This method is to test org """
        valid_op = GithubOrgClient(org_name)
        return_res = valid_op.org
        self.assertEqual(return_res, mock_get_json.return_value)
        mock_get_json.assert_called_once
