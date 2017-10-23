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
        self.assertEqual(saida, 'quatro minutos para as sete')

    def test_a_entrada_vale_uma_hora_e_quinze(self):
        horario = '01:15'
        saida = main.converter(horario)
        self.assertEqual(saida, 'uma hora e quinze minutos')

    def test_quatro_horas_e_trinta(self):
        horario = '04:30'
        saida = main.converter(horario)
        self.assertEqual(saida, 'quatro e meia')

    def test_a_entrada_vale_um(self):
        horario = 1
        saida = main.numeroliteral(horario)
        self.assertEqual(saida, 'um')

    def test_a_entrada_vale_uma_e_meia(self):
        horario = '01:30'
        saida = main.converter(horario)
        self.assertEqual(saida, 'uma e meia')

    def test_a_entrada_vale_vinte_para_as_cinco(self):
        horario = '04:40'
        saida = main.converter(horario)
        self.assertEqual(saida, 'vinte minutos para as cinco')

    def test_a_entrada_3_horas_utc_menos_1(self):
        horario = '03:00 UTC-1'
        saida = main.converter(horario)
        self.assertEqual(saida, 'duas horas')

if __name__ == '__main__':
    unittest.main()
