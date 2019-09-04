#!/bin/bash

array=("a a a" "b b b" "c c c")

echo ${array[2]}
echo ${array[*]}

newarr=("${array[*]}")
echo $newarr
