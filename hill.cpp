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

  int num_iter = 0, num_refresh = 0;

  // We stop if we solved, reached max iter or max refresh
  while(!solved || !(MAX_ITER - num_iter) || !(MAX_REFRESH - num_refresh)) {
    int fitness = eval(clauses, dict);

    // How many clauses have we solved
    printf("%d / %d\n", fitness, clauses.size());

    if(fitness == clauses.size())
      solved = true;
 
    else { 
      int best_choice, swap;
      int best_fitness = fitness, new_fitness;

      for(int i = 1; i <= n_vars; i++) {
        // Swap assignments for i
        swap = dict[i];
        dict[i] = dict[-i];
        dict[-i] = swap;

        new_fitness = eval(clauses, dict);

        if(new_fitness > best_fitness) {
          best_choice = i;
          best_fitness = new_fitness;
        }

        // Swap it back
        swap = dict[i];
        dict[i] = dict[-i];
        dict[-i] = swap;
      }

      // Swap it back
      swap = dict[best_choice];
      dict[best_choice] = dict[-best_choice];
      dict[-best_choice] = swap;
      num_iter++;

      // Select a random dict in case if we are stuck at local min
      if((num_iter >= REFRESH_ITER) || (best_fitness == fitness)) {
        printf("Stuck at local min, randomizing assignments\n");
        dict = random_assignment(n_vars);
        num_refresh++;
      }
    }
  }

  return solved;
}
