#!/bin/bash

if [ $# -ne 1 ] ; then
    echo "day argument missing!"
    exit 1
fi

cd D:/Repositories/advent-of-code2019
mkdir -p src/day0$1
touch src/day0$1/day0$1.py