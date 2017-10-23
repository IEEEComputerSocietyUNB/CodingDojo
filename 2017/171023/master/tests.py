import unittest
from main import ConvertTime

class DojoTests(unittest.TestCase):

    def setUp(self):
        self.cv = ConvertTime()

    def test_recv_hour_minute_and_conv_into_string(self):
        self.assertTrue(type(self.cv.recv_time_literal_time('5:45')), '__str__')

    def test_range_hour_between_one_and_eleven(self):
        hour_minute = '0:45'
        result = self.cv.recv_time_literal_time(hour_minute)
        self.assertEqual(result, 'ERROR')

    def test_range_minute_between_zero_and_sixty(self):
        hour_minute = '5:61'
        result = self.cv.recv_time_literal_time(hour_minute)
        self.assertEqual(result, 'ERROR')

    def test_correct_conv_hour(self):
        hour_minute = '5:32'
        result = self.cv.recv_time_literal_time(hour_minute)
        self.assertIn('cinco horas', result)

    def test_correct_conv_minute(self):
        hour_minute = '5:32'
        result = self.cv.recv_time_literal_time(hour_minute)
        self.assertIn('trinta e dois minutos', result)

    def test_hour_with_zero_minute(self):
        hour_minute = '5:00'
        result = self.cv.recv_time_literal_time(hour_minute)
        self.assertEqual(result, 'cinco horas')

    def test_minute_singular(self):
        hour_minute = '5:01'
        result = self.cv.recv_time_literal_time(hour_minute)
        self.assertEqual(result, 'cinco horas e um minuto')

    def test_first_sprint(self):
        hour_minute = '3:00'
        result = self.cv.recv_time_literal_time(hour_minute)
        self.assertEqual(result, 'três horas')

        hour_minute = '3:01'
        result = self.cv.recv_time_literal_time(hour_minute)
        self.assertEqual(result, 'três horas e um minuto')

        hour_minute = '6:56'
        result = self.cv.recv_time_literal_time(hour_minute)
        self.assertEqual(result, 'seis horas e cinquenta e seis minutos')

        hour_minute = '1:15'
        result = self.cv.recv_time_literal_time(hour_minute)
        self.assertEqual(result, 'uma hora e quinze minutos')

        hour_minute = '4:30'
        result = self.cv.recv_time_literal_time(hour_minute)
        self.assertEqual(result, 'quatro horas e trinta minutos')

    def test_twenty_to_the_next_hour(self):
        hour_minute = '4:40'
        result = self.cv.recv_time_correct_time(hour_minute)
        self.assertEqual(result, 'vinte minutos para as cinco')

    def test_half_hour(self):
        hour_minute = '4:30'
        result = self.cv.recv_time_correct_time(hour_minute)
        self.assertEqual(result, 'quatro e meia')

    def test_second_sprint(self):
        hour_minute = '3:00'
        result = self.cv.recv_time_correct_time(hour_minute)
        self.assertEqual(result, 'três horas')

        hour_minute = '3:01'
        result = self.cv.recv_time_correct_time(hour_minute)
        self.assertEqual(result, 'três horas e um minuto')

        hour_minute = '6:56'
        result = self.cv.recv_time_correct_time(hour_minute)
        self.assertEqual(result, 'quatro minutos para as sete')

        hour_minute = '1:30'
        result = self.cv.recv_time_correct_time(hour_minute)
        self.assertEqual(result, 'uma e meia')

        hour_minute = '4:40'
        result = self.cv.recv_time_correct_time(hour_minute)
        self.assertEqual(result, 'vinte minutos para as cinco')

    def test_rcv_utc(self):
        hour_minute = '3:00 UTC'
        result = self.cv.time_with_utc(hour_minute)
        self.assertEqual(result, 'três horas')

    def test_rcv_utc_increase_time(self):
        hour_minute = '3:03 UTC+2'
        result = self.cv.time_with_utc(hour_minute)
        self.assertEqual(result, 'cinco horas e três minutos')

    def test_rcv_utc_decrease_time(self):
        hour_minute = '9:43 UTC-5'
        result = self.cv.time_with_utc(hour_minute)
        self.assertEqual(result, 'dezessete minutos para as cinco')

    def test_rcv_utc_that_decrease_more_than_it_should(self):
        hour_minute = '5:43 UTC-5'
        result = self.cv.time_with_utc(hour_minute)
        self.assertEqual(result, 'ERROR')

    def test_rcv_utc_that_increase_more_than_it_should(self):
        hour_minute = '8:43 UTC+5'
        result = self.cv.time_with_utc(hour_minute)
        self.assertEqual(result, 'ERROR')

    def test_third_sprint(self):
        hour_minute = '3:00 UTC-1'
        result = self.cv.time_with_utc(hour_minute)
        self.assertEqual(result, 'duas horas')

        hour_minute = '7:03 UTC+3'
        result = self.cv.time_with_utc(hour_minute)
        self.assertEqual(result, 'dez horas e três minutos')

        hour_minute = '3:53 UTC-2'
        result = self.cv.time_with_utc(hour_minute)
        self.assertEqual(result, 'sete minutos para as duas')


if __name__ == '__main__':
    unittest.main()
