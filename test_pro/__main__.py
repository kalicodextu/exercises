# the main file

import pytest
from api_uri import *
from test_api import *


class MyPlugin(object):
    def pytest_sessionfinish(self):
        print '\n\n'
        print '***** test run reporting finishing *****'


if __name__ == '__nain__':
    pytest.main(["-s", "-v"], plugins=[MyPlugin()])
