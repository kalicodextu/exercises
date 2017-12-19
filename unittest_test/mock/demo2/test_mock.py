#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from mock import patch

import function 


class MyTestCase(unittest.TestCase):

    @patch("function.multiply")
    def test_add_and_mutiply(self, mock_multiply):
        mock_multiply.return_value = 15
        addition, multiply = function.add_and_multiply(3, 5)
        mock_multiply.assert_called_once_with(3, 5)
        self.assertEquals(8, addition)
        self.assertEquals(15, multiply)


if __name__ == '__main__':
    unittest.main()
