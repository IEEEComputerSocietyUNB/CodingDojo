package br.unb.cic.dojo.bowling;

import static org.junit.Assert.assertEquals;

import java.util.List;

import org.junit.Test;
import org.junit.runner.RunWith;
import org.junit.runners.JUnit4;


@RunWith(JUnit4.class)
public class ExampleTest {
	
	private int[] jogadas;
	
	@Test
	public void testeParametros(){
		
		jogadas = new int[]{1, 3, 4, 5, 6, 3, 10};
		
		List<Frame> listaDeJogadas = Processador.processa(jogadas);
		
		assertEquals(listaDeJogadas, listaDeJogadas);
		
		System.out.println(listaDeJogadas);
	}

	@Test
	public void entradaVaziaDeveSerValida() {
		jogadas = new int[0];
		
		assertEquals(0, Processador.processa(jogadas).size());
	}
	
	@Test
	public void processaFrameSimples() {
		jogadas = new int[]{1, 3};
		
		List<Frame> listaDeJogadas = Processador.processa(jogadas);
		Frame f = listaDeJogadas.get(0);
				
		assertEquals(1, f.get(0));
		assertEquals(3, f.get(1));
	}
	
	@Test(expected=IllegalArgumentException.class)
	public void frameInvalidoLancaExcecao() {
		Frame f = new Frame();
		f.push(1);
		f.push(10);
	}
	
	@Test
	public void stringCorreta() {
		jogadas = new int[]{1, 3, 4, 5, 6, 4, 10};
		List<Frame> listaDeJogadas = Processador.processa(jogadas);
		assertEquals("[[1,3], [4,5], [6,/], [X]]", 
				     listaDeJogadas.toString());
	}
	
	@Test
	public void stringAguardandoRolagem(){
		jogadas = new int[]{1, 3, 4, 5, 6};
		List<Frame> listaDeJogadas = Processador.processa(jogadas);
		assertEquals("[[1,3], [4,5], [6,_]]", 
				     listaDeJogadas.toString());
	
	}
	
	@Test
	public void stringZeroPontos(){
		jogadas = new int[]{0, 0, 4, 5, 6};
		List<Frame> listaDeJogadas = Processador.processa(jogadas);
		assertEquals("[[-,-], [4,5], [6,_]]", 
				     listaDeJogadas.toString());
	
	}
	
	@Test
	public void stringZeroSpare(){
		jogadas = new int[]{0, 10};
		List<Frame> listaDeJogadas = Processador.processa(jogadas);
		assertEquals("[[-,/]]", 
				     listaDeJogadas.toString());
	
	}
	
	@Test
	public void jogoVazioPontuacaoZero() {
		jogadas = new int[0];
		List<Frame> listaDeJogadas = Processador.processa(jogadas);
		
		assertEquals(0, Processador.calculaPontuacao(listaDeJogadas));
	}
	
	@Test
    public void pontuacaoSemStrikes() {
		jogadas = new int[]{1, 3};
		List<Frame> listaDeJogadas = Processador.processa(jogadas);
		assertEquals(4, Processador.calculaPontuacao(listaDeJogadas));
	}
	
	@Test
    public void pontuacaoComSpare() {
		jogadas = new int[]{1, 9, 4};
		List<Frame> listaDeJogadas = Processador.processa(jogadas);
		assertEquals(14, Processador.calculaPontuacao(listaDeJogadas));
	}
	
	@Test 
	public void pontuacaoSemJogoCompleto() {
		jogadas = new int[] { 4 };
		List<Frame> listaDeJogadas = Processador.processa(jogadas);
		assertEquals(0, Processador.calculaPontuacao(listaDeJogadas));
	}
}
