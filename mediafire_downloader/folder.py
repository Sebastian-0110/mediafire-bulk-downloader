

class Folder(object):
	""" Folder class to model mediafire folder structure """

	def __init__(self, name: str) -> None:
		""" Init method """

		self.name = name or "folder"
		self.files = []
		self.folders: list[Folder] = []

	def add_files(self, files: list[dict]) -> None:
		""" Add files to the folder """

		self.files.extend(files)

	def add_folders(self, folders: list["Folder"]) -> None:
		""" Add inner folders to the folder """

		self.folders.extend(folders)


	def __str__(self) -> str:
		return f"Folder ({self.name}): files: {self.files}, content: {self.folders}"
	
	def __repr__(self) -> str:
		return f"Folder ({self.name}): files: {self.files}, content: {self.folders}"