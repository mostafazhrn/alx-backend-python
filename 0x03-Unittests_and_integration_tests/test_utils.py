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
