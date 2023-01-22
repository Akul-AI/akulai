import os
import threading
import vosk
import pyaudio

class STT:
    def __init__(self):
        self.stop_listening = threading.Event()
        self.listening_thread = threading.Thread(target=self.listen)
        self.listening_thread.start()
        self.model = vosk.Model("vosk_model")
        self.recognizer = vosk.KaldiRecognizer(self.model, rate=16000)
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)

    def listen(self):
        while not self.stop_listening.is_set():
            data = self.stream.read(self.recognizer.rate, exception_on_overflow = False)
            if len(data) == 0:
                break
            if self.recognizer.AcceptWaveform(data):
                result = self.recognizer.Result()
                return result

    def stop(self):
        self.stop_listening.set()
