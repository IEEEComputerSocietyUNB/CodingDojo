package br.unb.dojo

import org.junit.Test
import org.junit.Assert._

class HelloTest {
  
  @Test
  def foo() {
     assertEquals(new Hello().toString,"Hello world")
  }
}