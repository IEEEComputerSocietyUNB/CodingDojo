# Coding Dojo UnB

## Problema: "O tempo em palavras"

[Baseado neste problema do Hackerrank][1].

Dado um horário em número, podemos convertê-lo em palavras, como demonstrado a seguir:

| Números | Palavras                           |
|---------|------------------------------------|
| 5:00    | Cinco horas                        |
| 5:01    | Cinco horas e um minuto            |
| 5:10    | Cinco horas e 10 minutos           |
| 5:15    | Quinze minutos após as cinco       |
| 5:30    | Cinco e meia                       |
| 5:40    | Vinte minutos para as seis         |
| 5:45    | Quinze minutos para as seis        |
| 5:47    | Doze minutos para as seis          |
| 5:28    | Vinte e oito minutos após as cinco |

Escreva uma classe que escreva a hora em palavras no formato mencionado acima.

### Entregas ###

- Primeira Entrega: Tradução literal dos horários, casos testes:
    - 3:00 -> três horas
    - 3:01 -> três horas e um minuto
    - 6:56 -> seis horas e cinquenta e seis minutos
    - 1:15 -> uma hora e quinze minutos
    - 4:30 -> quatro horas e trinta minutos

- Segunda Entrega: Tradução correta dos horários, casos testes (quinze minutos antes, e horários exatos, 00 ou 30) :
    - 3:00 -> três horas em ponto
    - 3:01 -> três horas e um minuto
    - 6:56 -> quatro minutos para sete horas
    - 1:30 -> uma hora e meia
    - 4:45 -> quinze minutos para cinco horas

- Terceira Entrega: Cálculo dos horários recebendo UTC do local:
    - 3:00 UTC-1 -> duas horas em ponto
    - 7:03 UTC+3 -> dez horas e três minutos
    - 3:53 UTC-2 -> sete minutos para duas horas


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
- ???

The Bad :worried::
- ???

### Sessão 2
The good :smiley::
- ???

The Bad :worried::
- ???

[1]: https://www.hackerrank.com/challenges/the-time-in-words
