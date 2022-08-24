#!/bin/bash
readonly DATA=$(dirname `pwd`)/CUtopia-data
echo moving $1 to $DATA
cp -r data/$1/* $DATA
