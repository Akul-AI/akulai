
import os
import threading
import vosk
import pyaudio
import js2py
import json
import pyttsx3


class AkulAI:
    def __init__(self):
        # Initialize the VOSK speech to text engine
        self.model = vosk.Model(os.path.join("model", "vosk_model"))
        self.recognizer = vosk.KaldiRecognizer(self.model, 16000)
        # Initialize the pyaudio device
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
        # Create the listening thread
        self.stop_listening = threading.Event()
        self.listening_thread = threading.Thread(target=self.listen)
        self.listening_thread.start()
        # Initialize the pyttsx3 speech engine
        self.engine = pyttsx3.init()
        self.voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', self.voices[0].id)
        # Create plugins dictionary
        self.plugins = {}
        self.discover_plugins()

    # Looks for subdirectories in the plugin directory, and scans them for the file types py, js, and pl
    def discover_plugins(self):
        for root, dirs, files in os.walk("plugins"):
            for file in files:
                if file == "main.py":
                    plugin_name = os.path.splitext(file)[0]
                    extension = os.path.splitext(file)[1]
                    self.check_info(root, plugin_name, extension)
                    self.plugins[plugin_name] = {"handle": self.load_plugin(os.path.join(root, file)),
                                                 "extension": ".py"}
                elif file == "main.js":
                    plugin_name = os.path.splitext(file)[0]
                    self.check_info(root, plugin_name, extension)
                    self.plugins[plugin_name] = {"handle": self.load_plugin(os.path.join(root, file)),
                                                 "extension": ".js"}
                elif file == "main.pl":
                    plugin_name = os.path.splitext(file)[0]
                    self.check_info(root, plugin_name, extension)
                    self.plugins[plugin_name] = {"handle": self.load_plugin(os.path.join(root, file)),
                                                 "extension": ".pl"}

    # Checks for the plugin.info file and installs any required dependencies.
    def check_info(self, root, plugin_name, extension):
        info_file = os.path.join(root, plugin_name, 'plugin.info')
        if os.path.isfile(info_file):
            with open(info_file) as f:
                lines = f.readlines()
                for line in lines:
                    if 'dependencies' in line:
                        dependencies = line.split(':')[1].strip()
                        if dependencies:
                            if extension == ".py":
                                try:
                                    os.system(f"pip install {dependencies}")
                                except Exception as e:
                                    print(f"Error log:{e}")
                            elif extension == ".js":
                                try:
                                    os.system(f"npm install {dependencies}")
                                except Exception as e:
                                    print(f"Error log:{e}")
                            elif extension == ".pl":
                                try:
                                    os.system(f"cpanm {dependencies}")
                                except Exception as e:
                                    print(f"Error log:{e}")
                            print(f"{plugin_name} has the following dependencies: {dependencies}")
                        else:
                            print(f"{plugin_name} has no dependencies.")
                    elif 'author' in line:
                        author = line.split(':')[1].strip()
                        print(f"{plugin_name} was written by: {author}")
                    elif 'description' in line:
                        description = line.split(':')[1].strip()
                        print(f"Plugin Description: {description}")

    # Loads the plugins
    def load_plugin(self, file):
        with open(file, "r") as f:
            return f.read()

    # Listen for audio input through mic with pyaudio and vosk
    def listen(self):
        while not self.stop_listening.is_set():
            data = self.stream.read(16000, exception_on_overflow=False)
            if len(data) == 0:
                break
            if self.recognizer.AcceptWaveform(data):
                result = json.loads(self.recognizer.Result())
                if 'text' in result:
                    print(f"You said: {result['text']}")
                    if any([shutdown_command for shutdown_command in ['exit', 'quit', 'stop', 'shut down'] if shutdown_command in result['text']]):
                        self.speak("Okay, exiting")
                        self.stop()
                    else:
                        self.process_command(result['text'])

    # Processes given command and scans the plugins for one that can complete the command.
    # If none are found, give error and listen for next command.
    def process_command(self, command):
        for plugin_name in self.plugins:
            if plugin_name in command:
                try:
                    plugin_module = self.plugins[plugin_name]
                    if plugin_module["extension"] == '.py':
                        plugin_module["handle"](self, command)
                    elif plugin_module["extension"] == '.js':
                        js2py.eval_js(f'''
                            const akulAI = {self};
                            {plugin_module["handle"]}
                        ''')
                    elif plugin_module["extension"] == '.pl':
                        os.system(f"perl plugins/{plugin_name}.pl", self, command)
                except Exception as e:
                    self.speak(f"An error occurred while running the command you asked for. Here is the full exception: {e}")
                    raise
                return
        self.speak("I'm sorry, I didn't understand that command.")

    def speak(self, text):
        print(f"AkulAI said: {text}")
        self.engine.say(text)
        self.engine.runAndWait()

    # Shuts down the program and all threads + other operations it is running
    def stop(self):
        self.stop_listening.set()
        self.listening_thread.join()
        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()
        exit()


