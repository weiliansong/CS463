#include <iostream>
#include <string>
#include <vector>
#include <ctime>
#include <cstdlib>
#include "util.h"

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

  mii dict = random_assignment(n_vars);

  for(auto it = dict.begin(); it != dict.end(); it++)
    cout<< it->first << ' ' << it->second << endl;

  return 0;
}

// Notes: make sure to index correctly into the array of assignment
