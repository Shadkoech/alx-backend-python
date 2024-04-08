#!/usr/bin/env python3
"""Module providing unit test for GitHub organization client"""

import unittest
from parameterized import parameterized
from client import GithubOrgClient
from unittest.mock import (
    patch,
    MagicMock,
    PropertyMock,
)


class TestGithubOrgClient(unittest.TestCase):
    """Test case class for the GithubOrgClient class"""

    @parameterized.expand([
        ("google", {'login': "google"}),
        ("abc", {'login': "abc"}),
    ])
    @patch('client.get_json')
    def test_org(self, org: str, expected_response: dict,
                 mocked_function: MagicMock) -> None:
        """Testing org method of GithubOrgClient by mocking get_json function
        Args:
            org (str): The organization name
            expected_response (dict): Expected response from get_json function
            mocked_function (MagicMock): The mocked get_json function"""

        # Mock the return value of get_json
        mocked_function.return_value = MagicMock(
            return_value=expected_response)

        # Initialize GithubOrgClient with the org name
        github_client = GithubOrgClient(org)

        # Call org method and assert that
        # returned response matches expected response
        self.assertEqual(github_client.org(), expected_response)

        # Assert that get_json was called once with the correct URL
        mocked_function.assert_called_once_with
        ("https://api.github.com/orgs/{}".format(org))

    def test_public_repos_url(self):
        """Test method ensuring _public_repos_url property of
        GithubOrgClient is correct"""
        # Patch the org property of GithubOrgClient
        with patch("client.GithubOrgClient.org", new_callable=PropertyMock) \
                as mock_org:
            # Set the return value of the mocked org property
            mock_org.return_value = {
                'repos_url': "https://api.github.com/users/google/repos",
                }
            # Create an instance of GithubOrgClient with org name "google"
            # Access _public_repos_url and check if it matches expected value
            self.assertEqual(
                GithubOrgClient("google")._public_repos_url,
                "https://api.github.com/users/google/repos",
            )
