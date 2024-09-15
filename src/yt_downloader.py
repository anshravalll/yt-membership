import threading
from yt_dlp import DownloadError, YoutubeDL
import sys
from pathlib import Path
import threading

project_root = Path(__file__).resolve().parent.parent  # Go up two levels to project_root
sys.path.insert(0, str(project_root))

from tests.yt_test import Telegram


class Downloader():
    def __init__(self, opts, id):
        url = self.default_url(id)
        if opts.get('cookiefile', None) or opts.get('cookiesfrombrowser', None):
            self.with_cookies(opts, url)
        else:
            self.plain_login(opts, url)

    def plain_login(self, opts, url):
        opts['username'] = input("Type your email:")
        opts['password'] = input("Type your password:")
        with YoutubeDL(opts) as ydl:
            ydl.download(url)

    def default_url(self, id):
        default_url = 'https://www.youtube.com/playlist?list='
        updated_url = default_url + 'UUMO' + id[2:] #Playlist for all membership videos for a channel
        return updated_url

    def with_cookies(self, opts, url):
        lock = threading.Lock()
        with YoutubeDL(opts) as ydl:
            while True:
                    try:
                        ydl.download(url)
                    except DownloadError:
                        return


if __name__ == "__main__":
    opts = {
            'cookiefile': r"C:\Users\Ansh\Desktop\coding\yt-membership\tests\cookies.txt",
        #'cookiesfrombrowser': ('firefox', 'C:/Users/Ansh/AppData/Local/Packages/Mozilla.Firefox_n80bbvh6b1yt2/LocalCache/Roaming/Mozilla/Firefox/Profiles/422oklgq.default-release'),

            'outtmpl': {
                'default': 'D:/Youtube/%(channel)s/%(playlist)s/Videos/%(title)s.%(ext)s',  # Video files
                'thumbnail': 'D:/Youtube/%(channel)s/%(playlist)s/Thumbnails/%(title)s.%(ext)s',  # Thumbnails
                'subtitle': 'D:/Youtube/%(channel)s/%(playlist)s/Subtitles/%(title)s.%(ext)s',  # Subtitles
                'description': 'D:/Youtube/%(channel)s/%(playlist)s/Description/%(title)s.%(ext)s',  # Description
                'infojson': 'D:/Youtube/%(channel)s/%(playlist)s/InfoJSON/%(title)s.%(ext)s',  # Info JSON
},
            'verbose': True,

            'sleep_interval': 5,
            'max_sleep_interval': 30,
            'sleep_requests': 1,

            # Error Handling
            #'ignoreerrors': True,
            'noprogress': True,

            # File Handling
            'nopart': False,  # Start fresh, do not continue downloads
            'overwrite': False,  # Prevent overwriting of existing files
            'download_archive': 'archive.log',  # Log downloaded videos to avoid re-downloading

            # Fragment Handling
            'concurrent_fragment_downloads': 3,


            'writedescription': True,  # Write video description to file
            'writeinfojson': True,  # Write video info JSON to file
            'writethumbnail': True,  # Write thumbnail image to file
            'writesubtitles': True,  # Allow writing subtitles
            'writeautomaticsub': True,
            'allsubs': True,  # Download all subtitles
            }

    id = 'UCfQgsKhHjSyRLOp9mnffqVg' #channel id

    #Downloader(opts, id)
    telegram_upload = Telegram()

    thread1 = threading.Thread(target = Downloader, args = (opts, id), daemon = True)
    thread2 = threading.Thread(target = telegram_upload.upload, daemon= True)
    thread1.start()
    thread2.start()



