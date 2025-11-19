from utils.file_manager import read


def generate_new_id(filename: str):
    data = read(filename=filename)
    if data:
        return int(data[-1][0]) + 1
    return 1
