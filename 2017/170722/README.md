# Coding Dojo UnB

## Tema: OpenStreetMap

- Linguagem: Python 3.
- Biblioteca de testes: pytest
- Mestre: @WilleMarcel

### Desafio .1

O OpenStreetMap é um grande banco de dados geoespaciais livre e colaborativo. Vamos utilizar os dados do OSM nesse desafio. O Overpass Turbo é um dos métodos de consulta que dispomos para consultar e extrair dados do OSM. Vamos utilizá-lo para extrair a capital de todos os países do mundo a partir do OpenStreetMap. Você pode acessar essa consulta feita previamente: http://overpass-turbo.eu/s/qxe e exportar o arquivo no formato GeoJSON para utilizá-lo nos próximos passos. Uma simples query nos dá uma infinidade de dados, observe que as cidades possuem informação de nomes em diversos idiomas. Com esses dados, faremos um pequeno jogo. A forma de interação do jogo será pela linha de comando.

Teremos os seguintes modos de jogo. Trabalharemos cada um deles em um sprint.

- Sprint #1 -Maior distância
Três cidades serão sorteadas. Uma será o ponto inicial e as outras duas serão os destinos. O jogador deve acertar qual das duas cidades destino fica mais próxima da cidade inicial.

- Sprint #2
Tente tratar o problema da linha internacional de data.

- Sprint #3 - Onde fica
O software apresentará o nome de uma cidade e o jogador terá que responder o nome do país da mesma em inglês. Caso o jogador prefira não responder, ele terá uma segunda chance, onde serão apresentados nomes de 5 países para que ele escolha a opção correta. O jogo não deve fazer distinção entre caracteres minúsculos e maiúsculos.

- Sprint #4 - Maiores populações
Serão sorteadas 4 capitais e o jogador terá que ordená-las em relação à população, em ordem decrescente. O jogo deve informar a porcentagem de acerto.

Sugestão: para ser mais fácil de testar, podemos usar uma sintaxe como:

  Fase.problema()
  Fase.responder(resposta)


### Desafio .2

Temos 3 tipos principais de elementos geoespaciais: nós (pontos), linhas e polígonos. Todos eles são constituídos por uma ou mais coordenadas geográficas. A coordenada geográfica é constituída por dois valores: longitude e latitude.
Escreva uma função que retorne o centroide de um elemento geoespacial, sendo ele um nó, uma linha ou um polígono. Escreva uma outra função que retorne o Bounding Box (BBOX) de uma linha ou de um polígono (não é possível calcular a bounding box de um nó). Em todos os casos, o dado de entrada deve ser apenas uma tupla ou lista.

O usuário deve inserir o nome de dois países e o software deve retornar a distância entre os centroides, além disso o software deve informar se os BBOX se intersectam e qual seria o polígono da área de intersecção dos BBOX

## Recursos
https://nominatim.openstreetmap.org/search/?country=Argentina&format=json
http://www.openstreetmap.org/relation/286393/
