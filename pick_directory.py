from subdirectory import SUBDIR


def pick_directory(value):
    """
    Determines the category of a given file based on its suffix.

    Args:
        value (str): The suffix of the file.

    Returns:
        str: The category of the file.

    """
    for category, suffixes in SUBDIR.items():
        for suffix in suffixes:
            if suffix == value:
                return category
