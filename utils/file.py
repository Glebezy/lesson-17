import os


def get_dir(filedir: str):
    CURRENT_FILE = os.path.abspath(__file__)
    DIRECTORY = os.path.dirname(CURRENT_FILE)
    FILE = os.path.join(DIRECTORY, "..", filedir)

    return FILE
