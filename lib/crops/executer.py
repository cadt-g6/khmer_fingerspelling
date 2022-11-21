import os
import cv2
from lib.crops.utils import write


def execute(
    childrens: list,
    only_run: list,
    dataset_path: str,
    destination_path: str,
    positions: dict
):
    for type in os.listdir(dataset_path):
        parent = f"{dataset_path}/{type}"

        if not os.path.isdir(parent):
            continue

        for character in os.listdir(parent):
            variants_path = f"{parent}/{character}"

            if len(only_run) > 0 and f"{type}/{character}" not in only_run:
                continue

            if not os.path.isdir(variants_path):
                continue

            variants = os.listdir(variants_path)
            variants = sorted(variants, key=lambda s: int(s.split(".")[0]))

            for index, variant in enumerate(variants):
                position = positions.get(type, {}).get(character, [])[index]

                width = position[0].split(":")
                height = position[1].split(":")

                height_start, height_end = int(width[0]), int(width[1])
                width_start, width_end = int(height[0]), int(height[1])

                image = cv2.imread(f"{variants_path}/{variant}")

                for index, element in enumerate(childrens):
                    height_start_add = element[0][0]
                    height_end_add = element[0][1]
                    width_start_add = element[1][0]
                    width_end_add = element[1][1]

                    height_start += height_start_add
                    height_end += height_end_add
                    width_start += width_start_add
                    width_end += width_end_add

                    write(
                        height_start=height_start,
                        height_end=height_end,
                        width_start=width_start,
                        width_end=width_end,
                        destination_path=destination_path,
                        character=character,
                        variant=variant,
                        image=image,
                        id=f"{index+1}",
                    )
