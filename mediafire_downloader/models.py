from typing import TypedDict
import pathlib


class File(TypedDict):
    """ Representation of a file """

    path: pathlib.Path
    filename: str
    download_link: str

