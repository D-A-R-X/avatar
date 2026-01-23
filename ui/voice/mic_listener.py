import threading
import speech_recognition as sr
import time
from voice.stt_listener import STTListener


class MicListener:
    def __init__(self, on_text_callback):
        self.on_text_callback = on_text_callback
        self.stt = STTListener()

        self.listening = False
        self.thread = None
        self.lock = threading.Lock()

    def start(self):
        with self.lock:
            if self.listening:
                return
            self.listening = True

        print("🎤 MIC ON")

        self.thread = threading.Thread(
            target=self._listen_loop,
            daemon=True
        )
        self.thread.start()

    def stop(self):
        with self.lock:
            if not self.listening:
                return
            self.listening = False

        print("🔇 MIC OFF")
        time.sleep(0.2)

    def _listen_loop(self):
        recognizer = sr.Recognizer()

        try:
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source)

                while True:
                    with self.lock:
                        if not self.listening:
                            break

                    try:
                        audio = recognizer.listen(
                            source,
                            timeout=5,
                            phrase_time_limit=6
                        )

                        text = self.stt.audio_to_text(audio)
                        if text:
                            print("VOICE:", text)
                            self.on_text_callback(text)

                    except sr.WaitTimeoutError:
                        continue
                    except sr.UnknownValueError:
                        continue

        except Exception as e:
            print("MIC ERROR:", e)
