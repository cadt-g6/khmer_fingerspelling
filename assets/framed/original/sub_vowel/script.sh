#!/bin/bash

declare -a NAME=("treisapt" "salap_pi" "robat" "bantak" "samyouk_sanhnhea" "lekh_tou" "koumutr" "chamnoch_pirkus" "khand" "asda" "otean" "tondokhead" "sanha_sur" "kakabat");

for i in "${NAME[@]}"
do
    mkdir ${i}
done
