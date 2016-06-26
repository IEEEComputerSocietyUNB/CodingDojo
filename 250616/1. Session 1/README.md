Calculadora Romana
================

### 25 - Junho - 2016

#### Breve Introdução:

- Test-Driven Development (TDD) - Funcionamento:
	- Técnica Dev Software - se baseia ciclo de repetições:
	  RED 	 		-> escrever teste que falhe
	  GREEN	 		-> fazer teste passar (de forma simplista!)
	  REFACTOR 		-> refatorar
	- Focar em Babysteps!


- A Linguagem (surpresa) abordada será: C#!
	- Linguagem simples de sintaxe orientada a objetos
	- Baseada em C++
	- IDE Visual Studio com Framework NUnit p/ testes

- Referências:
	- C# Programming Guide
		https://msdn.microsoft.com/en-us/library/67ef8sbd.aspx
	- Unidade de Testes NUnit:
		http://www.nunit.org/
	- TDD Caelum
		http://tdd.caelum.com.br/

===========
### QUESTÃO:

Calculadora Romana, calculando com números romanos!

Estamos em Roma! Dados os números romanos:

```
	I	Corresponde ao numeral 1. II são dois, III são três, IV são 4 (pode ver-se IIII como 4?)
	V	Corresponde ao numeral 5. IV são 4, VI são 6, VII são 7, VIII são 8.
	X	Corresponde ao numeral 10. IX são 9, XI é 11, etc..
	L	Corresponde ao numeral 50. XL é o 40.
	C	Corresponde ao numeral 100. C tem origem na palavra latina Centum.
	D	Corresponde ao numeral 500.
	M   Corresponde ao numeral 1000.
```
Já que não temos decimais ou int aqui, resolveremos operações com Strings.
Existem algumas regras para a utilização dos números romanos:

- Numerais podem ser concatenados para formar um número maior

```
"XX" + "II" = "XXII" ; "XIV" + "LX" = "LXXIV"
```

- Se um numeral menor é posto antes de um maior, significa que é a subtração do maior

```
"IV" significa quatro, "CM" significa novecentos
```

- Se o numeral é I, X ou C você não pode ter mais de três

```
"II" + "II" = "IV"
```

- Se o numeral é V, L ou D não é possível ter mais de um dele, pois:

```
"D" + "D" = "M"
```

Exemplo de operação: 


#### Dicas:

Agrupamento strings e concatenação são chaves para resolver. Lembrando sempre da regra de que os numerais menores podem
preceder maiores.


==========
### RETROSPECTIVA

The Good :smiley::
- Teve introdução linguagem + biblioteca testes em C#
- C# >>>>>>> Java
- Todo mundo codou (que chegou no horário)
- Todo mundo focou
- Exercício Entendível / Bom - melhor que semana passada

The Bad :worried::
- Dúvidas sobre TDD persistem
- Melhorar Babysteps!
