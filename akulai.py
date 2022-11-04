from core.ai import AI
from skills import factory, loader
from plugins import plugin_loader, plugin_factory
import json
from events.eventhook import Event_hook
import sys

akulai = AI()

# Setup events for plugins to attach to
akulai.start = Event_hook()
akulai.stop = Event_hook()

command = ""

# load the skills
with open("./skills/skills.json") as f:
    data = json.load(f)

    # load the plugins
    loader.load_skills(data["plugins"])

skills = [factory.create(item) for item in data["skills"]]
print(f'skills: {skills}')

# Load the plugins
with open("./plugins/plugins.json") as f:
    plugin_data = json.load(f)
    print(f'plugins: {plugin_data["plugins"]}')
    # load the plugins
    plugin_loader.load_plugins(plugin_data["plugins"])

plugins = [plugin_factory.create(item) for item in plugin_data["items"]]

# Register all the plugins
for item in plugins:
    item.register(akulai)

akulai.start.trigger()
akulai.say("Hello")
command = ""
while True and command not in ["good bye", 'bye', 'quit', 'exit','goodbye', 'the exit']:
    command = ""
    command = akulai.listen()
    if command:
        command = command.lower()
        print(f'command heard: {command}') 
        for skill in skills:
            if command in skill.commands(command):
                skill.handle_command(command, akulai)

akulai.say("Goodbye!")

# tell the plugins the server is shutting down
print('telling triggers to stop')
akulai.stop.trigger()
print('telling ai to stop')
akulai.stop_ai()
print('deleting ai')
del(akulai)
print('done')

