#!/bin/sh
dir=$(cd -P -- "$(dirname -- "$0")" && pwd -P)
cd "$dir"
./rotmg_update.py $1
