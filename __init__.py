from src.author import Author
from src.department import Department
from src.publication import Publication
from src.university import University

_univer = None


def getUniversity():
    global _univer
    if _univer is None:
        _univer = University()
    return _univer


if __name__ == "__main__":
    getUniversity()