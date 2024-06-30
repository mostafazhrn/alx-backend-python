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
        ("abc"),
        ])
    @patch('client.get_json', return_value={"payload": True})
    def test_org(self, org_name, mock_get_json):
        """ This method is to test org """
        valid_op = GithubOrgClient(org_name)
        return_res = valid_op.org
        self.assertEqual(return_res, mock_get_json.return_value)
        mock_get_json.assert_called_once

    def test_public_repos_url(self):
        """ This method shall be the test public_repos_url """
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_pub:
            mock_pub.return_value = TEST_PAYLOAD
            valid_op = GithubOrgClient('google')
            self.assertEqual(valid_op._public_repos_url, TEST_PAYLOAD)

    @patch('client.get_json', return_value=[{'name': 'google'}])
    def test_public_repos(self, mock_get_json):
        """ This method shall test public_repos """
        valid_op = GithubOrgClient('google')
        return_res = valid_op.public_repos()
        self.assertEqual(return_res, ['google'])
        mock_get_json.assert_called_once

    @patch('client.get_json', side_effect=HTTPError())
