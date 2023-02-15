import importlib
import os
import inspect

class PluginAssistant:
    def __init__(self):
        self.plugins = {}

    def load_plugins(self):
        plugin_dir = "plugins"
        for folder in os.listdir(plugin_dir):
            path = os.path.join(plugin_dir, folder)
            if os.path.isdir(path):
                for file in os.listdir(path):
                    if file.endswith(".py"):
                        name = file[:-3]
                        module = importlib.import_module(f"{plugin_dir}.{folder}.{name}")
                        for member in inspect.getmembers(module, inspect.isfunction):
                            if member[1].__module__ == module.__name__:
                                command_name = f"{folder}.{member[0]}"
                                self.register_command(command_name, member[1])

    def register_command(self, name, func):
        self.plugins[name] = func

    def handle_command(self, text):
        for name, func in self.plugins.items():
            if name in text:
                command = name.split(".")[1]
                return func(command)
        return ""