if __name__ == "__main__":
    akulai = AkulAI()
    print("say something")

    
    
    
    
#!/usr/bin/env python3
# -*- coding: utf-8 -*-   
import os
import vosk
import pyttsx3
import pyaudio
import importlib.util

class AkulAI:
    def __init__(self):
        # Initialize the VOSK speech to text engine
        self.model = vosk.Model(os.path.join("model", "vosk_model"))
        self.recognizer = vosk.KaldiRecognizer(self.model, 16000)
        # Initialize the pyaudio device
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
        # Create the listening thread
        self.stop_listening = threading.Event()
        self.listening_thread = threading.Thread(target=self.listen)
        self.listening_thread.start()
        # Initialize the pyttsx3 speech engine
        self.engine = pyttsx3.init()
        self.voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', self.voices[0].id)
        
    def speak(self, text):
        print(f"AkulAI said: {text}")
        self.engine.say(text)
        self.engine.runAndWait()

    # Discover and load all plugins
    self.plugins = []
    for dirpath, dirnames, filenames in os.walk("plugins"):
        for filename in filenames:
            if filename.endswith(".py"):
                # Load the Python plugin using importlib
                plugin_path = os.path.join(dirpath, filename)
                spec = importlib.util.spec_from_file_location("plugin", plugin_path)
                plugin = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(plugin)

                # Add the plugin to the list
                self.plugins.append(plugin)

            elif filename.endswith(".pl"):
                # Load the Perl plugin using subprocess
                plugin_path = os.path.join(dirpath, filename)
                import subprocess
                result = subprocess.check_output(['perl', plugin_path])
                plugin = result.decode('utf-8').strip()

                # Add the plugin to the list
                self.plugins.append(plugin)

            elif filename.endswith(".js"):
                # Load the JavaScript plugin using subprocess
                plugin_path = os.path.join(dirpath, filename)
                import subprocess
                result = subprocess.check_output(['node', plugin_path])
                plugin = result.decode('utf-8').strip()

                # Add the plugin to the list
                self.plugins.append(plugin)

            else:
                # Unsupported file extension
                continue

    # Listen for audio input through mic with pyaudio and vosk
    def listen(self):
        while not self.stop_listening.is_set():
            data = self.stream.read(16000, exception_on_overflow=False)
            if len(data) == 0:
                break
            if self.recognizer.AcceptWaveform(data):
                result = json.loads(self.recognizer.Result())
                if 'text' in result:
                    print(f"You said: {result['text']}")
                    if any([shutdown_command for shutdown_command in ['exit', 'quit', 'stop', 'shut down'] if shutdown_command in result['text']]):
                        self.speak("Okay, exiting")
                        self.stop()
                    else:
                        self.process_command(result['text'])

    def execute_command(self, command):
        for plugin in self.plugins:
            try:
                response = plugin.execute(command)

                if response:
                    self.speak(response)
                    return

            except Exception as e:
                print(f"Plugin execution failed: {e}")

        self.speak("Sorry, I didn't understand that.")

    def start(self):
        self.speak("Hello, I am AkulAI. How can I help you today?")

        while True:
            command = self.get_command()
            self.execute_command(command)
