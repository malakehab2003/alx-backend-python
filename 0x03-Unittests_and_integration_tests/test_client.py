#!/usr/bin/env python3
""" create TestGithubOrgClient class """
import unittest
from client import GithubOrgClient
from unittest.mock import Mock, patch, MagicMock
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


if __name__ == '__main__':
    unittest.main()
