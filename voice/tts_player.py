import pyttsx3
import threading


class TTSPlayer:
    def __init__(self):
        self.voice_id = None
        self.rate = 165
        self.volume = 1.0

        # Detect female voice ONCE
        engine = pyttsx3.init()
        voices = engine.getProperty("voices")

        for v in voices:
            name = v.name.lower()
            if "zira" in name or "female" in name or "woman" in name:
                self.voice_id = v.id
                break

        engine.stop()

    def speak(self, text):
        threading.Thread(
            target=self._speak_once,
            args=(text,),
            daemon=True
        ).start()

    def _speak_once(self, text):
        engine = pyttsx3.init()

        if self.voice_id:
            engine.setProperty("voice", self.voice_id)

        engine.setProperty("rate", self.rate)
        engine.setProperty("volume", self.volume)

        engine.say(text)
        engine.runAndWait()
        engine.stop()
