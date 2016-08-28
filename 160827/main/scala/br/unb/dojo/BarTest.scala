package br.unb.dojo

import org.junit.Test
import org.junit.Assert._

class BarTest {
  
  @Test
  def listaVaziaRetornaZero() {
    assertEquals(0, Bar.sizeof(""))
  }
  
  @Test
  def listaComUmElementoRetornaUm() {
    assertEquals(1, Bar.sizeof("a"))
  }
  
  @Test
  def listaComUmElementoeEspacoRetornaUm() {
    assertEquals(1, Bar.sizeof("a "))
  }
  
  @Test
  def listaSoComEspacoRetornaZero() {
    assertEquals(0, Bar.sizeof("   "))
  }
  
  @Test
  def listaSoComCaracteresInvalidosRetornaZero() {
    assertEquals(0, Bar.sizeof(" \\|/2~3`@"))
  }
  
  @Test
  def listaSoComCaracteresValidos(){
    assertEquals(4, Bar.sizeof("ACgT"))
  }
  
  @Test
  def listaQuantidadeDeA(){
    assertEquals(3, Bar.countletters('a', "acGA3 a"))
  }
  
  @Test
  def listaQuantidadeDeLetrasTotal(){
    
    assertEquals(Bar.countAllLetters("aA cC gG tT"), Map('a' -> 2, 'c' -> 2, 'g' -> 2, 't' -> 2))
  }
}