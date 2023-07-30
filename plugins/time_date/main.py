import datetime

# define all commonly used variables here
now = datetime.datetime.now()

def handle(command):
    if "time" in command:
        time_now = now.strftime("%H:%M:%S")
        akulai.speak(f"The current time is{time_now}")
    if "date" in command:
        date_now = now.strftime("%Y-%m-%d") 
        akulai.speak(f"The current date is{date_now}")
