import os
import threading
import time

# Try importing speech recognition safely
try:
    import speech_recognition as sr
except ImportError:
    sr = None


class MicListener:
    """
    Safe microphone listener.
    - Disabled automatically in Codespaces
    - Disabled if PyAudio is missing
    - Enabled only on real desktop systems
    """

    def __init__(self, on_text_callback=None):
        self.on_text_callback = on_text_callback
        self.enabled = False
        self.listening = False
        self.thread = None

        # Hard disable in Codespaces
        if os.environ.get("CODESPACES") == "true":
            print("🎙️ Mic disabled (Codespaces environment)")
            return

        if sr is None:
            print("🎙️ Mic disabled (SpeechRecognition not installed)")
            return

        # Try initializing recognizer + mic
        try:
            self.recognizer = sr.Recognizer()
            self.microphone = sr.Microphone()
            self.enabled = True
            print("🎙️ Mic initialized successfully")
        except Exception as e:
            print(f"🎙️ Mic disabled (audio backend error): {e}")
            self.enabled = False

    # ----------------------------
    # Public controls
    # ----------------------------

    def start(self):
        """Start listening in background thread"""
        if not self.enabled or self.listening:
            return

        self.listening = True
        self.thread = threading.Thread(target=self._listen_loop, daemon=True)
        self.thread.start()
        print("🎙️ Mic listening started")

    def stop(self):
        """Stop listening"""
        self.listening = False
        print("🎙️ Mic listening stopped")

    # ----------------------------
    # Internal loop
    # ----------------------------

    def _listen_loop(self):
        while self.listening:
            try:
                with self.microphone as source:
                    self.recognizer.adjust_for_ambient_noise(source, duration=0.3)
                    audio = self.recognizer.listen(
                        source,
                        timeout=3,
                        phrase_time_limit=5
                    )

                text = self.recognizer.recognize_google(audio)
                print(f"🎧 Heard: {text}")

                if self.on_text_callback:
                    self.on_text_callback(text)

            except sr.WaitTimeoutError:
                pass  # normal
            except sr.UnknownValueError:
                pass  # speech not clear
            except Exception as e:
                print(f"🎙️ Mic error: {e}")
                time.sleep(1)
