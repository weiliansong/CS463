#!/bin/bash

pushd ../

parallel --verbose -P 6 ./driver/runner.sh :::: ./driver/$1
