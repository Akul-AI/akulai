#!/usr/bin/env python3
# -*- coding: utf-8 -*-   
import importlib.util
import json
import os
import pyttsx3
import pyaudio
import subprocess
import threading
import vosk
import sys
from fastapi import FastAPI
import webbrowser


class JSPlugin:
    def __init__(self, plugin_path):
        self.plugin_path = plugin_path
        
    def handle(self, command):
        return subprocess.check_output(['node', self.plugin_path, json.dumps(command)]).decode('utf-8').strip()

class PerlPlugin:
    def __init__(self, plugin_path):
        self.plugin_path = plugin_path
        
    def handle(self, command):
        return subprocess.check_output(['perl', self.plugin_path, json.dumps(command)]).decode('utf-8').strip()


class AkulAI:
    def __init__(self):
        # Initialize the VOSK speech to text engine
        self.model = vosk.Model(os.path.join("model", "vosk_model"))
        self.recognizer = vosk.KaldiRecognizer(self.model, 16000)
        # Initialize the pyaudio device
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
        # Initialize the pyttsx3 speech engine
        self.engine = pyttsx3.init()
        self.voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', self.voices[0].id)
        # load the plugins
        self.discover_plugins()
        
    def speak(self, text):
        print(f"AkulAI said: {text}")
        self.engine.say(text)
        self.engine.runAndWait()

    # Discover and load all plugins
    def discover_plugins(self):
        self.plugins = []
        for dirpath, dirnames, filenames in os.walk("plugins"):
            for filename in filenames:
                if filename in ("main.py", "main.js", "main.pl"):
                    if filename.endswith(".py"):
                        # Load the Python plugin using importlib
                        plugin_path = os.path.join(dirpath, filename)
                        spec = importlib.util.spec_from_file_location("plugin", plugin_path)
                        plugin = importlib.util.module_from_spec(spec)
                        spec.loader.exec_module(plugin)

                        # Add the plugin to the list
                        self.plugins.append(plugin)
                        print(f"Loaded plugin from {plugin_path}")

                    elif filename.endswith(".pl"):
                        # Load the Perl plugin using subprocess
                        try:
                            plugin_path = os.path.join(dirpath, filename)
                            self.plugins.append(PerlPlugin(plugin_path))

                            # Add the plugin to the list
                            print(f"Loaded perl plugin: {plugin_path}")
                        except subprocess.CalledProcessError:
                            print(f"Error loading perl plugin: {plugin_path}")

                    elif filename.endswith(".js"):
                        # Load the JavaScript plugin using subprocess
                        try:
                            plugin_path = os.path.join(dirpath, filename)
                            self.plugins.append(JSPlugin(plugin_path))

                            # Add the plugin to the list
                            print(f"Loaded node plugin: {plugin_path}")
                        except subprocess.CalledProcessError:
                            print(f"Error loading node plugin: {plugin_path}")

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
                        self.execute_command(result['text'])

    def execute_command(self, command):
        handled = False
        for plugin in self.plugins:
            try:
                response = plugin.handle(command)
                
                if response:
                    self.speak(response)
                    handled = True

            except Exception as e:
                print(f"Plugin execution failed: {e}")

        if(not handled):
            self.speak("Sorry, I didn't understand that.")

    # shut down the program and all threads
    def stop(self):
        self.stop_listening.set()
        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()
        sys.exit()

# Set up API
app = FastAPI()
akulai = AkulAI()

if __name__ == '__main__':
    # Create the listening thread
    self.stop_listening = threading.Event()
    self.listening_thread = threading.Thread(target=self.listen)
    self.listening_thread.start()

   @app.get("/speak/{text}")
    async def speak(text: str):
        akulai.speak(text)
        return {"message": "Text synthesized"}

    @app.post("/listen")
    async def listen():
        akulai.listen()
        return {"message": "Listening..."}
    
    # Run the server for the API
    os.system("uvicorn akulai:app --reload")
    webbrowser.open("http://127.0.0.1:8000")
    akulai.speak("Hello, I am AkulAI. How can I help you today?")
