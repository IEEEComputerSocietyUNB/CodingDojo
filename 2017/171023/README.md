# Coding Dojo UnB

## Problema: "O tempo em palavras"

[Baseado neste problema do Hackerrank][1].

Dado um horário em número, podemos convertê-lo em palavras, como demonstrado a seguir:

| Números | Palavras                           |
|---------|------------------------------------|
| 5:00    | Cinco horas                        |
| 5:01    | Cinco horas e um minuto            |
| 5:10    | Cinco horas e dez minutos          |
| 5:15    | Cinco horas e quinze minutos       |
| 5:30    | Cinco e meia                       |
| 5:40    | Vinte minutos para as seis         |
| 5:45    | Quinze minutos para as seis        |
| 5:47    | Treze minutos para as seis         |
| 5:28    | Cinco horas e vinte e oito minutos |

Escreva uma classe que escreva a hora em palavras no formato mencionado acima.

### Entregas ###

- Primeira Entrega: Tradução literal dos horários, casos testes:
    - 3:00 -> três horas
    - 3:01 -> três horas e um minuto
    - 6:56 -> seis horas e cinquenta e seis minutos
    - 1:15 -> uma hora e quinze minutos
    - 4:30 -> quatro horas e trinta minutos

- Segunda Entrega: Tradução correta dos horários, casos testes (vinte minutos antes e caso de x:30) :
    - 3:00 -> três horas
    - 3:01 -> três horas e um minuto
    - 6:56 -> quatro minutos para as sete
    - 1:30 -> uma e meia
    - 4:40 -> vinte minutos para as cinco

- Terceira Entrega: Cálculo dos horários recebendo UTC do local:
    - 3:00 UTC-1 -> duas horas
    - 7:03 UTC+3 -> dez horas e três minutos
    - 3:53 UTC-2 -> sete minutos para as duas


## Sobre o Python

### Ambiente virtual ###

```bash
$ source venv/bin/activate
```

### Como executar ###

```bash
$ cd dojo
$ python tests.py
```

## Retrospectiva

### Sessão 1

The good :smiley::
- O problema foi adequado.
- Teve Coffee Break (cortesia da SENE).
- Linguagem diferente é legal.
- Python foi legal.
- A experiência com mó galera codando geral em um ambiente que nao eh sala de aula..
- Pair programming + TDD interessantíssimo.

The Bad :worried::
- SOCORRO `KeyError`
- Nem todos codaram.

Sugestao:
- Guia para os erros ficou faltando.

### Sessão 2
The good :smiley::
- ???

The Bad :worried::
- ???

[1]: https://www.hackerrank.com/challenges/the-time-in-words
