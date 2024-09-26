

class Folder(object):
	""" Folder class to model mediafire folder structure """

	def __init__(self, name: str) -> None:
		""" Init method """

		self.name = name or "folder"
		self.files = []
		self.folders: list[Folder] = []

	def add_file(self, file: dict) -> None:
		""" Add a file to the folder """

		self.files.append(file)

	def add_folder(self, folder: "Folder") -> None:
		""" Add a child folder to the folder """

		self.folders.append(folder)


	def __str__(self) -> str:
		return f"Folder '{self.name}': files({len(self.files)}), folders({len(self.folders)}): {self.folders}"
	
	def __repr__(self) -> str:
		return f"Folder '{self.name}': files({len(self.files)}), folders({len(self.folders)}): {self.folders}"
