#!/usr/bin/env python3
""" create class TestAccessNestedMap """
import unittest
from parameterized import parameterized
from utils import access_nested_map
from typing import Dict, Tuple, Union


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


if __name__ == '__main__':
    unittest.main()
