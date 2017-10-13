#include <ctime>
#include <cstdlib>
#include <iostream>
#include <vector>
#include "util.h"

using namespace std;

typedef vector<int>		    vi;
typedef vector<vi>		    vvi;
typedef map<int, int>     mii;

bool _or(vi vars, mii dict) {
  int results = 0;

  for(int i = 0; i < vars.size(); i++) 
    results += dict[vars[i]];

  return results;
}

bool _and(vi vars, mii dict) {
  int results = 1;

  for(int i = 0; i < vars.size(); i++) 
    results *= dict[vars[i]];

  return results;
}

int sum(vi nums) {
  int _sum = 0;
  for(int i = 0; i < nums.size(); i++)
    _sum += nums[i];

  return _sum;
}

void get_clauses(int &n_vars, vvi &clauses) {
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

  int n_clauses;
  cin >> n_vars >> n_clauses;

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
}

int eval(vvi clauses, mii dict) {
  vi clause_evals;

  for(int i = 0; i < clauses.size(); i++)
    clause_evals.push_back(_or(clauses[i], dict));

  return sum(clause_evals);
}

mii random_assignment(int num_vars) {
  srand(time(0));

  mii assignments;

  for(int i = 1; i <= num_vars; i++) {
    int value = rand() % 2;
    assignments[i] = value;
    assignments[-i] = (value + 1) % 2;
  }

  return assignments;
}
