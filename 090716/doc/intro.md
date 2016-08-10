# Pacote Mínimo para Clojure

Para rodar este projeto em Clojure, os softwares necessários foram:

- [Clojure](http://clojure.org)
- [Leiningen](http://leiningen.org)
- [Lighttable](http://lighttable.com)

Introdução à linguagem Clojure
------------------------------

Os exercícios requerem conhecimentos específicos da linguagem. Mais precisamente, precisamos saber declarar uma função e fazer uma estrutura condicional. Para declarar uma função, segue-se a sintaxe a seguir:
``` Clojure
(defn nome-da-funcao
    "Documentacao da funcao"
    [argumento1 argumento2]
    "corpo da funcao")
```
Chamamos esta função assim:
``` Clojure
(nome-da-funcao argumento1 argumento2)
```

Uma estrutura condicional pode ser construída em Clojure usando a função `if`:
``` Clojure
;; Comentario
(if condicao
    entao
    senao)
```
Note que esta estrutura é uma função, isto é, ela tem um retorno. Caso a condição seja verdadeira, esta função retorna a expressão contida em `entao`. Caso contrário, retorna a expressão contida em `senao`.

Introdução ao Leiningen
-----------------------

Leiningen é um sistema para escrever projetos em Clojure. Para criar um novo projeto rápido, usamos o comando

``` sh
lein new app nomeDoProjeto
```

Isto criará uma estrutura mínima para um projeto. Notavelmente, temos o arquivo `project.clj` (que contém as configurações do projeto), a pasta `src` (que contém o código do projeto) e a pasta `test` (que contém os arquivos de teste a serem escritos pelo programador). No arquivo principal do projeto (geralmente chamado de `core.clj`), temos a função `-main`, que será chamada quando executarmos o projeto usando o comando
``` sh
lein run
```
Para executar os testes presentes no arquivo de testes, usamos o comando
``` sh
lein test
```
Para adicionar um teste a este arquivo, usamos a função `deftest`:

``` Clojure
(deftest nome-do-teste
    (testing "Comentario do teste"
        "corpo do teste"))
```
