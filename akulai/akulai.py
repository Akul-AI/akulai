import os
import threading
import vosk
import pyaudio
import espeakng
import PyNodeJS

class AkulAI:
    def __init__(self):
        self.stop_listening = threading.Event()
        self.listening_thread = threading.Thread(target=self.listen)
        self.listening_thread.start()
        self.plugins = {}
        self.discover_plugins()
        self.model = vosk.Model("./vosk-model")
        self.recognizer = vosk.KaldiRecognizer(self.model, sample_rate=16000)
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)

    def discover_plugins(self):
        for file in os.listdir("plugins"):
            if file.endswith(".py"):
                plugin_name = os.path.splitext(file)[0]
                extension = os.path.splitext(file)[1]
                self.plugins[plugin_name] = {"handle": self.load_plugin(file, extension), "extension": ".py"}
            elif file.endswith(".js"):
                plugin_name = os.path.splitext(file)[0]
                self.plugins[plugin_name] = {"handle": self.load_plugin(file), "extension": ".js"}

    def load_plugin(self, file):
        with open(f"plugins/{file}", "r") as f:
            return f.read()

    def listen(self):
        while not self.stop_listening.is_set():
            data = self.stream.read(self.recognizer.sample_rate, exception_on_overflow = False)
            if len(data) == 0:
                break
            if self.recognizer.AcceptWaveform(data):
                result = self.recognizer.Result()
                self.process_command(result)
       
    def process_command(self, command):
        for plugin_name in self.plugins:
            if plugin_name in command:
                try:
                    plugin_module = self.plugins[plugin_name]
                    if plugin_module["extension"]=='.py':
                        plugin_module["handle"](self,command)
                    elif plugin_module["extension"]=='.js':
                        PyNodeJS.execute_js(f'''
                            const akulAI = {self};
                            {plugin_module["handle"]}
                        ''')
                except Exception as e:
                    self.speak(f"An error occurred while running the plugin {plugin_name}: {str(e)}")
                    raise
                return
        self.speak("I'm sorry, I didn't understand that command.")

    def speak(self,text):
        aispeaker = espeakng.speaker()
        aispeaker.say(text)

    def stop(self):
        self.stop_listening.set()
        self.listening_thread.join()
        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()
        
akulai = AkulAI()
