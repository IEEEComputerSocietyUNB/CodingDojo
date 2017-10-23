# Python Guide

## Introdução básica da linguagem Python 3:

### Variáveis

``` python
any_var = 3 # números
any_var = 'something' # strings
```

### Manipulação de strings

``` python
string_input = input('Enter some string')
print('Pair programming is %s', % ('awesome'))
'{1} is {0}'.format('awesome!', 'Dojo')
'Coding ' + 'Dojo'
len('ODD')
```

### Estruturas de dados

- Listas

``` python
list = [0, 3] # define lista

list + other_list # concatena

list.append(3) # adiciona valor no final da lista
list.insert(1,3) # adiciona valor 3 no índice 1 da lista
list.remove(3) # retira o item com valor 3 da lista
list.pop() # retira o último item da lista

3 in list # confere se o valor 3 existe na lista
list.index(3) # coleta o índice do primeiro valor encontrado           
              # na lista ou lança excessão
list[1] # Procura o valor no índice 0 da lista
list[-1] # Procura o valor no último índice da lista
list[1:] # Omite o primeiro valor da lista
```

- Dicionários

``` python
dict = {'one' : 2, 'two': 1, 'four': 5} # define um dicionário

dict['one'] # Procura o valor da chave 'one'
dict.keys() # coleta todas as chaves do dicionário
dict.values() # coleta todas as valores da chaves do dicionário
dict.items() # coleta o dicionário em formato de lista de tuplas dos valores
```

- Tuplas

``` python
tuple = (1, 3) # Define a tupla
a, b, c = (1, 2, 3) # Coleta valores da tupla em variáveis separadas

tuple + other_tuple # concatena tuplas

3 in tuple # confere se o valor 3 existe na tupla

tuple[1] # Procura o valor no índice 1 da tupla
list[2:] # Omite até o segundo valor da tupla (retorna uma tupla)
```

### Funções/métodos

``` python
def bestFunctionEver(var, var2): # Declara função com 2 parâmetros
  return var + var2 # Retorno da função

bestFunctionEver(3, 4) # Chama função com 2 parâmetros

# declara função anônima
func = lambda name: 'Some anonymous function called ' + name
func('anonymous') # chama função anônima
```

### Classes

``` python
class WorseClassEver: # Declara classe
  def __init__(self): # Método base de setup da classe
    return False # Retorno do método base de setup da classe
```

### Controle de Fluxo

- If's

``` python
if var > 2: # if padrão
  print('hmmm')
elif var < 2:
  print('yes')
else:
  print('ue')

'yeih!' if 3 > 2 else 'aff' # condicional ternário
```

- For

``` python
for number in [1, 2, 3]: # for sobre listas
  print(number)

for key, value in some_dict.items(): # for sobre dicionários
  print(key, value)

for i in range(4): # itera de 0 a 3
  print(i)

for i in range(2, 4): # itera de 2 a 3
  print(i)    

[i for i in range(2, 4) if i < 3] # List comprehensions: Retorna 2
```

- While

``` python
dojo = 0
while dojo < 10:
  print('dojo is awesome')
  dojo += 1
```

- Exceções

``` python
try:
  var = list_not_declare[1]
  raise IndexError('Another index erro') # Levanta erro de acesso de índice
except IndexError as error:
  pass # Se encontrar este erro faça alguma ação para recuperar o fluxo
except (TypeError, NameError):
  pass # Exceções múltiplas
else:
  print('Good!') # Se não lançar nenhuma exceção
finally:
  print('All clean') # Executa sob qualquer circunstância
```

## Introdução básica do framework de teste `unittest`:

Extende-se do unittest.TestCase:

``` python
import unittest

Class TestFrame(unittest.TestCase):
```

### Assertivas

``` python
self.assertEqual('DOJO', dojo.upper())
self.assertNotEqual('Dojo', dojo.upper())
self.assertTrue(1 < 2)
self.assertFalse(1 > 2)
```

### Executar

``` sh
python3 -m unittest test.py
```

Se o código abaixo estiver presente no arquivo teste, executar normalmente como código python.

``` python
if __name__ == '__main__':
    unittest.main()
```
