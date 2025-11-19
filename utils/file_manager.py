import csv
import os


def writerows(filename: str, data: list[list]) -> None:
    """
    write given list of data to csv
    :param filename: file name
    :param data: list of data
    :return: None
    """
    path = f"data/{filename}.csv"
    with open(file=path, mode="w", encoding="UTF-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(data)


def read(filename: str) -> list:
    """
    read csv file as a list
    :param filename: file name
    :return: list of data
    """
    path = f"data/{filename}.csv"
    if os.path.exists(path=path):
        with open(file=path, mode="r", encoding="UTF-8", newline="") as file:
            reader = csv.reader(file)
            return list(reader)
    return list()


def append(filename: str, data: list) -> None:
    """
    write given list of data to csv
    :param filename: file name
    :param data: list of data
    :return: None
    """
    path = f"data/{filename}.csv"
    with open(file=path, mode="a", encoding="UTF-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(data)
