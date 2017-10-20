#!/bin/bash

# This small snippet of code is borrowed from my research
# Original Author: Nathan Jacobs

pushd ../

parallel --verbose ./driver/runner.sh :::: ./driver/$1
