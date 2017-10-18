#!/bin/bash

pushd ../

set -e

parallel :::: ./driver/methods.list
