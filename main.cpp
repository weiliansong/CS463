#include <iostream>
#include <string>
#include <vector>
#include <ctime>
#include <cstdlib>
#include "util.h"
#include "hill.h"

using namespace std;

typedef vector<int>		    vi;
typedef vector<vi>		    vvi;
typedef map<int, int>     mii;

int main() {
  int n_vars;
  vvi clauses;

  get_clauses(n_vars, clauses);

  // Test to ensure correct reading of file
  // for(int i=0; i < clauses.size(); i++) {
  //   for(int j = 0; j < clauses[i].size(); j++)
  //     printf("%d ", clauses[i][j]);
  //   printf("\n");
  // }
  
  bool solved = hill_climb(n_vars, clauses);

  if(solved)
    printf("SATISFIABLE\n");
  else
    printf("NOT SATISFIABLE\n");

  return 0;
}
