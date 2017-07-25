# Dojo UnB

+ Coding Dojo UnB praticado dia 9/7/2016.
+ Neste Dojo, vamos usar a linguage Clojure, a plataforma Leiningen.
+ Estes exercícíos foram tirados do livro "Structure and Implementation of Computer Programs" por Harold Abelson e Julie Sussman.

Setup
-----

Após baixar e instalar o Clojure e o Leiningen, pode-se criar um projeto como este com o comando:

```
lein new app <nome do processo>
```

Retrospectiva
-------------

### Problema 1 ###

O que foi bom:

+ Todos tiveram foco
+ Linguagem foi massa e funcional
+ Uso do Git
+ Sem interface gráfica `no noobs here`
+ Todos que puderam, codaram
+ Não repetiu gente
+ Melhoramos com o TDD
+ Pessoas novas `:)` `deem continuidade pleeeaase`

O que foi ruim:

+ Nem todos codaram porque faltou tempo
+ Plateia deveria se policiar mais (embora seja algo bom)
+ Problema poderia ter sido mais amigável com o TDD
+ Não conseguimos terminar o problema em uma sessão

### Problema 1, parte 2: a Vingança ###

O que foi bom:

+ Terminamos a `#####` do exercício.
+ Ficamos mais familiarizados com o LISP.
+ Todo mundo codou.
+ Foi massa

```
IRADO
```

O que foi ruim:

+ Não fizemos o exercício 2.
+ Algumas pessoas saíram e não deram continuidade.
+ Perdemos muito tempo no final com base matemática.
+ Fizemos passos muito grandes para testar.
+ Não fizemos alguns commits necessários.
+ Corrigimos um bug que não foi provado.


Problema 1: Algoritmo de Newton para raíz quadrada
--------------------------------------------------

Como podemos calcular raízes quadradas? O jeito mais comum é usar o método das aproximações sucessivas de Newton, que diz que, sempre que tivermos uma estimativa G para o valor da raiz quadrada do número X, podemos realizar uma manipulação simples para obter uma nova estimativa (mais próxima da verdadeira raiz quadrada) tirando a média entre G e X/G. Por exemplo, podemos computar a raíz quadrada de 2 como segue. Supondo que a nossa estimativa inicial é 1:

Estimativa | Quociente           | Média
-----------|---------------------|--------------------------------
1.0        | 2 / 1 = 2           | (2 + 1) / 2 = 1.5
1.5        | 2 / 1.5 = 1.333     | (1.333 + 1.5) / 2 = 1.4167
1.4167     | 2 / 1.4167 = 1.4118 | (1.4167 + 1.4118) / 2 = 1.4142
1.4142     | ...                 | ...

Continuando este processo, podemos obter aproximações cada vez melhores da raiz quadrada. Vamos agora formalizar este processo em termos de procedimentos. Começaremos com um valor para o radicando (o número cuja raíz quadrada estamos tentando computar) e um valor para a estimativa. Se a estimativa for boa o suficiente para os nossos propósitos, terminamos o algoritmo. Caso contrário, devemos repetir o processo com uma estimativa melhorada.

Simplificação: Considere que a raíz quadrada de um número negativo é -1.

Bônus: Para a raíz cúbica, pode-se usar como melhor aproximação o valor (X/(G^2)+2*G)/3.

Problema 2: Exponenciação de um número inteiro
----------------------------------------------

Considere o problema de computar a exponencial de um determinado número. Gostaríamos de um procedimento que tome como argumentos a base B e um número inteiro positivo N; e compute B^N. Um jeito de resolver isto é pela definição recursiva:

```
B^N := B * B^(N-1)
B^0 := 1
```

Tarefa: Implemente este algoritmo.
Bônus: Há uma implementação mais rápida deste algoritmo, que usa do fato de que:

```
N é par => B^N = (B^(N/2))^2
```
