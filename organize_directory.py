import os
from pathlib import Path

from get_user_input import get_user_path_input
from pick_directory import pick_directory


def organize_directory(path):
    """
    Organizes files in the specified directory by moving them into
    appropriate subdirectories based on their file type.

    Args:
        path (str): The path of the directory to be organized.

    Returns:
        None

    Raises:
        None

    """
    if path is None:
        return

    files = os.scandir(path)

    print("Organizing files...")
    for file in files:
        if file.is_dir():
            continue
        file_path = Path(file)
        file_Type = file_path.suffix.lower()
        directory = pick_directory(file_Type)
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


if __name__ == "__main__":
    path = get_user_path_input()
    organize_directory(path)
