# Utility functions

import re
import pathlib
import requests
from bs4 import BeautifulSoup

from .models import File


URL_VALIDATION_REGEX = re.compile(
	r"https:\/\/www\.mediafire\.com\/folder\/[a-zA-Z0-9]+(\/.+)?\/?",
	re.IGNORECASE
)


def is_valid(url: str) -> bool:
	""" Check if an url matches the mediafire folder url regex """

	return not re.match(URL_VALIDATION_REGEX, url) is None


def get_folder_key(url: str) -> str:
	""" Get the folder key from an url """

	return url.split("/")[4]

def __scrape_direct_download_link(download_url: str) -> str:
	""" Scrape the direct download link from the mediafire page """

	with requests.get(download_url) as response:
		soup = BeautifulSoup(response.text, "html.parser")

	download_link = soup.find("a", class_="input popsok").attrs["href"]

	if download_link:
		return download_link

	raise Exception("Could not scrape direct download link (download link not found)")

def download_file(file: File, destination: pathlib.Path) -> None:
	""" Download files """

	file["path"] = pathlib.Path(destination, file["path"])
	file["path"].mkdir(exist_ok=True, parents=True)

	direct_download_link = __scrape_direct_download_link(file["download_link"])
	with requests.get(direct_download_link, stream=True) as response:
		with (file["path"] / file["filename"]).open("wb") as f:
			for chunk in response.iter_content(chunk_size=8192):
				if chunk:
					f.write(chunk)

	print(f"File '{file['download_link']}' downloaded!")