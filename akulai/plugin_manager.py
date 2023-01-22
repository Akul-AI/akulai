import os
import subprocess

class PluginManager:
    def __init__(self):
        self.plugins = {}
        self.discover_plugins()

    # Looks for subdirs in the plugin directory, and scans them for the file types py, js, and pl
    def discover_plugins(self):
        for root, files in os.walk("plugins"):
            extension = os.path.splitext(file)[1]
            for file in files:
                if file.endswith(".py"):
                    plugin_name = os.path.splitext(file)[0]
                    extension = os.path.splitext(file)[1]
                    self.check_info(root, plugin_name, extension)
                    self.plugins[plugin_name] = {"handle": self.load_plugin(os.path.join(root, file), extension), "extension": ".py"}
                elif file.endswith(".js"):
                    plugin_name = os.path.splitext(file)[0]
                    self.check_info(root, plugin_name, extension)
                    self.plugins[plugin_name] = {"handle": self.load_plugin(os.path.join(root, file)), "extension": ".js"}
                elif file.endswith(".pl"):
                    plugin_name = os.path.splitext(file)[0]
                    self.check_info(root, plugin_name, extension)
                    self.plugins[plugin_name] = {"handle": self.load_plugin(os.path.join(root, file)), "extension": ".pl"}

    # Checks for the plugin.info file and installs any required dependencies based on on what file type the plugin was made with
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
                                subprocess.run(["pip", "install", dependencies])
                            elif extension == ".js":
                                subprocess.run(["npm", "install", dependencies])
                            elif extension == ".pl":
                                subprocess.run(["cpanm", dependencies])
                            print(f"{plugin_name} has the following dependencies: {dependencies}")
                    else:
                        print(f"{plugin_name} has no dependencies.")
        elif 'author' in line:
            author = line.split(':')[1].strip()
            print(f"{plugin_name} was written by: {author}")

    # Loads the plugins
    def load_plugin(self, file):
        with open(file, "r") as f:
            return f.read()
