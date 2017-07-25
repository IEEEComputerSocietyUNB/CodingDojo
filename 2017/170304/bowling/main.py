class Frames:
    def jogada(self, play):
        return play

    def verifica_par(self, play):
        qtd = len(play)
        resto_divisao = qtd % 2
        if resto_divisao == 0:
            return True
        else:
            return False

    def aglutinarJogadas(self, lista1):
        resultado = []
        parcial = []
        for percorre in lista1:
            if percorre == 10:
                resultado.append([percorre])
            else:
                parcial.append(percorre)
                if len(parcial) is 2:
                    resultado.append(parcial)
                    parcial = []
        if len(parcial) > 0:
            resultado.append(parcial)
        return resultado
