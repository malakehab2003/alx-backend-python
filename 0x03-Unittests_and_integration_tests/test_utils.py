#!/usr/bin/env python3
""" create class TestAccessNestedMap """
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json
from typing import Dict, Tuple, Union
from unittest.mock import patch, Mock


class TestAccessNestedMap(unittest.TestCase):
    """ try test with utils.access_nested_map """
    @parameterized.expand([
        ({'a': 1}, ('a',), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])

    def test_access_nested_map(self, map: Dict, path: Tuple[str], ex: Union[Dict, int]) -> None:
        """ test nested map """
        self.assertEqual(access_nested_map(map, path), ex)


    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a", 1}, ("a", "b"), KeyError),
    ])

    def test_access_nested_map_exception(self, map: Dict, path: Tuple[str], ex: Exception) -> None:
        """ test nested loop with exception """
        with self.assertRaises(ex):
            access_nested_map(map, path)


class TestGetJson(unittest.TestCase):
    """ test with utils.get_json """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, url: str, payload: Dict) -> None:
        """ test get json function """
        with patch('utils.requests.get') as mock_get:
            mock_respond = Mock()
            mock_respond.json.return_value = payload
            mock_get.return_value = mock_respond
            
            result = get_json(url)
            
            mock_get.assert_called_once_with(url)
            self.assertEqual(result, payload)


if __name__ == '__main__':
    unittest.main()
