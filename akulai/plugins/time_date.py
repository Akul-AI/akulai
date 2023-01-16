# This file does anything relating to time/date/calendar... you get the idea.
import time

def handle(command):
    if "time" in command:
        print("The current time is:", time.strftime("%H:%M:%S"))
    