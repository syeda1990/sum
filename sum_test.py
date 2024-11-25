import unittest
from sum import sum

class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum(4,4),8)

if __name__ == '__main__':
    unittest.main()
