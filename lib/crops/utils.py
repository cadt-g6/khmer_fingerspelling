
import cv2
import os
import pathlib


# y:y+h, x:x+w
def write(
    height_start,
    height_end,
    width_start,
    width_end,
    destination_path,
    character,
    variant,
    image,
    id,
):
    cropped_image = image[height_start:height_end,
                          width_start:width_end]

    name, extension = variant.split('.')
    parent_path = f"{destination_path}/{character}"

    filename = f"{name}-{id}-{character}.{extension}"
    filepath = f"{parent_path}/{filename}"

    pathlib.Path(parent_path).mkdir(parents=True, exist_ok=True)
    cv2.imwrite(filepath, cropped_image)
