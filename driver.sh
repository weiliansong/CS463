#!/bin/bash

g++ -g -o run -std=c++11 main.cpp util.h util.cpp
./run < test.cnf

# for filename in easy/*.cnf; do
#   ./run < filename > stats/filename
# done
