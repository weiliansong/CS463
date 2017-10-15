#include <map>
#include <vector>

#define MAX_ITER 10000
#define REFRESH_ITER 1000

using namespace std;

typedef vector<int>		    vi;
typedef vector<vi>		    vvi;
typedef map<int, int>     mii;

bool hill_climb(int n_vars, vvi clauses);
