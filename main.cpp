#include <iostream>
#include <string>
#include <vector>

typedef vector<int> vi;
typedef vector<vi> vvi;

using namespace std;

int abs(int a) {
  return a > 0 ? a : -a;
}

int main() {
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

  return 0;
}


// Notes: make sure to index correctly into the array of assignment
