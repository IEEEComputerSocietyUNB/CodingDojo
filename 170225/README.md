Por [Rômulo César](mailto:instrutor.romulo@gmail.com)

Dojo  – Receita e Numerais Romanos
==================================

Uma mulher nutricionista chamada Maria é responsável por modificar valores constantemente no sistema de um restaurante. É necessário que a partir dessas informações o sistema calcule o valor total da receita seguindo as regras estipuladas pelo restaurante e essa é a primeira sessão do Dojo. A segunda sessão é o problema dos numerais romanos. No contexto do problema você tem um sistema que gera lista de receitas baseadas em um livro ordenadas por números romanos. No cenário da segunda sessão você deve entrar com um número romano e o sistema realizar a conversão para inteiro.

Usaremos o framework de C# usado no [dojo do dia 25 de Junho de 2016](https://github.com/ComputerSocietyUNB/TDD/blob/master/160625/0.%20Introduction%20C%23%20testing/README.md).

Sessão 1 – O problema da Maria
------------------------------

As informações que devem ser inseridas pela Maria são as seguintes.

| Receita        |                |
| :------------- | :------------- |
| Nome           | Item Two       |
| -------------- | -------------- |
| Valor          | Item Two       |
| -------------- | --------------------------- |
| Tipo           | Enumeração (PRATOPRINCIPAL, GUARNICAO, SUCOS)      |


Primeiramente é necessário calcular o valor total da receita.
Regras para o  primeiro problema:

- Se a receita for do tipo Prato Principal deverá ter um desconto de 20% caso a receita seja maior ou igual a R$ 10,00 caso contrário o desconto é de 10%.
- Guarnição e suco terá o desconto de 5% se o valor da receita for maior ou igual R$ 3,00 e 1% em caso contrário.

### Testes ###

Valor Receita Maior ou Igual a R$ 10.00 – Prato Principal:
- Valor: R$ 11.00
- Entrada: 8.8
- Saida: true

Valor menor que  R$ 10.00 – Prato Principal:
- Valor: R$ 9.00
- Entrada: 8.1
- Saida: true

Prato Guarnição e Suco maior ou igual a R$ 3,00:
- Valor: R$ 4.00
- Entrada: 3.8
- Retorno: true

Prato Guarnição e Suco inferior a R$ 3,00:
- Valor: R$ 2.00
- Entrada: 1.98
- Retorno: true

Sessão 2 – O Problema dos Números Romanos
-----------------------------------------

Dado um número romano converta-o para o inteiro correspondente:

```
I, unus, 1 (um)
V, quinque,5, (cinco)
X, decem, 10 (dez)
L, quinquaginta, 50 (cinquenta)
C, centum, 100 (cem)
D, quingenti, 500 (quinhentos)
M, mile, 1.000 (mil)
```

Regras:
Algarismos de menor ou igual valor à direita são somados ao algarismo de maior valor.
Algarismos de menor valor à esquerda são subtraídos do algarismo de maior valor.
Nenhum símbolo pode ser repetido lado a lado por mais de 3 vezes. Ex: O número 4 é `IV` e não `IIII`.

Exemplo:
`XV` representa 15 `(10+5)` e o número `XXVIII` representa 28 `(10+10+5+1+1+1)`. Pode existir outras regras, mas basicamente o desafio é transformar o algarismo romano no inteiro correspondente.

### Testes ###

Entender o Simbolo I:
- Valor: I
- Entrada: 1
- Saida: true

Entender Símbolo V:
- Valor: V
- Entrada: 5
- Saida: true

Entender Dois Símbolos:
- Valor: II
- Entrada: 2
- Saida: true

Entender Quatro Símbolos Dois a Dois:
- Valor: XXII
- Entrada: 22
- Saida: true

Entender o Símbolo IV:
- Valor: IV
- Entrada: 4
- Saida: true

Vai Entender Complexo XXIV:
- Valor: XXIV
- Entrada:24
- Saída:true
