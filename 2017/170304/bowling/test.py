from main import Frames
import unittest

class BasicTest(unittest.TestCase):
    def test_frame_vazio_valido(self):
        frames = Frames()
<<<<<<< HEAD
        self.assertEqual(0,len(frames.jogada([])))

    def test_frame_um_spare_valido(self):
        frames = Frames()
        frame_jogado = [2,3]
        self.assertEqual(2,len(frames.jogada(frame_jogado)))

    def test_frame_pares(self):
        frames = Frames()
        lista1 = [1, 9, 2, 8, 0, 4]
        self.assertTrue(frames.verifica_par(lista1))

    def test_frame_impares(self):
        frames = Frames()
        lista1 = [1, 9, 2, 8, 0]
        self.assertFalse(frames.verifica_par(lista1))

    def test_separar_duplas(self):
        frames = Frames()
        lista1 = [1, 9, 2, 8, 10, 0, 7, 4]
        self.assertEqual([ [1, 9], [2, 8], [10], [0, 7], [4] ], frames.aglutinarJogadas(lista1))

    def test_separar_duplas_com_o_10(self):
        frames = Frames()
        lista1 = [1, 9, 2, 8, 10, 0, 4]
        self.assertEqual([[1,9],[2,8],[10],[0,4]], frames.aglutinarJogadas(lista1))
=======
        self.assertEqual(0, len(frames.jogadas([])))

    def test_frame_com_um_spare_valido_retorna_lista_de_int(self):
        frames = Frames()
        frame_base = [2, 8]

        self.assertEqual(2, frames.jogadas(frame_base)[0])
        self.assertEqual(8, frames.jogadas(frame_base)[1])

    def test_frame_com_um_spare_invalido_retorna_excecao(self):
        frames = Frames()
        frame_base = [2, '@']

        with self.assertRaises(Exception) as context:
            frames.jogadas(frame_base)
>>>>>>> fa8960202b431a39f2cca9923a2458f5dac5d8ca

        self.assertTrue('Valor incorreto na jogada.' in str(context.exception))
        
if __name__ == '__main__':
    unittest.main()



#organizacao das listas
# lista1 = [1, 9, 2, 8, 0, 4]
# lista2 = []
# lista3 = []
# lista2.append(lista1[0])
# lista2.append(lista1[1])
# lista3.append(lista2)
