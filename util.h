#include <vector>
#include <map>

using namespace std;

typedef vector<int>		    vi;
typedef vector<vi>		    vvi;
typedef map<int, int>     mii;

// OR the variables together, given their assignments through a hashmap
bool set_or(vi vars, mii dict);

// IO stuff. Passing stuff by reference as we need to return more than one
void get_clauses(int &n_vars, vvi &clauses);

// Evaluate clauses to see how many are satisfied
int eval(vvi clauses, mii dict);

// Retrieve a random assignment, given number of variables and a seed
mii random_assignment(int num_vars);
