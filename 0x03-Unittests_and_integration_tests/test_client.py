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
    @parameterized.expand([
        ({'license': {'key': 'my_license'}}, 'my_license', True),
        ({'license': {'key': 'other_license'}}, 'my_license', False)
    ])
    def test_has_license(self, repo, license, expected):
        """ this instance shall test has_license """
        self.assertEqual(GithubOrgClient.has_license(repo, license), expected)


@parameterized_class(('org_payload', 'repos_payload',
                      'expected_repos', 'apache2_repos'), [
    (org_payload, repos_payload, expected_repos,
     apache2_repos) for org_payload, repos_payload,
    expected_repos, apache2_repos in TEST_PAYLOAD
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """ This instance shall rep class for testing integration GithubClient"""
    @classmethod
    def setUpClass(cls):
        """ This method shall set up the class """
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        """ This method shall tear down the class """
        cls.get_patcher.stop()

    def test_public_repos(self):
        """ This method shall test public_repos """
        self.mock_get.return_value.json.side_effect = [self.org_payload,
                                                       self.repos_payload]
        valid_op = GithubOrgClient('google')
        self.assertEqual(valid_op.org, self.org_payload)
        self.assertEqual(valid_op.repos, self.expected_repos)

    def test_public_repos_with_license(self):
        """ This method shall test public_repos with license """
        x = GithubOrgClient('y')
        self.assertEqual(x.org, self.org_payload)
        self.assertEqual(x.repos_payload, self.repos_payload)
        self.assertEqual(x.public_repos(), self.expected_repos)
        self.assertEqual(x.public_repos('apache-2.0'), self.apache2_repos)
        self.assertEqual(x.public_repos('NONEXISTENT'), [])
        self.get.assert_has_calls([call('https://api.github.com/orgs/y'),
                                   call(self.org_payload['repos_url'])])
