import requests
import datetime

# define all commonly used variables here
now = datetime.datetime.now()

response = requests.get('http://127.0.0.1:8000/speak')
def handle(command):

    if "time" in command:
        time_now = now.strftime("%H:%M") # %H:%M:%S
        speak(f"The current time is {time_now}")
    
    if "date" in command:
        date_now = now.strftime("%Y-%m-%d") 
        speak(f"The current date is {date_now}")