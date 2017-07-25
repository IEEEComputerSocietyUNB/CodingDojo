using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using NUnit.Framework;
using DojoUnbReceitaRomana.Core;

namespace DojoUnbReceitaRomana.Test
{
    [TestFixture]
    public class ProdutoTest
    {
        //[Test]
        //public void VerificarValorTotal()
        //{
        //    Produto p = new Produto("Arroz",2, Tipo.GUARNICAO);
        //    double valor = p.CalcularTotal();
        //    Assert.AreEqual(20,valor);

        //}

        [Test]
        public void ReceitaPratoPrincipalTemDesconto10mais()
        {
            Produto p = new Produto("Arroz Branco", 11, Tipo.PRATOPRINCIPAL);
            double valor = p.CalcularPorcentagem();
            Assert.AreEqual(8.8, valor);

        }

        [Test]
        public void ReceitaPratoPrincipalTemDesconto10menos()
        {
            Produto p = new Produto("Carne", 9, Tipo.PRATOPRINCIPAL);
            double valor = p.CalcularPorcentagem();
            Assert.AreEqual(8.1, valor);

        }

        [Test]
        public void ReceitaGuarnicaoTemDesconto3mais()
        {
            Produto p = new Produto("Feijao", 4, Tipo.GUARNICAO);
            double valor = p.CalcularPorcentagem();
            Assert.AreEqual(3.8, valor);

        }

        [Test]
        public void ReceitaGuarnicaoTemDesconto3menos()
        {
            Produto p = new Produto("Salada", 2, Tipo.GUARNICAO);
            double valor = p.CalcularPorcentagem();
            Assert.AreEqual(1.98, valor);

        }

        [Test]
        public void ReceitaSucoTemDesconto3mais()
        {
            Produto p = new Produto("Suco de Uva", 4, Tipo.SUCO);
            double valor = p.CalcularPorcentagem();
            Assert.AreEqual(3.8, valor);

        }

        [Test]
        public void ReceitaSucoTemDesconto3menos()
        {
            Produto p = new Produto("Suco de Laranja", 2, Tipo.SUCO);
            double valor = p.CalcularPorcentagem();
            Assert.AreEqual(1.98, valor);

        }
    }
}
