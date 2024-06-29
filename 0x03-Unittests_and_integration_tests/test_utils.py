#!/usr/bin/env python3
""" This script is a unitest module for testing utils.py """
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch, Mock
from unittest import mock, TestCase


class TestAccessNestedMap(TestCase):
    """ This instance is a class for testing above func"""
    @parameterized.expand([
        ({'a': 1}, ('a',), 1),
        ({'a': {'b': 2}}, ("a",), {'b': 2}),
        ({'a': {'b': 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, result):
        """ This method is to test access_nested_map """
        valid_op = access_nested_map(nested_map, path)
        self.assertEqual(valid_op, result)

    @parameterized.expand([
        ({}, ("a",), 'a'),
        ({'a': 1}, ('a', 'b'), 'b')
    ])
    def test_access_nested_map_exception(self, nested_map, path, not_res):
        """ this method shall test access_nested_map exception """
        with self.assertRaises(KeyError) as error:
            access_nested_map(nested_map, path)
        self.assertEqual(error.exception.args[0], path[-1])


class TestGetJson(unittest.TestCase):
    """ This instance is a class for testing above func"""
    @parameterized.expand([
        ('http://example.com', {'payload': True}),
        ('http://holberton.io', {'payload': False})
    ])
    @patch('test_utils.get_json')
    def test_get_json(self, url, payload, mock_get):
        """ This method is to test get_json """
        mock_get.return_value = payload
        valid_op = get_json(url)
        self.assertEqual(valid_op, payload)


class TestMemoize(unittest.TestCase):
    """ This instance shall rep  a class for testing the memoize func"""
    def test_memoize(self):
        """ This method shall be the test memoize """
        class TestClass:
            """ This instance shall rep class for testing the memoize func"""
            def a_method(self):
                """ This method shall rep to test memoize """
                return 42

            @memoize
            def a_property(self):
                """ This method is to test memoize """
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mock_method:
            class_preuba = TestClass()
            class_preuba.a_property
            class_preuba.a_property
            mock_method.assert_called_once()
