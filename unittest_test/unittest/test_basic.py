#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest


class TestStringMethods(unittest.TestCase):
    def test_upper(self):
        self.assertEquals('foo'.upper(), 'FOO')

    @unittest.expectedFailure
    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEquals(s.split(), ['hello', 'world'])
        with self.assertRaises(TypeError):
            s.split(2)


if __name__ == '__main__':
    # method 1
    '''
    unittest.main()
    '''

    # method 2

    suite = unittest.TestLoader().loadTestsFromTestCase(TestStringMethods)
    unittest.TextTestRunner(verbosity=2).run(suite)
    print suite.countTestCases()

    # method 3
    '''
    basic_testSuite = unittest.TestSuite()
    basic_testSuite.addTest(TestStringMethods("test_upper"))
    basic_testSuite.addTest(TestStringMethods("test_isupper"))
    unittest.TextTestRunner(verbosity=2).run(basic_testSuite)
    '''
