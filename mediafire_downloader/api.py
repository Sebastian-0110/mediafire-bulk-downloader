import requests
from typing import Literal

from .folder import Folder


BASE_API_URL = "https://www.mediafire.com/api/1.4/"

def __get_folder_content(folder_key: str, content_type: Literal["files", "folders"]) -> dict:
	""" Retrieve the folder data from the mediafire api """

	if content_type != "files" and content_type != "folders":
		raise ValueError("content_type must be either 'files' or 'folders'")

	params = {
		"response_format": "json",
		"folder_key": folder_key,
		"content_type": content_type,
		"chunk": 1,
	}

	result = []

	# TODO: Improve this by implementing a generator so we dont load all the files to memory
	while True:
		with requests.get(f"{BASE_API_URL}/folder/get_content.php", params=params) as response:
			json = response.json()["response"]["folder_content"]
			result.extend(json[content_type])

		if json["more_chunks"] == "no":
			break

		params["chunk"] += 1

	return result

def __clean_file_objects(files: list[dict]) -> list[dict]:
	""" Remove the usesless information that comes with the file data """

	return [
		{
			"filename": file["filename"],
			"download_link": file["links"]["normal_download"]
		} for file in files
	]


def get_folder_info(folder_key: str) -> dict:
	""" Get the folder info from the mediafire api """

	data = {
		'recursive': 'yes',
		'folder_key': folder_key,
		'response_format': 'json',
	}
	
	with requests.post(f"{BASE_API_URL}/folder/get_info.php?", data=data) as response:
		return response.json()["response"]["folder_info"]


def get_folder_content(folder_key: str) -> Folder:
	""" Get the folder content from the mediafire api """

	folder_name = get_folder_info(folder_key)["name"]
	root_folder = Folder(folder_name)

	files = __clean_file_objects(__get_folder_content(folder_key, "files"))
	root_folder.add_files(files)

	folders = __get_folder_content(folder_key, "folders")

	folder_objects: list[Folder] = []
	for folder in folders:
		# TODO: Keep an eye on this in case we start hitting the recursion limit, might refactor this
		folder_objects.append(get_folder_content(folder["folderkey"]))

	root_folder.add_folders(folder_objects)

	return root_folder
