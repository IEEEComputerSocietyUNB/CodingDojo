#include <vector>
#include <iostream>
#include <stdio.h>
using namespace std;

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
