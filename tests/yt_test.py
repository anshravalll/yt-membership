from abc import ABC
import subprocess
import threading

class Uploader(ABC):
    def upload(self):
        pass
    
class Telegram(Uploader):
    def upload(self):
        lock = threading.Lock()
        subprocess.run(["telegram-upload", r"C:\Users\Ansh\Pictures\Saved Pictures\tranqx_droga_zombie.jpg_242310155-2799045096.jpg"])





