from main import Frames
import unittest

class BasicTest(unittest.TestCase):
    def test_frame_vazio_valido(self):
        frames = Frames()
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

        self.assertTrue('Valor incorreto na jogada.' in str(context.exception))
        
if __name__ == '__main__':
    unittest.main()
