import argparse
import pathlib

from concurrent.futures import ThreadPoolExecutor
from itertools import repeat

from mediafire_downloader import (
	is_valid,
	get_folder_key,
	get_folder_content,
	download_file
)

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

if not is_valid(folder_url):
	print("The url is not a valid mediafire folder link")
	exit()

if not destination.exists():
	try:
		destination.mkdir(parents=True)
	
	except Exception as e:
		print(f"Failed to create destination directory '{destination}': {e}")
		exit()

folder_key = get_folder_key(folder_url)

print("Getting folder content...")
folder_files = get_folder_content(folder_key)

print("Downloading files...")
with ThreadPoolExecutor(max_workers=5) as executor:
	executor.map(download_file, folder_files, repeat(destination))

print("Job done!")
