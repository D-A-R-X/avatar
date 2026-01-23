from PySide6.QtCore import QObject, QThread, Signal
import speech_recognition as sr


class MicWorker(QObject):
    text_detected = Signal(str)

    def __init__(self):
        super().__init__()
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        self.stopper = None

    def start_listening(self):
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source)

        self.stopper = self.recognizer.listen_in_background(
            self.microphone,
            self._callback
        )

    def stop_listening(self):
        if self.stopper:
            self.stopper(wait_for_stop=False)
            self.stopper = None

    def _callback(self, recognizer, audio):
        try:
            text = recognizer.recognize_google(audio)
            self.text_detected.emit(text)
        except Exception:
            pass


class MicListener(QObject):
    text_ready = Signal(str)

    def __init__(self):
        super().__init__()

        self.thread = QThread()
        self.worker = MicWorker()
        self.worker.moveToThread(self.thread)

        self.worker.text_detected.connect(self.text_ready)

        self.thread.start()

    def start(self):
        self.worker.start_listening()

    def stop(self):
        self.worker.stop_listening()
