from core.tts import TTS
from core.stt import STT
from plugin_manager import PluginManager
import pynodejs
import subprocess

class AkulAI:
    def __init__(self):
        self.tts = TTS()
        self.stt = STT()
        self.plugins = PluginManager()

    def process_command(self, command):
        for plugin_name in self.plugins:
            if plugin_name in command:
                try:
                    plugin_module = self.plugins[plugin_name]
                    if plugin_module["extension"]=='.py':
                        plugin_module["handle"](self,command)
                    elif plugin_module["extension"]=='.js':
                        pynodejs.execute_js(f'''
                            const akulAI = {self};
                            {plugin_module["handle"]}
                        ''')
                    elif plugin_module["extension"]=='.pl':
                        subprocess.run(["perl", f"plugins/{plugin_name}.pl", self, command])
                except Exception as e:
                    self.tts(f"An error occurred while running the plugin {plugin_name}: {str(e)}")
                    raise
                return
        self.tts("I'm sorry, I didn't understand that command.")
        if command.lower() == "stop listening":
            self.stt.stop()
            self.tts.speak("Stopping listening")
            return

if __name__ == "__main__":
    ai = AkulAI()
    while True:
        command = input("Say something: ")
        ai.process_command(command)