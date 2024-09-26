import argparse
import pathlib
from mediafire_downloader import get_folder_key, get_folder_content


argument_parser = argparse.ArgumentParser(description="Download entire folders from mediafire")
argument_parser.add_argument("folder_url", type=str, help="the url of the folder to download")
argument_parser.add_argument(
	"-d", "--destination",
	type=pathlib.Path,
	default="./downloads/",
	help="the path where files will be downloaded"
)

args = argument_parser.parse_args()

folder_url: str = args.folder_url
destination: pathlib.Path = args.destination

if not destination.exists():
	try:
		destination.mkdir(parents=True)
	
	except Exception as e:
		print(f"Failed to create destination directory '{destination}': {e}")


folder_key = get_folder_key(folder_url)
folder_content = get_folder_content(folder_key)
