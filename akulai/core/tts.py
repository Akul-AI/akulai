import subprocess

class TTS:
    def __init__(self):
        pass
    
    def speak(self, text):
        subprocess.run(["espeak", "-s", "120", "-v", "en-us", text])
