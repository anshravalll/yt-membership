from abc import ABC
import subprocess

class Uploader(ABC):
    def upload(self):
        pass
    
class Telegram(Uploader):
    def upload(self):
        subprocess.run(["telegram-upload", r"C:\Users\Ansh\Pictures\Saved Pictures\tranqx_droga_zombie.jpg_242310155-2799045096.jpg"])

telegram_upload = Telegram().upload()




