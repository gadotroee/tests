from typing import Hashable, Dict


def get_without_none_values(dictionary: dict):
    """Returns new dict without None values"""
    return {
        key: value for key, value in dictionary.items() if value is not None
    }


def invert_dict(original_dict: Dict[Hashable, Hashable]):
    """
    Returns inverted dictionary.
    All values must be unique, Otherwise, ValueError Exception will be raised
    e.g: input_dict: {'a': 1, 'b': 2} -> output_dict { 1: 'a', 2: 'b' }
    """
    if len(original_dict.values()) != len(set(original_dict.values())):
        raise ValueError("Cannot contains non-unique values")
    return {v: k for k, v in original_dict.items()}
