import unittest
from main import ConvertTime

class DojoTests(unittest.TestCase):

    def setUp(self):
        self.cv = ConvertTime()

    def test_recv_a_number_hour_minute_and_conv_into_string(self):
        self.assertTrue(type(self.cv.recv_time(5, 45)), '__str__')

    def test_range_hour_between_one_and_eleven(self):
        hour, minute = 0, 45
        result = self.cv.recv_time(hour, minute)
        self.assertEqual(result, 'ERROR')

    def test_range_minute_between_zero_and_sixty(self):
        hour, minute = 5, 61
        result = self.cv.recv_time(hour, minute)
        self.assertEqual(result, 'ERROR')

    def test_correct_conv_hour(self):
        hour, minute = 5, 32
        result = self.cv.recv_time(hour, minute)
        self.assertIn('cinco horas', result)

    def test_correct_conv_minute(self):
        hour, minute = 5, 32
        result = self.cv.recv_time(hour, minute)
        self.assertIn('trinta e dois minutos', result)

    def test_hour_with_zero_minute(self):
        hour, minute = 5, 00
        result = self.cv.recv_time(hour, minute)
        self.assertEqual(result, 'cinco horas')

    def test_minute_singular(self):
        hour, minute = 5, 1
        result = self.cv.recv_time(hour, minute)
        self.assertEqual(result, 'cinco horas e um minuto')

    def test_first_sprint(self):
        hour, minute = 3, 00
        result = self.cv.recv_time(hour, minute)
        self.assertEqual(result, 'três horas')

        hour, minute = 3, 1
        result = self.cv.recv_time(hour, minute)
        self.assertEqual(result, 'três horas e um minuto')

        hour, minute = 6, 56
        result = self.cv.recv_time(hour, minute)
        self.assertEqual(result, 'seis horas e cinquenta e seis minutos')

        hour, minute = 1, 15
        result = self.cv.recv_time(hour, minute)
        self.assertEqual(result, 'uma hora e quinze minutos')

        hour, minute = 4, 30
        result = self.cv.recv_time(hour, minute)
        self.assertEqual(result, 'quatro horas e trinta minutos')

if __name__ == '__main__':
    unittest.main()
