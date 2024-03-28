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


# path = "/Users/remy/Downloads"


# print(os.path.exists(path))
# try:
#     all_files = os.scandir(path)

# except FileNotFoundError:
#     print("The specified path does not exist.")


def getUserPathInput():

    while True:
        path = input("Enter the path to the directory you want to organize: ")
        if os.path.exists(path):
            print("The path you are trying to organize is: ", path)
            return path
        else:
            print("The specified path does not exist.")

    # path = input("Enter the path to the directory you want to organize: ")
    # while not os.path.exists(path):
    #     print("The specified path does not exist.")
    #     path = input("Enter the path to the directory you want to organize: ")
    # return path


path = getUserPathInput()

print(path)


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

        directory_path = Path(path) / directory
        try:
            if not directory_path.is_dir():
                os.mkdir(directory_path)
            file_path.rename(directory_path / file_path.name)
        except FileExistsError:
            pass
    print("Files organized.")


organizeDirectory()
