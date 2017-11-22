import unittest
from main import Brainfuck

class BrainfuckTests(unittest.TestCase):
  
  def setUp(self):
        self.bf = Brainfuck()
    
  def test_output_cell(self):
    program = '.'
    leitura = ''
    result = self.bf.brainfuck_program(program,leitura)
    self.assertEqual(ord(result),0)
  
  def test_ret_inc_cell(self):
    program = '+'
    leitura = ''
    result = self.bf.brainfuck_program(program,leitura)
    self.assertEqual(result,'')
  
  def test_ret_dec_cell(self):
    program = '-'
    leitura = ''
    result = self.bf.brainfuck_program(program,leitura)
    self.assertEqual(result,'')
  
  def test_ret_inc_pont(self):
    program = '>'
    leitura = ''
    result = self.bf.brainfuck_program(program,leitura)
    self.assertEqual(result,'')
  
  def test_ret_dec_pont(self):
    program = '<'
    leitura = ''
    result = self.bf.brainfuck_program(program,leitura)
    self.assertEqual(result,'Erro limite')
    
  def test_ret_input(self):
    program = ','
    leitura = 'a'
    result = self.bf.brainfuck_program(program,leitura)
    self.assertEqual(result,'')
  
  def test_ret_inc_uni_cell(self):
    program = '+.'
    leitura = ''
    result = self.bf.brainfuck_program(program,leitura)
    self.assertEqual(ord(result),1)
  
  def test_ret_dec_uni_cell(self):
    program = '-.'
    leitura = ''
    result = self.bf.brainfuck_program(program,leitura)
    self.assertEqual(ord(result),255)
  
  def test_ret_inc_uni_pont(self):
    program = '>.'
    leitura = ''
    result = self.bf.brainfuck_program(program,leitura)
    self.assertEqual(ord(result),0)
  
  def test_ret_dec_uni_pont(self):
    program = '<.'
    leitura = ''
    result = self.bf.brainfuck_program(program,leitura)
    self.assertEqual(result,'Erro limite')
    
  def test_ret_uni_input(self):
    program = ',.'
    leitura = 'a'
    result = self.bf.brainfuck_program(program,leitura)
    self.assertEqual(result,'a')
  
  def test_ret_char_dif(self):
    program = '/sdçkasdfçs.'
    leitura = ''
    result = self.bf.brainfuck_program(program,leitura)
    self.assertEqual(ord(result),0)
    
  def test_incrementa_cell(self):
    program = '+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.'
    leitura = ''
    result = self.bf.brainfuck_program(program,leitura)
    self.assertEqual(result,'A')
  
  def test_decrementa_cell(self):
    program = '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.'
    leitura = ''
    result = self.bf.brainfuck_program(program,leitura)
    self.assertEqual(result,'ZYXWVUTSRQPONMLKJIHGFEDCBA')
    
  def test_incrementa_pont(self):
    program = '+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.>++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.'
    leitura = ''
    result = self.bf.brainfuck_program(program,leitura)
    self.assertEqual(result,'AB')
  
  def test_decrementa_pont(self):
    program = '+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++>++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++>+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++<<.>.>.'
    leitura = ''
    result = self.bf.brainfuck_program(program,leitura)
    self.assertEqual(result,'ABC')
    
  def test_input_cell(self):
    program = ',-.'
    leitura = '9'
    result = self.bf.brainfuck_program(program,leitura)
    self.assertEqual(result,'8')
  
  def test_char_diferente(self):
    program = '+++++Testando+++++++++++++++Outros+++++++++++++++++++++++++++++++++++++Caracteres++++++++++++++++++++++++e+++++++++.-.-.-.-.-deixando.-.-.-.-.-.-a.-.-.-.-cadeia.-.-.-.-.-.-.-enorme.-.-.-.'
    leitura = ''
    result = self.bf.brainfuck_program(program,leitura)
    self.assertEqual(result,'ZYXWVUTSRQPONMLKJIHGFEDCBA')
    
  def test_cont_colchete_errado(self):
    program = '+[>,]<-[+.<-]]'
    result = self.bf.cont_colchete(program)
    self.assertEqual(result, 'Malformed expression')
    
  def test_loop_simples(self):
    program = '++++++++++[>++++++++>++++++++++>+++++++++++>++++++++++>++++++++++++>++++++++++>++++++++++>+++>++++++++>+++++<<<<<<<<<<-]>++++.>---.>--.>+++++.>----.>++++.>---.>++.>+++.>.'
    leitura = ''
    result = self.bf.brainfuck_program(program,leitura)
    self.assertEqual(result, 'Talitha S2')
  
  def test_loops_encadeados(self):
    program = '++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++.'
    leitura = ''
    result = self.bf.brainfuck_program(program,leitura)
    self.assertEqual(result, 'Hello World!\n')
    
    
if __name__ == '__main__':
    unittest.main()
    
