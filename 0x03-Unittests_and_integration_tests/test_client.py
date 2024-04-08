#!/usr/bin/env python3
"""Module providing unit test for GitHub organization client"""

import unittest
from client import GithubOrgClient
from requests import HTTPError
from fixtures import TEST_PAYLOAD
from unittest.mock import (
    patch,
    Mock,
    MagicMock,
    PropertyMock,
)
from parameterized import parameterized, parameterized_class


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


@parameterized_class([
    {
        'org_payload': TEST_PAYLOAD[0][0],
        'repos_payload': TEST_PAYLOAD[0][1],
        'expected_repos': TEST_PAYLOAD[0][2],
        'apache2_repos': TEST_PAYLOAD[0][3],
    },
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """_summary_

    Args:
            unittest (_type_): _description_

    Returns:
            _type_: _description_
    """
    @classmethod
    def setUpClass(cls) -> None:
        """Set up the test environment before running the tests"""

        route_payload = {
            'https://api.github.com/orgs/google': cls.org_payload,
            'https://api.github.com/orgs/google/repos': cls.repos_payload,
        }

        def get_payload(url):
            """Get the payload for a given URL"""
            if url in route_payload:
                return Mock(**{'json.return_value': route_payload[url]})
            return HTTPError

        cls.get_patcher = patch("requests.get", side_effect=get_payload)
        cls.get_patcher.start()

    def test_public_repos(self) -> None:
        """Test the public_repos method of GithubOrgClient"""
        self.assertEqual(
            GithubOrgClient("google").public_repos(),
            self.expected_repos,
        )

    def test_public_repos_with_license(self) -> None:
        """Test public_repos method of GithubOrgClient with specific license"""
        self.assertEqual(
            GithubOrgClient("google").public_repos(license="apache-2.0"),
            self.apache2_repos,
        )

    @classmethod
    def tearDownClass(cls) -> None:
        """Clean up the test environment after running the tests"""
        cls.get_patcher.stop()
