using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;


namespace DojoUnbReceitaRomana.Core
{
    public class Produto
    {
        //string
        //int
        //double
        //char

        public string Nome { get; set; }//
        public double Valor { get; set; }
        public Tipo tipo { get; set; }

        public Produto(string nome, double valor, Tipo tipo)
        {
            this.Nome = nome;
            this.Valor = valor;
            this.tipo = tipo;

        }

        public double CalcularTotal()
        {
            return 0;
      
        }

        public double CalcularPorcentagem()
        {
            if(this.tipo == Tipo.PRATOPRINCIPAL)
            {
                if(this.Valor >= 10)
                {
                    return this.Valor * .80;
                }
                else
                {
                    return this.Valor * .90;
                }
            }
            else if(this.tipo == Tipo.GUARNICAO || this.tipo == Tipo.SUCO)
            {
                if (this.Valor >= 3)
                {
                    return this.Valor * .95;
                }
                else
                {
                    return this.Valor * .99;
                }
            }
            return 0;
        }
    }

}
