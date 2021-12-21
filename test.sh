#!/bin/bash -e

declare -a parts
parts=( $(find . -type f -name 'part*.py' | sort) )

for part in "${parts[@]}"
do
    echo "Running ${part}"
    python3 "${part}" | sed 's/^/    /g'
done
