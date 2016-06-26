using NUnit.Framework;

namespace CalculadoraRomana
{
    [TestFixture]
    class CalcRomanaTeste
    {
        private CalcRomana Calc = new CalcRomana();
        [Test]
        public void testa_se_retorna_I()
        {
            string input = "I";
            string output = CalcRomana.GetNumero(input);
            Assert.AreEqual(output, "I");
        }


        [Test]
        public void testa_se_retorna_input()
        {
            string input1 = "I";
            string input2 = "I";
            Calc.Input1 = input1;
            Calc.Input2 = input2;
            var out1 = Calc.Input1;
            var out2 = Calc.Input2;
            Assert.AreEqual(out1, input1);
            Assert.AreEqual(out2, input2);
        }

        [Test]
        public void testa_se_armazena_input()
        {
            string input1 = "I";
            string input2 = "I";
            var out1 = Calc.Input1;
            var out2 = Calc.Input2;
            Assert.AreEqual(out1, input1);
            Assert.AreEqual(out2, input2);
        }
    }
}
