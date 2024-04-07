#!/usr/bin/env python3
"""Module that provide unit test for generic utilities for
interacting with a GitHub organization client"""

import unittest
from utils import access_nested_map
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """Unit test class for the access_nested_map function."""

    @parameterized.expand([
        ({"a": 1}, ["a"], 1),                # Test case 1
        ({"a": {"b": 2}}, ["a"], {"b": 2}),  # Test case 2
        ({"a": {"b": 2}}, ["a", "b"], 2)     # Test case 3
    ])
    def test_access_nested_map(self, nested_map, path, expected_output):
        """Method testing access_nested_map function with varied input
        Parameters:
            nested_map (dict): The nested dictionary
            path(tuple): The path to access the nested value
            expected_output: expected output when accessing the nested value
        Test cases:
            Test case 1: Accessing a value directly
            Test case 2: Accessing a nested dictionary
            Test case 3: Accessing a nested value
            """
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected_output)
