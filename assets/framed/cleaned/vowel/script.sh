#!/bin/bash

declare -a NAME=("srak_a" "srak_i" "srak_ei" "srak_oe" "srak_eu" "srak_o" "srak_ou" "srak_uo" "srak_aeu" "srak_oea" "srak_ie" "srak_e" "srak_ae" "srak_ai" "srak_ao" "srak_au" "srak_um" "srak_om" "srak_oam" "srak_ah" "srak_oh" "srak_eh" "srak_aoh");

for i in "${NAME[@]}"
do
    mkdir ${i}
done
