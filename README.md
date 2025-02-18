# yt-membership

**yt-membership** is a Python-based tool designed to simultaneously download and upload all member-exclusive videos from YouTube. This tool leverages the `yt-dlp` library to manage video downloads and supports various output configurations including video files, thumbnails, subtitles, descriptions, and JSON information.

> **Note**: This tool is currently under development and may undergo significant changes.

## Features

- **Simultaneous Download**: Supports concurrent downloads of YouTube membership videos, including thumbnails, subtitles, and descriptions.
- **Customizable Output**: Users can specify the output directory structure for videos, thumbnails, subtitles, descriptions, and JSON files.
- **Error Handling**: Built-in error handling to manage download interruptions and retries.
- **Flexible Integration**: Upload content to video hosting services automatically.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/anshravalll/yt-membership.git
   cd yt-membership
   ```

2. **Install Dependencies**:
   Install `yt-dlp` and other required Python packages:
   ```bash
   pip install yt-dlp
   ```

## Usage

1. **Set Up Your Configuration**:
   Update the `opts` dictionary in the script with your desired settings:
   - **Cookie File**: Specify the path to your YouTube cookies file to access member-exclusive content.
   - **Output Templates**: Configure where to save downloaded videos, thumbnails, subtitles, descriptions, and JSON files in a strucutred manner.
   - **InfoJson**: Get the information about each and every metadata and portion of the video.
   - **Error Handling and Download Options**: Customize sleep intervals, error handling, and concurrent downloads.

2. **Run the Script**:
   Execute the script with the desired YouTube channel ID:
   ```bash
   python yt-membership.py
   ```

3. **Example Configuration**:
   ```python
   opts = {
       'cookiefile': r"C:\Path\To\Your\cookies.txt",
       'cookiesfrombrowser': ('firefox', 'C:/Path/To/Your/Browser/Profile'),
       'outtmpl': {
           'default': 'D:/Youtube/%(channel)s/%(playlist)s/Videos/%(title)s.%(ext)s',
           'thumbnail': 'D:/Youtube/%(channel)s/%(playlist)s/Thumbnails/%(title)s.%(ext)s',
           'subtitle': 'D:/Youtube/%(channel)s/%(playlist)s/Subtitles/%(title)s.%(ext)s',
           'description': 'D:/Youtube/%(channel)s/%(playlist)s/Description/%(title)s.%(ext)s',
           'infojson': 'D:/Youtube/%(channel)s/%(playlist)s/InfoJSON/%(title)s.%(ext)s',
       },
       'verbose': True,
       'sleep_interval': 5,
       'max_sleep_interval': 30,
       'sleep_requests': 1,
       'noprogress': True,
       'nopart': False,
       'overwrite': False,
       'download_archive': 'archive.log',
       'concurrent_fragment_downloads': 3,
       'writedescription': True,
       'writeinfojson': True,
       'writethumbnail': True,
       'writesubtitles': True,
       'writeautomaticsub': True,
       'allsubs': True,
   }
   ```

## Contribution

I welcome contributions! Please fork the repository and create a pull request with your improvements. Thanks!!!




