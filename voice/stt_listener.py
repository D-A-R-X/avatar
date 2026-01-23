import speech_recognition as sr
from PySide6.QtCore import QObject, Signal, QThread


class STTWorker(QThread):
    voice_text = Signal(str)
    error = Signal(str)

    def __init__(self):
        super().__init__()
        self.running = False
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()

    def run(self):
        try:
            with self.microphone as source:
                self.recognizer.adjust_for_ambient_noise(source)
        except Exception as e:
            self.error.emit(str(e))
            return

        self.running = True

        while self.running:
            try:
                with self.microphone as source:
                    audio = self.recognizer.listen(source)

                text = self.recognizer.recognize_google(audio)
                self.voice_text.emit(text)

            except sr.UnknownValueError:
                pass
            except Exception as e:
                self.error.emit(str(e))

    def stop(self):
        self.running = False


class STTListener(QObject):
    voice_text = Signal(str)
    error = Signal(str)

    def __init__(self):
        super().__init__()
        self.worker = STTWorker()
        self.worker.voice_text.connect(self.voice_text)
        self.worker.error.connect(self.error)

    def start_listening(self):
        if not self.worker.isRunning():
            self.worker.start()

    def stop_listening(self):
        if self.worker.isRunning():
            self.worker.stop()
