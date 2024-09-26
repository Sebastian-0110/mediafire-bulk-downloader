import requests
import pathlib
from typing import Literal, Generator


BASE_API_URL = "https://www.mediafire.com/api/1.4/"

def __get_folder_content(
		folder_key: str,
		content_type: Literal["files", "folders"]
	) -> Generator[dict, None, None]:
	""" Retrieve the folder data from the mediafire api """

	if content_type != "files" and content_type != "folders":
		raise ValueError("content_type must be either 'files' or 'folders'")

	params = {
		"response_format": "json",
		"folder_key": folder_key,
		"content_type": content_type,
		"chunk": 1,
	}

	while True:
		with requests.get(f"{BASE_API_URL}/folder/get_content.php", params=params) as response:
			json = response.json()["response"]["folder_content"]
		
		for item in json[content_type]:
			yield item

		if json["more_chunks"] == "no":
			return

		params["chunk"] += 1

def get_folder_info(folder_key: str) -> dict:
	""" Get the folder info from the mediafire api """

	data = {
		'recursive': 'yes',
		'folder_key': folder_key,
		'response_format': 'json',
	}
	
	with requests.post(f"{BASE_API_URL}/folder/get_info.php?", data=data) as response:
		return response.json()["response"]["folder_info"]


def get_folder_content(folder_key: str, path: pathlib.Path = pathlib.Path("")) -> list[dict]:
	""" Get the folder content from the mediafire api """

	files: list[dict] = []
	folder_name: str = get_folder_info(folder_key)["name"]
	
	new_path = pathlib.Path(path, folder_name).resolve()

	for file in __get_folder_content(folder_key, "files"):
		files.append({
			"filename": file["filename"],
			"path": new_path,
			"download_link": file["links"]["normal_download"]
		})

	# NOTE: Might want to refactor this and get rid of recursion
	for folder in __get_folder_content(folder_key, "folders"):
		files.extend(get_folder_content(folder["folderkey"], new_path))

	return files