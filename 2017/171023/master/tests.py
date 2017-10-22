import unittest
from main import ConvertTime

class DojoTests(unittest.TestCase):

    def test_recv_a_number_hour_minute_and_conv_into_string(self):
        cv = ConvertTime()
        self.assertTrue(type(cv.recv_time(5, 45)), '__str__')

    def test_range_hour_between_one_and_eleven(self):
        cv = ConvertTime()
        hour, minute = 0, 45
        result = cv.recv_time(hour, minute)
        self.assertEqual(result, 'ERROR')

    def test_range_minute_between_zero_and_sixty(self):
        cv = ConvertTime()
        hour, minute = 5, 61
        result = cv.recv_time(hour, minute)
        self.assertEqual(result, 'ERROR')

if __name__ == '__main__':
    unittest.main()
