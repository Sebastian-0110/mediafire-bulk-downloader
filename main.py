import argparse
import utils



argument_parser = argparse.ArgumentParser(description="Download entire folders from mediafire")
argument_parser.add_argument("folder_url", type=str, help="the url of the folder to download")

args = argument_parser.parse_args()



folder_url = args.folder_url

if not utils.is_valid(folder_url):
	print("The given url is not a valid mediafire folder url")
	exit()

folder_key = utils.get_folder_key(folder_url)

content = utils.get_folder_content(folder_key)

print(content.files)
print(content.folders)
