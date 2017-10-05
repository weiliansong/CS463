#include <vector>
#include <map>

using namespace std;

typedef vector<int>		    vi;
typedef vector<vi>		    vvi;
typedef map<int, int>     mii;

bool _and(vi vars);
bool _or(vi vars);
int abs(int a);
vvi get_clauses();
