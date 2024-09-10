from abc import ABC, abstractmethod
import os 

class Uploader(ABC):
    def upload(self):
        pass
    
class Telegram(Uploader):
    def upload(self):
      pass  


