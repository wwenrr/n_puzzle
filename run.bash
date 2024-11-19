#!/bin/bash

if [ -z "$2" ]; then
    echo "Thiếu tham số --max-depth, --size"
    exit 1
fi

python3 -m src.service.n_puzzle.main --max-depth "$1" --size "$2" > sample_test_output/test"$3".txt

echo "Chạy thành công với max-depth=$1, size=$2, test=$3"