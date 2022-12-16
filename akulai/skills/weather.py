from dataclasses import dataclass
from skills import factory
from core.ai import AI

# get weather from google so we dont have to rely on any apis, may change this in the future
import requests
from bs4 import BeautifulSoup

@dataclass
class Weather_skill:
    name = 'weather_skill'

    def commands(self, command:str):
        return ['weather', 'forecast', 'what is the weather like', 'give me the forecast',"what's the weather","what's the weather like"]

    def handle_command(self, command:str, ai:AI):
        # creating url and requests instance
        url = "https://www.google.com/search?q=weather+in+my+area"
        html = requests.get(url).content

        # getting raw data
        soup = BeautifulSoup(html, 'html.parser')
        temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
        str = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text

        # formatting data
        data = str.split('\n')
        time = data[0]
        sky = data[1]
        
        # getting all div tag
        listdiv = soup.findAll('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'})
        strd = listdiv[5].text
        
        # getting other required data
        pos = strd.find('Wind')
        other_data = strd[pos:]
        
        # printing all data
        print("Temperature is", temp)
        print("Time: ", time)
        print("Sky Description: ", sky)
        print(other_data)

        # saying all data
        ai.say("Temperature is", temp)
        ai.say("Time is", time)
        ai.say("Sky Description: ", sky)
        ai.say(other_data)

def initialize():
    factory.register('weather_skill', Weather_skill)
    # print("Weather initialized")