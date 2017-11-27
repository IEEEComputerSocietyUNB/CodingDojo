#!/usr/bin/env python3
import unittest
import inspect
import sys
from main import Brainfuck, OutOfLimitException

class TestDojo(unittest.TestCase):
    def setUp(self):
        self.brain = Brainfuck()

    def teste_brainfuck(self):
        '''testa se está definida a classe Brainfuck'''
        self.assertEqual(inspect.isclass(Brainfuck), True)

    def test_existe_vetor(self):
        ''' Existe vetor de inteiros BrainFuck'''
        self.assertTrue(hasattr(self.brain, "vetor"))

    def test_vetor_tem_tamanho_30000(self):
        self.assertEqual(30000, len(self.brain.vetor))

    def test_elementos_do_vetor_inicialmente_tem_valor_0(self):
        self.assertTrue(x == 0 for x in self.brain.vetor)

    def teste_indice_tem_valor_0(self):
        ''' Existe indice BrainFuck e ele é iniciado com 0'''
        self.assertTrue(hasattr(self.brain, "indice"))
        self.assertEqual(0, self.brain.indice)

    def test_incrementa_pos_um(self):
        ''' testa o incremento uma vez'''
        sentenca = '+'
        self.brain.executar(sentenca)
        self.assertEqual(1, self.brain.vetor[self.brain.indice])

    def test_incremetar_acima_do_limite_255(self):
        '''Incrementa mais do que 255 vezes'''
        sentenca = 256*"+"
        self.brain.executar(sentenca)
        self.assertEqual(0, self.brain.vetor[self.brain.indice])

    def test_decrementar_um(self):
        sentenca = '++-'
        self.brain.executar(sentenca)
        self.assertEqual(1, self.brain.vetor[self.brain.indice])

    def test_decrementar_0(self):
        '''decrementa quando e 0'''
        sentenca = '-'
        self.brain.executar(sentenca)
        self.assertEqual(255, self.brain.vetor[self.brain.indice])

    def test_incrementa_ponteiro(self):
        '''Verifica se o ponteiro eh incrementado de 1 em 1'''
        sentenca = '<'
        self.brain.executar(sentenca)
        self.assertEqual(1, self.brain.indice)

    def test_incrementar_ponteiro_acima_do_limite_30000(self):
        '''Verifica se para o programa ao tentar incrementar o
        ponteiro acima do limite superior'''
        sentenca = '<' * 30000
        with self.assertRaises(OutOfLimitException):
            self.brain.executar(sentenca)

    def test_decrementa_ponteiro(self):
        '''Verifica se o ponteiro eh decrementado de 1 em 1'''
        sentenca = '<<>'
        self.brain.executar(sentenca)
        self.assertEqual(1, self.brain.indice)

    def test_decrementar_ponteiro_abaixo_de_zero(self):
        '''Verificar se para o programa ao tentar decrementar o ponteiro abaixo
        limite inferior'''
        sentenca = '>'
        with self.assertRaises(OutOfLimitException):
            self.brain.executar(sentenca)

    def test_mostrar_char_na_tela(self):
        ''' Verifica a impressão de caractere'''
        sentenca = 65*"+" + "."
        caracter = self.brain.executar(sentenca)
        self.assertEqual("A", caracter)

    def test_inicia_e_termina_loop(self):
        ''' Verifica se loop inicia e termina'''
        sentenca = '+[+].'
        caracter = self.brain.executar(sentenca)
        self.assertEqual(caracter, 0)



    def test_aceitar_input_testar_funcao_virgula(self):
        sentenca = ',.'
        input_usuario = 'x'
        caracter = self.brain.executar(sentenca, input_usuario)
        self.assertEqual('x', caracter)

if __name__ == "__main__":
    unittest.main()
