import re

URL_VALIDATION_REGEX = re.compile(
	r"https:\/\/www\.mediafire\.com\/folder\/[a-zA-Z0-9]+(\/.+)?\/?",
	re.IGNORECASE
)