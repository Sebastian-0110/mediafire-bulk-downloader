# Utility functions


import re


URL_VALIDATION_REGEX = re.compile(
	r"https:\/\/www\.mediafire\.com\/folder\/[a-zA-Z0-9]+(\/.+)?\/?",
	re.IGNORECASE
)


def is_valid_url(url: str) -> bool:
	""" Check if an url matches the mediafire folder url regex """

	return not re.match(URL_VALIDATION_REGEX, url) is None


def get_folder_key(url: str) -> str:
	""" Get the folder key from an url """

	return url.split("/")[4]


def download_file(path: str, file: dict) -> None:
	""" Download files """

	raise NotImplementedError("Implement this")
