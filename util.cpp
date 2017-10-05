#include <iostream>
#include <vector>
#include "util.h"

using namespace std;

typedef vector<int>		    vi;
typedef vector<vi>		    vvi;
typedef map<int, int>     mii;

bool _or(vi vars, mii assignment) {
  int results = 0;

  for(int i = 0; i < vars.size(); i++) 
    results += assignment[vars[i]];

  return results;
}

bool _and(vi vars, mii assignment) {
  int results = 1;

  for(int i = 0; i < vars.size(); i++) 
    results *= vars[i];

  return results;
}

int abs(int a) {
  return a > 0 ? a : -a;
}

vvi get_clauses() {
  // IO stuff...
  char first;
  cin >> first;

  while(first == 'c') {
    cin.ignore(256, '\n');
    cin >> first;
  }

  if(first != 'p') {
    cout << "No p at the beginning, exiting...\n";
    exit(1);
  }

  string format;
  cin >> format;

  if(format != "cnf") {
    cout << "Not CNF format, exiting...\n";
    exit(1);
  }

  int n_vars, n_clauses;
  cin >> n_vars >> n_clauses;

  vvi clauses;

  // Grab all the clauses
  while(n_clauses--) {
    int var; vi clause;
    cin >> var;

    while(var != 0) {
      clause.push_back(var);
      cin >> var;
    }

    clauses.push_back(clause);
  }

  return clauses;
}
