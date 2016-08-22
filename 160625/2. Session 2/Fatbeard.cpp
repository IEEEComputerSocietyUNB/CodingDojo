#include <iostream>
#include <vector>
#include <cstdio>

using namespace std;

struct Edge
{
  int gold;
  int dest;
};
int raidPath(int currentPoint, vector<Edge> pathList, int goldSum);


int main(int argv, char* argc[])
{

  int N,M,F,G,A,B; // F ponto inicial

  scanf("%d %d %d\n", &N, &M, &F);

  vector<Edge> pathList(M);   // caminho
  vector<int> visitedList(N); // caminho visitados
  vector<Edge>::iterator it;

  while(scanf("%d %d %d\n", &G, &A, &B))
  {
    pathList[A].gold = G;
    pathList[A].dest = B;
  }


  return 0;
}

int raidPath(int currentPoint, vector<Edge> pathList, vector<int> visitedPoints, int goldSum)
{
  /*
  if(checkCycle(visitedPoints,currentPoint)){
    goldSum = 0;
    return goldSum;
  }
  else{

    goldSum += raidPath(pathList[currentPoint].dest,pathList,visitedPoints,goldSum);
  }
  */
  return pathList[currentPoint].gold;
}
