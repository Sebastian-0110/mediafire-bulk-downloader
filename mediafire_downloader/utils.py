# Utility functions

import re


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


def get_folder_info(folder_key: str) -> dict:
	""" Get the folder info from the mediafire api """

	data = {
		'recursive': 'yes',
		'folder_key': folder_key,
		'response_format': 'json',
	}
	
	with requests.post(f"{BASE_API_URL}/folder/get_info.php?", data=data) as response:
		return response.json()["response"]["folder_info"]


def get_folder_content(folder_key: str) -> dict:
	""" Get the folder content from the mediafire api """

	folder_name = get_folder_info(folder_key)["name"]
	root_folder = Folder(folder_name)

	content_types = ["files", "folders"]

	for content_type in content_types:
		params = {
			"response_format": "json",
			"folder_key": folder_key,
			"content_type": content_type,
			"chunk": 1,
		}

		while True:
			with requests.get(f"{BASE_API_URL}/folder/get_content.php", params=params) as response:
				json = response.json()
			
			if content_type == "files":
				root_folder.add_files(json["response"]["folder_content"]["files"])

			elif content_type == "folders":
				folders_info = json["response"]["folder_content"]["folders"]

				folders = []
				for folder in folders_info:
					folders.append(get_folder_content(folder["folderkey"]))

				root_folder.add_folders(folders)

			if json["response"]["folder_content"]["more_chunks"] == "no":
				break

			params["chunk"] += 1

	return root_folder
