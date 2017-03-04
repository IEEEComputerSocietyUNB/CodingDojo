class Frames:
    def jogadas(self, play):
        for i in play:
            if not str(i).isdigit():
                raise Exception('Valor incorreto na jogada.')

        return play
