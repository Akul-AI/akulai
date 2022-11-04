# AkulAI V1

This is the very first version of the AkulAI project. This is very basic, but I definetly plan on adding other things as well. I will update from time to time, but make sure to look out for other repos with later version. This one will only contain bug fixes after this. 

To create your own skill, create a new file in the skills folder, and type in the followng code.
'''
from dataclasses import dataclass
from skills import factory
from core.ai import AI

@dataclass
class Insults_skill:   # This is an example, name it anything you want, with _skill after it
    name = 'insults_skill'
    
    def commands(self, command:str): # What ever the ai should listen to to respond
        return ['insult me', 'tell me an insult', 'give me an insult', 'roast me']
        
    def handle_command(self, command:str, ai:AI): # how should the ai respond
       ai.say('you are a worm')

def initialize():
    factory.register('insult_skill', Insult_skill) # registers the skill with the class name and what ever skill you put in there
'''

now update the skills.json file so it looks like this:
''' json
{
    "plugins": ["skills.goodday", "skills.weather", "skills.facts", "skills.jokes", "skills.calendar", "skills.insult"],
    "skills": [
        {
            "name": "weather_skill"
        },
        {
            "name": "facts_skill"
        },
        {
            "name": "jokes_skill"
        },
        {
            "name": "goodday_skill"
        },
        {
            "name": "calendar_skill"
        },
        {
            "name": "insult_skill"
        }
    ]
}
'''

Reload the AI and test out your new skill!
