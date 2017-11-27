#!/usr/bin/env python3
class OutOfLimitException(Exception):
    '''excecao lancada quando limite de 30000 eh excedido'''
    pass

class Brainfuck():
    def __init__(self):
        self.vetor = [0] * 30000
        self.indice = 0
        self.posicao_loop = 0
        self.loop_auxiliar = []
        self.posicao_loop_final = 0
        self.result = ''
        # self.io = BrainFuckIO()

    def executar(self, sentenca, input_usuario=''):
        for index, caractere in enumerate(sentenca):
            if caractere == "+":
                self.incrementa_vetor()
            elif caractere == '-':
                self.decrementa_vetor()
            elif caractere == '<':
                self.incrementa_ponteiro()
            elif caractere == '>':
                self.decrementa_ponteiro()
            elif caractere == '.':
                self.result += chr(self.vetor[self.indice])
            elif caractere == ',':
                self.vetor[self.indice] = ord(input_usuario[0])
                input_usuario = input_usuario[1:]
            elif caractere == '[':
                self.posicao_loop = index
                for index2, caractere_auxiliar in enumerate(sentencia[index:]):
                    if caracterer_auxiliar == ']':
                        self.posicao_loop_final = index2 + index
                        break
                    self.loop_auxiliar.append(caractere_auxiliar)
            elif caractere == ']':

                self.executar(loop_auxiliar)

        return self.result






    def incrementa_vetor(self):
        self.vetor[self.indice] += 1
        if self.vetor[self.indice] == 256:
            self.vetor[self.indice] = 0

    def decrementa_vetor(self):
        self.vetor[self.indice] -= 1
        if self.vetor[self.indice] == -1:
            self.vetor[self.indice] = 255

    def incrementa_ponteiro(self):
        self.indice += 1
        if self.indice > 29999:
            raise OutOfLimitException()

    def decrementa_ponteiro(self):
        self.indice -= 1
        if self.indice < 0:
            raise OutOfLimitException()

# class BrainFuckIO():
#
#
#     def ler_caractere(self, input_usuario):
#         # ch = self.io.ler_caractere()
#         # self.vetor[self.indice] = ord(input_usuario)
#         pass
#
#     def escrever_caractere(self):
#         return(chr(self.vetor[self.indice]))
