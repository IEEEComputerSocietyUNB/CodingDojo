package br.unb.dojo

object Bar {
  
  def sizeof(xs: String): Int = {
     if (xs.isEmpty()) {
       0
     }
     else {
       if (xs.head != 'A' && 
           xs.head != 'C' &&
           xs.head != 'G' &&
           xs.head != 'T' &&
           xs.head != 'a' && 
           xs.head != 'c' &&
           xs.head != 'g' &&
           xs.head != 't'){
         0 + sizeof(xs.substring(1))
       }
       else {
         1 + sizeof(xs.substring(1)) 
       }
     }
  }
  
  def countletters(c:Char, xs:String): Int = {
     if (xs.isEmpty()) {
       0
     }
     else {
       if (xs.head.toLower != c.toLower){
         0 + countletters(c, xs.substring(1))
       }
       else {
         1 + countletters(c, xs.substring(1))
       }
       //+ countletters(c, xs.substring(1))
     }
  }
  
  def countLoop(result: Map[Char, Int], letters: List[Char], phrase: String): Map[Char, Int] = {
       
    if(letters.isEmpty){
      return result
    }
    
    val quant_char = countletters(letters.head,phrase)
    val new_result = result++Map(letters.head -> quant_char)
   countLoop(new_result, letters.tail,phrase)
  }
  
  def countAllLetters(xs:String): Map[Char, Int] = {
    val letters = List('a', 'g', 'c', 't')
       
   countLoop(Map[Char, Int](), letters, xs)     
    
  }
  
}