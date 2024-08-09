from yt_dlp import YoutubeDL

class Downloader():
    def __init__(self, opts, id):
        default_url = 'https://www.youtube.com/playlist?list='
        updated_url = default_url + 'UUMO' + id[2:]

        with YoutubeDL(opts) as ydl:
            ydl.download(updated_url)

        

if __name__ == "__main__":
    opts = {'cookiefile': r"C:\Users\Ansh\Desktop\coding\yt-membership\tests\cookies.txt",

            'outtmpl': {
                'default': 'D:/Youtube/%(channel)s/%(playlist)s/Videos/%(title)s.%(ext)s',  # Video files
                'thumbnail': 'D:/Youtube/%(channel)s/%(playlist)s/Thumbnails/%(title)s.%(ext)s',  # Thumbnails
                'subtitle': 'D:/Youtube/%(channel)s/%(playlist)s/Subtitles/%(title)s.%(ext)s',  # Subtitles
                'description': 'D:/Youtube/%(channel)s/%(playlist)s/Description/%(title)s.%(ext)s',  # Description
                'infojson': 'D:/Youtube/%(channel)s/%(playlist)s/InfoJSON/%(title)s.%(ext)s',  # Info JSON
},

            'sleep_interval': 5,
            'max_sleep_interval': 30,
            'sleep_requests': 1,

            # Error Handling
            'ignoreerrors': True,
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
    id = 'UCfQgsKhHjSyRLOp9mnffqVg'
    Downloader(opts, id)


