import unittest
import main

class DojoTests(unittest.TestCase):
    def test_a_entrada_eh_valida(self):
        horario = '00:00'
        saida = main.converter(horario)
        self.assertEqual(saida, 'error')

    def test_a_entrada_vale_tres_horas(self):
        horario = '03:00'
        saida = main.converter(horario)
        self.assertEqual(saida, 'três horas')

    def test_a_entrada_vale_tres_horas_e_um_minuto(self):
        horario = '03:01'
        saida = main.converter(horario)
        self.assertEqual(saida, 'três horas e um minuto')

    def test_a_entrada_eh_seis_e_56(self):
        horario = '06:56'
        saida = main.converter(horario)
        self.assertEqual(saida, 'seis horas e cinquenta e seis minutos')

    def test_a_entrada_vale_uma_hora_e_quinze(self):
        horario = '01:15'
        saida = main.converter(horario)
        self.assertEqual(saida, 'uma hora e quinze minutos')

if __name__ == '__main__':
    unittest.main()
