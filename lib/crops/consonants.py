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


def execute():
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

            height_start, height_end = int(width[0]), int(width[1])
            width_start, width_end = int(height[0]), int(height[1])

            image = cv2.imread(f"{variants_path}/{variant}")

            childrens = [
                {
                    "height_start_add": 0,
                    "height_end_add": 0,
                    "width_start_add": 0,
                    "width_end_add": 0,
                },
                {
                    "height_start_add": 0,
                    "height_end_add": 0,
                    "width_start_add": 0,
                    "width_end_add": 0,
                },
                {
                    "height_start_add": 0,
                    "height_end_add": 0,
                    "width_start_add": 0,
                    "width_end_add": 0,
                },
                {
                    "height_start_add": 0,
                    "height_end_add": 0,
                    "width_start_add": 0,
                    "width_end_add": 0,
                },
                {
                    "height_start_add": 0,
                    "height_end_add": 0,
                    "width_start_add": 0,
                    "width_end_add": 0,
                },
                {
                    "height_start_add": 0,
                    "height_end_add": 0,
                    "width_start_add": 0,
                    "width_end_add": 0,
                },
                {
                    "height_start_add": 0,
                    "height_end_add": 0,
                    "width_start_add": 0,
                    "width_end_add": 0,
                },
                {
                    "height_start_add": 0,
                    "height_end_add": 0,
                    "width_start_add": 0,
                    "width_end_add": 0,
                },
                {
                    "height_start_add": 0,
                    "height_end_add": 0,
                    "width_start_add": 0,
                    "width_end_add": 0,
                }
            ]

            for index, element in enumerate(childrens):
                height_start_add = element.get('height_start_add', 0)
                height_end_add = element.get('height_end_add', 0)
                width_start_add = element.get('width_start_add', 0)
                width_end_add = element.get('width_end_add', 0)

                height_start = height_start + height_start_add
                height_end = height_end + height_end_add
                width_start = width_start + width_start_add
                width_end = width_end + width_end_add

                write(
                    height_start=height_start,
                    height_end=height_end,
                    width_start=width_start,
                    width_end=width_end,
                    destination_path=destination_path,
                    consonant=consonant,
                    variant=variant,
                    image=image,
                    id=f"{index+1}",
                )
