# 🚀 Mediafire Bulk Downloader

[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/license-mit.svg)](https://forthebadge.com)

A Python-based tool that allows you to download entire folders from Mediafire **in bulk**. This downloader automates the process of fetching individual file download links from Mediafire folders and downloads multiple files simultaneously, supporting large folder structures with ease.

## ✨ Features

- 🗂️ **Download entire folders** from Mediafire, no premium account required.
- ⚡ **Concurrent downloads** (pending) using multithreading for faster performance.

## 🛠️ Requirements

- 🐍 Python 3.7+
- 📦 `requests`
- 🍲 `beautifulsoup4`

## 💻 Installation

First, clone this repository:

```bash
git clone https://github.com/your-username/mediafire-bulk-downloader.git

cd mediafire-bulk-downloader
```

Then install the required dependencies:

```bash
pip install -r requirements.txt
```

## 🚀  Usage

#### Example

```bash
python main.py "https://www.mediafire.com/folder/your_folder_link" -d ./downloads
```

#### Arguments

- 🌐 **`folder_url` (positional argument):** The Mediafire folder URL containing the files you want to download.

- 📂 **`--destination` or `-d` (optional argument):** The destination path where files will be saved (defaults to ./downloads).


## 📄 Licence
This project is licensed under the MIT License. See the [LICENSE](LICENCE) file for details

#

> **Disclaimer:** This tool is intended for educational purposes only. Please ensure you have the right to download any content and respect the terms of service of [Mediafire](https://mediafire.com/) or any other platforms you interact with.

