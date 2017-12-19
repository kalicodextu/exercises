import unittest
import sys


class mylib(object):
    __version__ = (1, 2)


class MyTestCase(unittest.TestCase):
    @unittest.skip("demonstrating skipping")
    def test_nothing(self):
        self.fail("shouldn't happen")

    @unittest.skipIf(mylib.__version__ < (1, 3),
                     "not supported in this library version")
    def test_format(self):
        # Tests that work for only a certain version of the library.
        pass

    @unittest.skipUnless(sys.platform.startswith("win"), "requires Windows")
    def test_windows_support(self):
        # windows specific testing code
        pass


if __name__ == '__main__':
    unittest.main()

# cmd:
# python -m unittest -v widge_test
# output:
# ttest -v widge_test
# test_format (widge_test.MyTestCase) ... skipped 'not supported in this library version'
# test_nothing (widge_test.MyTestCase) ... skipped 'demonstrating skipping'
# test_windows_support (widge_test.MyTestCase) ... skipped 'requires Windows'
#
# ----------------------------------------------------------------------
# Ran 3 tests in 0.000s
#
# OK (skipped=3)
