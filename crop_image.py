from lib.crops.data.vowels import positions as vpositions
from lib.crops.data.sub_vowels import positions as svpositions
from lib.crops.data.stack_consonants import positions as scpositions
from lib.crops.data.independent_vowels import positions as ivpositions
from lib.crops.data.consonants import positions as cpositions
from lib.crops.executer import execute

dataset_path = 'datasets/light_weight'
destination_path = 'datasets/cropped'

# height_start_add, height_end_add
# width_start_add, width_end_add
childrens = [
    [[0, 0], [0, 0]],
    [[0, 0], [0, 0]],
    [[0, 0], [0, 0]],
    [[0, 0], [0, 0]],
    [[0, 0], [0, 0]],
    [[0, 0], [0, 0]],
    [[0, 0], [0, 0]],
    [[0, 0], [0, 0]],
    [[0, 0], [0, 0]],
]

center_positions = {
    "consonants": cpositions,
    "independent_vowels": ivpositions,
    "stack_consonants": scpositions,
    "sub_vowels": svpositions,
    "vowels": vpositions,
}

execute(
    childrens=childrens,
    dataset_path=dataset_path,
    destination_path=destination_path,
    positions=center_positions,
    only_run=[
        # "consonants/tho2",
        # "independent_vowels/ae"
        # "stack_consonants/stack_ba"
        # "sub_vowels/asda",
        # "vowels/bantak"
    ],
)
