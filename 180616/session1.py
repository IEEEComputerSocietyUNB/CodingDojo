'''
Um homem chamado José é o responsável por ligar e desligar as luzes de um corredor.
Cada lâmpada tem seu próprio interruptor que liga e a desliga. Inicialmente todas as lâmpadas estão desligadas.
José faz uma coisa peculiar: se existem n lâmpadas no corredor, ele caminha até o fim do corredor e volta n vezes.
Na iésima caminhada, ele aperta apenas os interruptores aos quais sua posição é divisível por i.
Ele não aperta nenhum interruptor na volta à sua posição inicial, apenas na ida.
A iésima caminhada é definida como ir ao fim do corredor e voltar.

Determine qual é o estado final de cada lâmpada. Está ligada ou desligada?

Casos de Teste:

Entrada: -3
Saída: []

Entrada: 0
Saída: []

Entrada: 1
Saída: [on]

Entrada: 3
Saída: [true, false, false]

Entrada: 8
Saída: [true, false, false, true, false, false, false, false]

Entrada: 12
Saída: [
  	 true, false, false, true, false, false, false, false, true, false,false, false]

Entrada: 16
Saída: [
  	 true, false, false, true, false, false, false, false, true, false, false, false, false, false, false, true];

'''

import unittest
import math

class TestCase(unittest.TestCase):
    def testNeg(self):
        lam = Lampadas(-3)
        self.assertFalse(lam.result)

    def testZero(self):
        lam = Lampadas(0)
        self.assertFalse(lam.result)

    def testUm(self):
        lam = Lampadas(1)
        self.assertEquals(lam.result, [True])

    def testDois(self):
        lam = Lampadas(2)
        self.assertEquals(lam.result, [True, False])

    def testTres(self):
        lam = Lampadas(3)
        self.assertEquals(lam.result, [True, False, False])

    def testQuatro(self):
        lam = Lampadas(4)
        self.assertEquals(lam.result, [True, False, False, True])


class Lampadas:
    def __init__(self, n):
        if n <= 0:
            self.result = []
        else:
            self.result = [False] * n;
            for i in range(1, int(math.sqrt(n))+1):
                if (i*i <= n):
                    self.result[(i*i)-1] = True



if __name__ == '__main__':
    unittest.main()
