#!/usr/bin/env python3
"""Module that provide unit test for generic utilities for
interacting with a GitHub organization client"""

import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock
from utils import access_nested_map, get_json, memoize


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

    @parameterized.expand([
        ({}, ("a",), KeyError),           # Test case 1
        ({"a": 1}, ("a", "b"), KeyError)  # Test case 2
    ])
    def test_access_nested_map_exception(self, nested_map, path,
                                         expected_output):
        """ Method testing access_nested_map function for raising KeyError
        Parameters:
            nested_map (dict): The nested dictionary.=
            path (tuple): The path to access the nested value
            expected_output: The expected exception message
        Test cases:
            Test 1: KeyError: Key 'a' not found in nested map
            Test 2: KeyError: Key 'b' not found in nested map 'a'.")"""

        with self.assertRaises(expected_output) as context:
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Unit test class for the get_json function"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),       # Test case 1
        ("http://holberton.io", {"payload": False}),     # Test case 2
    ])
    def test_get_json(self, url, expected_output):
        """ method testing get_json function by mocking requests.get method
        Args:
            url (str): The URL to fetch JSON from
            expected_output (dict): The expected JSON payload
        Test cases:
            - Test with example.com URL and true payload
            - Test with holberton.io URL and false payload"""

        mock_response = Mock()
        mock_response.json.return_value = expected_output
        with patch('requests.get', return_value=mock_response):
            response = get_json(url)
            self.assertEqual(response, expected_output)


class TestMemoize(unittest.TestCase):
    """Test case class for the memoize decorator"""

    class TestClass:
        """Test class containing a method and a memoized property."""

        def a_method(self):
            """A method that returns 42"""
            return 42

        @memoize
        def a_property(self):
            """A memoized property that calls the a_method"""
            return self.a_method()

    def test_memoize(self):
        """Method to test the memoization of memoized property"""
        # Patching the a_method of TestClass
        with patch.object(self.TestClass, 'a_method') as mock_a_method:
            # Create an instance of TestClass
            test_instance = self.TestClass()

            # Call the memoized property twice
            result1 = test_instance.a_property
            result2 = test_instance.a_property

            # Assert that the a_method was called only once
            mock_a_method.assert_called_once()

            # Assert that the results are equal
            self.assertEqual(result1, result2)
