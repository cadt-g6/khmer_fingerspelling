#!/bin/bash

declare -a NAME=("e" "ei" "o" "ou" "au_treisapt" "rue" "rueu" "lue" "lueu" "ae" "ai" "ao" "au");

for i in "${NAME[@]}"
do
    mkdir ${i}
done
