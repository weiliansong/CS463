#include <vector>
#include <map>

using namespace std;

typedef vector<int>		    vi;
typedef vector<vi>		    vvi;
typedef map<int, int>     mii;

// OR the variables together, given their assignments through a hashmap
bool _or(vi vars);

// AND the variables together, given their assignments through a hashmap
bool _and(vi vars);

// Sum a vector of elements
int sum(vi nums);

// IO stuff...
vvi get_clauses();

// Evaluate clauses to see how many are satisfied
int eval(vvi clauses, mii dict);
