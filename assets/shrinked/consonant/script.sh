#!/bin/bash

declare -a NAME=("ka" "kha" "ko" "kho" "ngo" "cha" "chha" "cho" "chho" "nho" "da" "tha1" "do" "tho1" "na" "ta" "tha2" "to" "tho2" "no" "ba" "pha" "po" "pho" "mo" "yo" "ro" "lo" "vo" "sa" "ha" "la" "or");

for i in "${NAME[@]}"
do
    mkdir ${i}
done
