"""Custom shallow-copy implementation for dicts whose values are lists or dicts."""
from contents import recipes


def my_deepcopy(d: dict) -> dict:
    """Copy a dictrionary, creating copies of the `list` or `dict` values.

    The function will crash with an AttributeError if the values arent lists or dictionaries.

    :param d: the dictionary to copy.
    :return: A copy of `d`, with the values being copies of the original values.
    """
    dict_copy = {}

    for key, value in d.items():
        new_value = value.copy()
        dict_copy[key] = new_value

    return dict_copy


recipes_copy = my_deepcopy(recipes)
recipes_copy["Butter chicken"]["ginger"] = 300
print(recipes_copy["Butter chicken"]["ginger"])
print(recipes["Butter chicken"]["ginger"])
