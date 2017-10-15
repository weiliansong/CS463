#include <map>
#include <vector>
#include "util.h"
#include "hill.h"

using namespace std;

typedef vector<int>		    vi;
typedef vector<vi>		    vvi;
typedef map<int, int>     mii;

bool hill_climb(int n_vars, vvi clauses) {
  // Grab random assignment first
  mii dict = random_assignment(n_vars);

  // Boolean to check if we solved the problem
  bool solved = false;

  // How many iterations have we done on the same dict?
  int num_iter = 0;

  while(!solved || !(MAX_ITER - num_iter)) {
    int fitness = eval(clauses, dict);

    // How many clauses have we solved
    printf("%d / %d\n", fitness, clauses.size());

    if(fitness == clauses.size())
      solved = true;
 
    else {
      // Select a random dict in case if we are stuck at local min
      if(num_iter >= REFRESH_ITER)
        dict = random_assignment(n_vars);
    
      mii best_dict;
      int best_fitness = fitness, new_fitness;

      for(int i = 1; i <= n_vars; i++) {
        mii new_dict = dict;
        
        // Swap assignments for i
        new_dict[i] = (new_dict[i] + 1) % 2;
        new_dict[-i] = (new_dict[-i] + 1) % 2;

        new_fitness = eval(clauses, new_dict);

        if(new_fitness > best_fitness) {
          best_dict = new_dict;
          best_fitness = new_fitness;
        }
      }

      dict = best_dict;
      num_iter++;
    }
  }

  return solved;
}
