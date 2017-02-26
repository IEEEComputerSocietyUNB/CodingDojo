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
    public class RomanoTest
    {
        [Test]
        public void VerificarSimboloI()
        {
            Romano num1 = new Romano("I");
            int valorRomano = num1.Avaliar();
            Assert.AreEqual(1, valorRomano);
        }

        [Test]
        public void VerificarSimboloV()
        {
            Romano num1 = new Romano("V");
            int valorRomano = num1.Avaliar();
            Assert.AreEqual(5, valorRomano);
        }

        [Test]
        public void VerificarDoisSimbolos()
        {
            Romano num1 = new Romano("II");
            int valorRomano = num1.Avaliar();
            Assert.AreEqual(2, valorRomano);
        }

        [Test]
        public void VerificarTresSimbolos()
        {
            Romano num1 = new Romano("III");
            int valorRomano = num1.Avaliar();
            Assert.AreEqual(3, valorRomano);
        }
        [Test]
        public void VerificarRetornoQuatro()
        {
            Romano num = new Romano("IV");
            int valorRomano = num.Avaliar();
            Assert.AreEqual(4, valorRomano);
        }
        //[Test]
        //public void VerificarQuatroSimbolosDoisDois()
        //{
        //    Romano num1 = new Romano("XXII");
        //    int valorRomano = num1.Avaliar();
        //    Assert.AreEqual(22, valorRomano);
        //}

       // [Test]
       // public void VerificarSimboloQuatro()
        //{
          //  Romano num1 = new Romano("IV");
            //int valorRomano = num1.Avaliar();
           // Assert.AreEqual(4, valorRomano);
      //  }
    }
}
