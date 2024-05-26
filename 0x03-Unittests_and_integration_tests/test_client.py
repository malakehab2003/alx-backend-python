#!/usr/bin/env python3
""" create TestGithubOrgClient class """
import unittest
from client import GithubOrgClient
from unittest.mock import PropertyMock, patch, MagicMock
from typing import Dict
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    """ test github org clinet """
    @parameterized.expand([
        ("google", {'login': "google"}),
        ("abc", {'login': "abc"}),
    ])
    @patch(
        "client.get_json",
    )
    def test_org(self, org: str, resp: Dict, mocked_fxn: MagicMock) -> None:
        """Tests the `org` method."""
        mocked_fxn.return_value = MagicMock(return_value=resp)
        gh_org_client = GithubOrgClient(org)
        self.assertEqual(gh_org_client.org(), resp)
        mocked_fxn.assert_called_once_with(
            "https://api.github.com/orgs/{}".format(org)
        )

    @patch('client.GithubOrgClient.org', new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org):
        """ Test the _public_repos_url property """
        payload = {
             'repos_url': 'https://api.github.com/orgs/google/repos'
        }

        mock_org.return_value = payload
        client = GithubOrgClient('google')
        self.assertEqual(client._public_repos_url, payload['repos_url'])

    @patch('client.GithubOrgClient.org', new_callable=PropertyMock)
    def test_public_repos(self, mock_org):
        """ test public repos """
        payload = {
            'repos_url': 'https://api.github.com/orgs/google/repos'
        }
        mock_org.return_value = payload
        client = GithubOrgClient('google')
        self.assertEqual(client._public_repos_url, payload['repos_url'])


if __name__ == '__main__':
    unittest.main()
