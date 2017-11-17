# Coding Dojo UnB

## Problema: Interpretador de BrainFuck

Brainfuck é uma linguagem de programação cujo funcionamento é muito parecido com uma máquina de Turing. Essa máquina possui como componentes um vetor de 30000 bytes, indexado de 0 a 29999, e um ponteiro, que guarda uma posição desse vetor. Em cada passo, a máquina realiza uma instrução de acordo com o byte armazenado na posição do vetor indicada pelo ponteiro. 
Quando esse byte é igual a zero, a execução é terminada. 

O conjunto de instruções válidas da linguagem é o seguinte:

Instrução | Descrição
------------|-------------
"<" | Incrementa o ponteiro.
">" | Decrementa o ponteiro.
"+" | Incrementa o byte na posição indicada pelo ponteiro.
"–" | Decrementa o byte na posição indicada pelo ponteiro.
"," | Lê um byte e armazena na posição indicada pelo ponteiro. Se não houver nada que possa ser lido (entrada acabou), armazenar zero.
"." | Imprime o valor do byte na posição indicada pelo ponteiro.
"[" | Início do loop: Executa o código delimitado até que o byte na posição indicada pelo ponteiro seja igual a zero.
"]" | Fim do loop: Volta para "[".

#### Informações úteis
- Brainfuck ignora qualquer caractere exceto os 8 acima
- Caso o valor do vetor na posição indicada pelo ponteiro passar de 256, volta a 0
- Caso o valor do vetor na posição indicada pelo ponteiro diminuir de 0, volta a 256
 
#### Casos de erro
- Comandos "[" e "]" não estão em quantidades iguais
- Ponteiro maior que 29999 ou menor que 0

Para visualizar um exemplo de como o brainfuck funciona: [Brainfuck](https://fatiherikli.github.io/brainfuck-visualizer/#KysrKysrKysrK1s+KysrKysrKys+KysrKysrKysrKz4rKysrKysrKysrKz4rKysrKysrKysrPisrKysrKysrKysrKz4rKysrKysrKysrPisrKysrKysrKys+KysrPisrKysrKysrPisrKysrPDw8PDw8PDw8PC1dPisrKysuPi0tLS4+LS0uPisrKysrLj4tLS0tLj4rKysrLj4tLS0uPisrLj4rKysuPi4=)

## Entregas ##

- Primeira entrega: Programa simples que aceite os 6 comandos basicos +-<>,. :

Casos de testes | Output
----------------|-------
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++. | A
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++>++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++>+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++<<.>.>. | ABC
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-. | ZYXWVUTSRQPONMLKJIHGFEDCBA 
,. | "Imprime o caracter digitado"
,>,. | "Descrementa em 1 o numero digitado"
,>,------------------------------------------------[<+>-]<. | "x-y"


- Segunda entrega: Aceitar loops : 

Casos de testes |  Output   
----------------|---------   
++++++[>++++++++++<-]>+++++. |  A   
++++++[>++++++++++>++++++++++>++++++++++<<<-]>+++++.>++++++.>+++++++. | ABC 
++++++[>++++++++++<-]>++++>++++++++++++++++++++++++++[<+.>-] | ABCDEFGHIJKLMNOPQRSTUVWXYZ
++++++++++[>++++++++>++++++++++>+++++++++++>++++++++++>++++++++++++>++++++++++>++++++++++>+++>++++++++>+++++<<<<<<<<<<-]>++++.>---.>--.>+++++.>----.>++++.>---.>++.>+++.>. | Talitha S2
++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++. | Hello Word!
  
- Terceira entrega: Garantir que os demais caracteres sejam ignorados :

Casos de testes | Output
----------------|--------
++++testando++>+++caracteres++<[>++++++ignorados++++<-]>. | A
++++TESTE++>+++DOS++>+++MUITOS++>+++CARACTERES++<<<[>+++++IG+++++>++++NO++++++>+++RA+++++++<<<-]>.DOS>+.>++. | ABC
