import os
from pathlib import Path

from subdirectory import SUBDIR


def pickDirectory(value):
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


download_folder = "/Users/remy/Downloads"

all_files = os.scandir(download_folder)


def organizeDirectory():

    print("Organizing files...")
    for item in all_files:
        if item.is_dir():
            continue
        file_path = Path(item)
        file_Type = file_path.suffix.lower()
        directory = pickDirectory(file_Type)
        if directory is None:
            continue

        directory_path = Path(download_folder) / directory
        try:
            if not directory_path.is_dir():
                os.mkdir(directory_path)
            file_path.rename(directory_path / file_path.name)
        except FileExistsError:
            pass
    print("Files organized.")


organizeDirectory()

# os.mkdir(f"{download_folder}/test")
