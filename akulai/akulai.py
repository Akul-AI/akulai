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
