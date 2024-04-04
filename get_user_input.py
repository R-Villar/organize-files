import os


def get_user_path_input():
    """
    Prompts the user to enter the path to the directory they want to organize.

    Returns:
        str: The path to the directory entered by the user.

    Raises:
        None

    Example:
        Enter the path to the directory you want
        to organize: /Users/user/Documents
        The path you are trying to organize is: /Users/user/Documents
        '/Users/user/Documents'
    """
    while True:
        path = input(
            "Enter the path to the directory you want to organize, or 'q' to quit: "
        )
        if path.lower() == "q":
            break
        if os.path.exists(path):
            print("The path you are trying to organize is: ", path)
            return path
        else:
            print(
                "The specified path does not exist. Please try again. or press 'q' to quit."
            )
