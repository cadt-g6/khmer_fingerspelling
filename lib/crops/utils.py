
import cv2
import os
import pathlib


def write(
    width_start,
    width_end,
    height_start,
    height_end,
    destination_path,
    consonant,
    variant,
    image,
    id,
):
    print(f'{consonant}/{variant}')

    cropped_image = image[width_start:width_end,
                          height_start:height_end]

    name, extension = variant.split('.')
    parent_path = f"{destination_path}/{consonant}"

    filename = f"{name}-{id}.{extension}"
    filepath = f"{parent_path}/{filename}"

    pathlib.Path(parent_path).mkdir(parents=True, exist_ok=True)
    cv2.imwrite(filepath, cropped_image)
