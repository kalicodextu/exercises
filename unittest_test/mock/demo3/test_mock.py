import unittest
from mock import patch


class Calculator(object):
    def add(self, a, b):
        return a + b

    def is_error(self):
        try:
            os.mkdir("test")
            return False
        except Exception as e:
            return True

class TestProducer(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    @patch.object(Calculator, 'add')
    def test_effect(self, mock_add):
        mock_add.side_effect = [1, 2, 3]
        self.assertEqual(self.calculator.add(8, 14), 1)
        self.assertEqual(self.calculator.add(8, 14), 2)
        self.assertEqual(self.calculator.add(8, 14), 3)

    @patch('os.mkdir')
    def test_exception(self, mock_mkdir):
        mock_mkdir.side_effect = Exception
        self.assertEqual(self.calculator.is_error(), True)

if __name__ == '__main__':
    unittest.main()
