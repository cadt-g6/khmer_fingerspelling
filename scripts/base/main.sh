rm -rf datasets/csv
mkdir datasets/csv

find scripts/independent_vowels/ -name "*.sh" -exec {} \;
find scripts/sub_vowels/ -name "*.sh" -exec {} \;
find scripts/vowels/ -name "*.sh" -exec {} \;
