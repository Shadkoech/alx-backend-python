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

    @patch('client.get_json')
    @patch.object(GithubOrgClient, '_public_repos_url',
                  new_callable=PropertyMock)
    def test_public_repos(self, mock_public_repos_url, mock_get_json):
        """Test the public_repos method of GithubOrgClient."""
        # Define a known payload for the mocked get_json function
        payload = [
            {"name": "repo1", "license": {"key": "MIT"}},
            {"name": "repo2", "license": {"key": "Apache"}},
            {"name": "repo3", "license": {"key": "GPL"}},
        ]
        # Patch the return value of the mocked get_json function
        mock_get_json.return_value = payload

        # Set the return value of the mocked _public_repos_url property
        mock_public_repos_url.return_value = \
            "https://api.github.com/orgs/example/repos"

        # Create an instance of GithubOrgClient
        github_client = GithubOrgClient("example")

        # Call the public_repos method
        repos = github_client.public_repos()

        # Assert that the return value matches the expected list of repos
        self.assertEqual(repos, ["repo1", "repo2", "repo3"])

        # Assert that the mocked get_json was called once
        mock_get_json.assert_called_once()

        # Assert that the mocked _public_repos_url property was called once
        mock_public_repos_url.assert_called_once()

    @parameterized.expand([
        ({'license': {'key': "bsd-3-clause"}}, "bsd-3-clause", True),
        ({'license': {'key': "bsl-1.0"}}, "bsd-3-clause", False),
    ])
    def test_has_license(self, repo: dict, key: str, expected: bool) -> None:
        """Test method to check the has_license method
        Args:
            repo (dict): repository data containing the license information
            key (str): The license key to check
            expected (bool): expected result of `has_license` method"""

        # Create instance of GithubOrgClient with organization name "google"
        gh_org_client = GithubOrgClient("google")

        # Call has_license method with provided repo and key
        client_has_license = gh_org_client.has_license(repo, key)

        # Assert that returned result matches expected result for each testcase
        self.assertEqual(client_has_license, expected)
