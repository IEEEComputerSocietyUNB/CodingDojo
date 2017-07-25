using NUnit.Framework;

namespace ExemploIntroducao
{
    [TestFixture]
    class Simples_Teste
    {
        [Test]
        public void Quando1_Retorna1()
        {
            int input = 1;
            string output = Simples.GetValorEmString(input);
            Assert.AreEqual(output, "1");
        }
    }
}
