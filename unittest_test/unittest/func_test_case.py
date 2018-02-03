#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from unittest import FunctionTestCase


class makeSomething(object):
    def __init__(self):
        self.name = None


def testSomething():
    something = makeSomething()
    assert something.name is not None


testcase = FunctionTestCase(testSomething)

if __name__ == '__main__':
    unittest.main()
