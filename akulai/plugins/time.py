import time

def handle(command):
    if "time" in command:
        print("The current time is:", time.strftime("%H:%M:%S"))
