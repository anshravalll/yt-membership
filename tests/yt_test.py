from abc import ABC
import subprocess
import threading

class Uploader(ABC):
    def upload(self):
        raise NotImplementedError
    
class Telegram(Uploader):
    def upload(self):
        subprocess.run(["telegram-upload", r"C:\Users\Ansh\Pictures\Saved Pictures\tranqx_droga_zombie.jpg_242310155-2799045096.jpg"])

    def file_to_upload(self):
        pass




