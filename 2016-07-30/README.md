Dojo UnB - 30/07/2016

== Boliche

Um grande empresário brasileiro, aproveitando o clima das olimpíadas, resolveu investir em um esporte bastante praticado pelos turistas americanos, o boliche.
Investiu pesado na loja, preparou as pistas, calçados, bolas, fez uma grande campanha de marketing... Mas resolveu cortar os gastos no programa que conta a pontuação dos jogadores contratando seu sobrinho.
Como todos sabem, o único resultado possível era um software capenga que calculava tudo errado.

Agora, a apenas quatro horas da grande inauguração de sua loja, com diversos turistas na fila e todas as pistas reservadas pelo resto da noite, ele percebeu o problema e contactou o dojo de programação da UnB, 
reconhecido mundialmente pela sua alta capacidade de raciocínio, robustes dos testes e alta qualidade do software para refazer completamente o sistema.

Para garantir que haveria pelo menos alguma coisa funcionando para a inauguração, ele enviou as regras de pontuação e 3 entregas por ordem de prioridade:

==== Regras do Boliche

Cada jogo (line) de boliche possui 10 turnos (frames) por jogador.

A cada frame, o jogador tem até 2 rolagens para derrubar os 10 pinos

Caso o jogador não derrube todos os pinos nas duas rolagens, a pontuação é igual ao número de pinos derrubados. Ex:
[1, 3] -> 4 pontos

Caso o jogador derrube todos os pinos na segunda rolagem (spare), a pontuação é igual a 10 mais o número de pinos derrubados na próxima rolagem. Ex:
[6, 4], [1, 6] -> 18 pontos (11 da primeira jogada, mais 7 da segunda)

Caso o jogador derrube todos os pinos na primeira rolagem (strike), a pontuação é igual a 10 mais o número de pinos derrubados nas próximas duas rolagens. Ex:
[10], [8, 1]       -> 28 pontos (19 da primeira jogada, mais 9 da segunda)
[10], [10], [8, 1] -> 56 pontos (28 da primeira jogada, 19 da segunda e 9 da terceira)

No décimo turno, caso o jogador faça um strike ou um spare, ele deverá rolar 3 vezes no turno para definir o valor final do strike/spare. Ex:
[10, 10, 10] -> 30 pontos (conta-se os pontos da primeira rolagem apenas)
[9, 1, 10] -> 20 pontos

==== Primeira entrega

É preciso que o software seja capaz de transformar um array de rolagens (int) em um array de frames. Ex:

[1, 9, 2, 8, 10, 0, 7, 4] -> [ [1, 9], [2, 8], [10], [0, 7], [4, ] ]

Caso o array esteja errado, deve ser lançada uma exceção. Ex:

[2, 9, ...] -> WhateverYouWantException

É preciso, após criado o array de jogadas, que haja um método retornando uma representação em String, para ser impressa na tela:

[ [1, 9], [2, 8], [10], [0, 7], [4, ] ] -> [1, /], [2, /], [X], [-, 7], [4, _]

OBS: Não é preciso se preocupar com a 10ª jogada

==== Segunda Entrega

É preciso que o software mostre a pontuação do jogador. 
Importante, caso os pontos de uma jogada ainda estejam em aberto, não devem ser computados

[1, /], [2, /] -> 12 pontos (O último spare ainda está em aberto)
[1, /], [2, 7] -> 21 pontos
[1, _]         -> 0  pontos

OBS: Não é preciso se preocupar com a 10ª jogada

<Intervalo>


==== Terceira Entrega

Agora finalmente entra o conceito de jogador. Em uma pista de boliche, são aceitos até 6 jogadores. 
O programa deve receber o nome de todos os jogadores, e aplicar o array de jogadas como se um tivesse jogado após o outro:

$ Bob
$ Ana
$ {1, 9, 4, 6, 3}

Bob [1, 9], [3, _] -> 13 pontos
Ana [4, 6],        -> 0  pontos


E deve aceitar inputs de jogadas após o carregamento inicial:


Bob [1, 9], [3, _] -> 13 pontos
Ana [4, 6],        -> 0  pontos

$ próxima rolagem:
$ 4

Bob [1, 9], [3, 4] -> 20 pontos
Ana [4, 6], [_, _] -> 0  pontos

Agora que existe o conceito de jogador, é preciso se preocupar com a 10ª jogada.

==== Entrega bônus

Após o jogo acabar, Ele deve exibir o placar final:

Ana  [X], [X], [X], [X], [X], [X], [X], [X], [X], [X, X, 9] -> 299 pontos WINNER
Cleo [X], [X], [X], [X], [X], [X], [X], [X], [X], [X, X, 8] -> 298 pontos
Bob  [X], [X], [X], [X], [X], [X], [X], [X], [X], [X, X, 7] -> 297 pontos LOSER

Caso alguém tenha a pontuação máxima (300), deve exibir PERFECT no lugar de WINNER

Ana  [X], [X], [X], [X], [X], [X], [X], [X], [X], [X, X, X] -> 300 pontos PERFECT








