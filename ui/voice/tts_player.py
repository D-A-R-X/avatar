import pyttsx3
from PySide6.QtCore import QObject, Slot


class TTSPlayer(QObject):
    def __init__(self):
        super().__init__()
        self.engine = pyttsx3.init()
        self.engine.setProperty("rate", 165)   # speech speed
        self.engine.setProperty("volume", 1.0)

    @Slot(str)
    def speak(self, text: str):
        if not text:
            return
        self.engine.say(text)
        self.engine.runAndWait()
