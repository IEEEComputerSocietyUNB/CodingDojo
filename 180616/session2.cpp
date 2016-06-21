#include <vector>
#include <iostream>
#include <stdio.h>
using namespace std;

/* Maratona 18\06\16
Guitar Queer-O
Autor: Matheus Pimenta

Apos comprarem o novo Guitar Hero III: Legends of Rock, Stan e Kyle tem
treinado incessantemente para se tornarem astros do rock.

Acontece que a copia do jogo dos garotos veio cheia de bugs! Agora eles
precisam da sua ajuda para continuarem o treinamento!
Dada a sequencia de combinacoes de teclas da musica e as duas sequencias de
teclas pressionados por Stan e Kyle, determine a pontuacao total dos garotos.
Cada combinacao tem no maximo 5 teclas e pode dar no minimo -5 e no maximo 5
pontos para cada garoto. Dadas duas combinacoes de teclas, a combinacao
correta e a combinacao pressionada, cada tecla fixa que aparece
simultaneamente em ambas as combinacoes acrescenta um ponto para o garoto que
a pressionou. Alem disso, para cada tecla que foi pressionada quando nao
deveria, ou que nao foi pressionada quando deveria, um ponto e subtraido.

Entrada
A primeira linha da entrada contem um unico inteiro N, o numero de combinacoes
de teclas da musica.
As proximas N linhas representam as combinacoes de teclas que devem ser
pressionadas para tocar a musica corretamente.
As proximas N linhas representam as combinacoes pressionadas por Stan.
As proximas N linhas representam as combinacoes pressionadas por Kyle.
Uma combinacao de teclas e uma string no formato G-R-Y-B-O. Variacoes deste
formato onde algumas letras sao substituidas por - (hifen) tambem sao
combinacoes validas. Cada letra representa uma tecla.

Saida
Imprima uma linha com a pontuacao total dos garotos.
Caso a pontuacao total seja a maior possivel, imprima outra linha com a
mensagem CONGRATULATIONS, YOU ARE FAGS!.
Caso a pontuacao total seja a menor possivel, imprima outra linha com a
mensagem GAME OVER, YOU SUCK!.

Restricoes
1 ≤ N ≤ 10^5

Exemplos

Entrada
1
--R-Y-B--
--R-Y---O
--R-Y-B-O

Saida
2

Entrada
1
--R-Y-B--
--R-Y-B--
--R-Y-B-O

Saida
5

Entrada
1
--R-Y-B--
--R-Y-B--
--R-Y-B--

Saida
6
CONGRATULATIONS, YOU ARE FAGS!

Entrada
1
--R-Y-B--
G-------O
G-------O

Saida
-10
GAME OVER, YOU SUCK!


A) Sobre a entrada
1. A entrada de seu programa deve ser lida da entrada padrao.
2. Quando uma linha da entrada contem varios valores, estes sao separados por
um unico espaco em branco; a entrada nao contem nenhum outro espaco em branco.
3. Cada linha, incluindo a ultima, contem o caractere final-de-linha.
4. O final da entrada coincide com o final do arquivo.

B) Sobre a saida
1. A saida de seu programa deve ser escrita na saida padrao.
2. Quando uma linha da saida contem varios valores, estes devem ser separados
por um unico espaco em branco; a saida nao deve conter nenhum outro espaco
em branco.
3. Cada linha, incluindo a ultima, deve conter o caractere final-de-linha.
*/

int main(int argc, char const *argv[]) {
    int N, score;
    bool noErrors = true;
    std::string line;
    vector<string> gameOutput;
    vector<string> kyleInput;
    vector<string> stanInput;

    // LEITURA DAS VARIÁVEIS
    getline(cin, line);
    sscanf(line.c_str(), "%d", &N);
    for (int l = 0; l < N; l++)
        getline(cin, line),
        gameOutput.push_back(line);
    for (int l = 0; l < N; l++)
        getline(cin, line),
        kyleInput.push_back(line);
    for (int l = 0; l < N; l++)
        getline(cin, line),
        stanInput.push_back(line);

    // LÓGICA DO PROGRAMA
    score = 0;
    for (int n = 0; n < N; n++)
    {
        string inlet = gameOutput.at(n);
        string kyle =  kyleInput.at(n);
        string stan =  stanInput.at(n);

        for (int i = 0; i < 9; i += 2)
        {
            if (inlet[i] == kyle[i]) { // checar se é igual
                if(inlet[i]!='-') { // checar se pode pontuar
                    score++;
                }
            }
            else {
                score--;
                noErrors = false;
            }

            if (inlet[i] == stan[i]) {
                if(inlet[i]!='-') {
                    score++;
                }
            }
            else {
                score--;
                noErrors = false;
            }
        }
    }
    std::cout << score << std::endl;
    if (score == -10*N)
        cout << "GAME OVER, YOU SUCK!" << endl;
    if (noErrors)
        cout << "CONGRATULATIONS, YOU ARE FAGS!" << endl;

    return 0;
}
