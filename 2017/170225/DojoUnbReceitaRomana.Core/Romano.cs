using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace DojoUnbReceitaRomana.Core
{
    public class Romano
    {
        /*public enum TipoNueroRomano
        {
            PRATOPRINCIPAL, GUARNICAO, SUCO
        }*/
        public Dictionary<char, int> ValoresRomanos_Inteiros =
            new Dictionary<char, int>()
            {
                {'I',1 }, {'V',5 }, {'X',10 },
                {'L',50 }, {'C',100 }, {'D',500 },
                {'M',1000}
            };
        public string Valor { get; set; }

        public Romano(string valor)
        { 
            this.Valor = valor;
    
        }

        public int Avaliar()
        {
            int total = 0;
            int atual;
            int proximo;

            foreach(var iten in this.Valor)
            {
                atual = ValoresRomanos_Inteiros[iten];
                total += atual;
            }
            return total;
        }
    }
}
