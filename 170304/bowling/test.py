from main import Frames
import unittest

class BasicTest(unittest.TestCase):
    def test_base(self):
        frames = Frames()
        self.assertEqual('[0]',frames.firstFrame())

    def test_base_true(self):
        self.assertTrue(1 < 2)

if __name__ == '__main__':
    unittest.main()
