import os
import cv2

from lib.crops.utils import write
from lib.crops.data.consonant import positions

consonants_path = 'datasets/light_weight/consonants'
destination_path = 'datasets/cropped/consonants'

only_run_these = [
    "tho2"
]


def extract_number(s: str):
    return int(s.split(".")[0])


for consonant in positions.keys():
    variants_path = f"{consonants_path}/{consonant}"

    if consonant not in only_run_these:
        continue

    variants = os.listdir(variants_path)
    variants = sorted(variants, key=lambda s: extract_number(s))

    for index, variant in enumerate(variants):
        position = positions.get(consonant, {})[index]

        width = position[0].split(":")
        height = position[1].split(":")

        width_start, width_end = int(width[0]), int(width[1])
        height_start, height_end = int(height[0]), int(height[1])

        image = cv2.imread(f"{variants_path}/{variant}")

        # 1
        write(
            width_start, width_end, height_start, height_end, destination_path,
            consonant, variant, image, "1"
        )

        # 2
        # write(
        #     width_start, width_end, height_start, height_end, destination_path,
        #     consonant, variant, image, "2"
        # )

        # 3
        # write(
        #     width_start, width_end, height_start, height_end, destination_path,
        #     consonant, variant, image, "3"
        # )

        # 4
        # write(
        #     width_start, width_end, height_start, height_end, destination_path,
        #     consonant, variant, image, "4"
        # )

        # 5
        # write(
        #     width_start, width_end, height_start, height_end, destination_path,
        #     consonant, variant, image, "5"
        # )

        # 6
        # write(
        #     width_start, width_end, height_start, height_end, destination_path,
        #     consonant, variant, image, "6"
        # )

        # 7
        # write(
        #     width_start, width_end, height_start, height_end, destination_path,
        #     consonant, variant, image, "7"
        # )

        # 8
        # write(
        #     width_start, width_end, height_start, height_end, destination_path,
        #     consonant, variant, image, "8"
        # )

        # 9
        # write(
        #     width_start, width_end, height_start, height_end, destination_path,
        #     consonant, variant, image, "9"
        # )

        # 10
        # write(
        #     width_start, width_end, height_start, height_end, destination_path,
        #     consonant, variant, image, "10"
        # )

        # 11
        # write(
        #     width_start, width_end, height_start, height_end, destination_path,
        #     consonant, variant, image, "11"
        # )
