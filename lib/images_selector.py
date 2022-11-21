import os


class ImagesSelector:
    def __init__(self) -> None:
        pass

    def extract_number(self, s: str):
        return int(s.split(".")[0])

    def take_three_from_each_sample(self, groups: dict):
        cleaned_groups = dict()

        for key in groups.keys():
            group: dict = groups[key]
            cleaned_groups[key] = dict()

            for group_key in group.keys():
                variants: list = group[group_key]

                # item1 = variants[0]
                item2 = variants[len(variants) // 2]
                # item3 = variants[len(variants) - 1]

                # cleaned_groups[key][group_key] = [
                #     item1, item2, item3]
                cleaned_groups[key][group_key] = [item2]

        return cleaned_groups

    def group_each_sample(self, images_path: str, except_classes: dict = {}):
        # images_groups can be consonant_group, or vowel_group, etc.
        images_groups = dict()
        classes = os.listdir(images_path)

        # class_name can be consonant_name, or vowel_name, etc.
        for di, class_name in enumerate(classes):
            variants_path = f'{images_path}/{class_name}'

            if not os.path.isdir(variants_path):
                continue

            variants = os.listdir(variants_path)
            variants = [variant for variant in variants if variant.endswith(
                ".jpg") and "_" not in variant]
            variants = sorted(variants, key=lambda s: self.extract_number(s))

            if (len(variants) == 0):
                continue

            group = dict()
            previus_item = self.extract_number(variants[0])
            starter_index = -1

            debug_starter = []

            for index, variant in enumerate(variants):
                current_item = self.extract_number(variant)
                is_starter = current_item - previus_item > 1 or index == 0
                previus_item = current_item

                if is_starter:
                    debug_starter.append(variant)
                    starter_index = starter_index + 1
                    group[starter_index] = [variant]
                else:
                    group[starter_index].append(variant)

            images_groups[class_name] = group
            max = except_classes.get(class_name, 8)

            if (len(group) != max):
                raise Exception(
                    f"Must be 8 samples: {di}/{len(classes)}:{variants_path}\n{debug_starter}")

        return images_groups
