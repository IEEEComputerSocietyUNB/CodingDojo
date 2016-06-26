Exemplo Introdução
================

### 25 - Junho - 2016

#### Objetivos:
- Abordagem introdutória à linguagem C# e ao TDD
- Habituação com ferramentas (Visual Studio, NUnit e Testes)

===========

#### Configurando:
- Criar novo Projeto no Visual Studio (ExemploIntrodução)
  Básico Console Application - ignorar classes criadas automaticamente, pois testaremos uma classe

- Criar Classe Simples.cs                 -> classe alvo dos testes
- Criar Classe de testes Simples-Teste.cs -> classe que testará a classe alvo

- Manage NuGet Packages -> Adicionar ao projeto o framework NUnit 2.6.4 (compatível com o Adapter) + NUnitTestAdapter
  * Usaremos o framework NUnit pois é focado em TDD *

- Manter o TestExplorer aberto

===========

#### Implementação:
Em Simples-Teste.cs podemos modificar a classe para que se torne uma classe de testes:

```C#
		[TestFixture]                     // atributo indica que a classe conterá testes
    class Simples_Teste               // classe de testes
    {
        [Test]                        // indica um primeiro teste
        public void PrimeiroTeste()   // primeiro teste
        {
        	Assert.Pass();            // PRIMEIRO PASS - demonstração Ok
        }
    }
```
Rodar o teste em Run All no TestExplorer -> passou! Mas isto ainda não é um caso de TDD! Este foi só exemplo do NUnit em ação...

- Simples-Teste.cs podemos adicionar um novo teste mais complexo:

```C#
    [Test]
    public void Quando1_Retorna1() // input 1 inteiro, output deve devolver a string "1"
    {
        int input = 1;

        string output = Simples.GetValor(input);
    }
```
GetValor ainda não exite! Em Show Potencial Fixes - automaticamente criamos o Método GetValor no Simples.cs
Rodar testes novamente -> vai Falhar! Pois na criação automática o método lança a exeção de não implementado

- Corrigindo então eem Simples.cs:


```C#
  	public static string GetValor(int input)
    {
        return string.Empty; // retornar uma string vazia p/ entregar uma string ao output
    }
```

Deu certo agora, pois a output já recebe algo. Mas, de novo, ainda não é TDD! Para o TDD devemos utilizar um Assert!
Agora sim, vamos começar o TDD.

1. Em Simples-Teste.cs devemos escrever teste que falhe (RED):

```C#
	public void Quando1_Retorna1()
	{
    	int input = 1;

	    string output = Simples.GetValor(input);

        Assert.AreEqual("1", output); // o Assert compara a igualdade entre "1" e output
	}
```
FALHOU! Acredite ou não então estamos no caminho certo!


2. Hora de reescrever esse teste para passar (GREEN) - Em Simples.cs então devemos fazer do jeito mais simples possível!

```C#
    public static string GetValor(int input)
    {
        return "1"; // é o requisito mínimo
    }
```
- PASSOU! Beleza!


3. Último Sinal do ciclo TDD. Agora sim poderemos refatorar para algo mais digno:

```C#
	public static string GetValor(int input)
    {
        string output = string.Empty;

        if(input == 1)
        {
            output = "1";
        }
	return output;
	}
```
Ou então, dando um passo maior:

```C#
public static string GetValor(int input)
{
    return input.ToString();
}
```

===========
#### FIM!
