#!/usr/bin/env python3
""" create class TestAccessNestedMap """
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
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

            
class TestMemoize(unittest.TestCase):
    """ test the memoize function """
    def test_memoize(self) -> None:
        """ test the memoize function """
        class TestClass:
            """ create test class """
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()
        with patch.object(TestClass, 'a_method', return_value = lambda: 42) as mock_method:
            re1 = TestClass()
            self.assertEqual(re1.a_property(), 42)
            self.assertEqual(re1.a_property(), 42)
            mock_method.assert_called_once()

if __name__ == '__main__':
    unittest.main()
