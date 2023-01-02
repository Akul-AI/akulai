# AkulAI Core

This is the very first version of the AkulAI project. This is very basic, but I definetly plan on adding other things as well. I will update from time to time, but as a solo developer (during the time of writing), please don't expect a lot.

(This does open up a WebUI which probably won't be supported in other versions.)

Please share this and contribute to it, I would love to get some help.

This is an example of how to make a very simple skill.

``` python
from dataclasses import dataclass
from skills import factory
from core.ai import AI

@dataclass
class Insults_skill:
    name = 'insults'
    
    def commands(self, command:str):
        return ['insult me', 'tell me an insult', 'give me an insult', 'roast me']
        
    def handle_command(self, command:str, ai:AI):
       ai.say('you are a worm')

def initialize():
    factory.register('insult_skill', Insult_skill)
```

3. Update the `skills.json` file to include the new skill:

``` json
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
```


Reload the AI and test out your new skill!
