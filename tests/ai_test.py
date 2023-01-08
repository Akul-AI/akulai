from akulai.core.ai import AI
from time import sleep

akulai = AI()
print ("say something")
message = ""
while True and message != 'good bye':
    message = akulai.listen()
    if message:
        print(message)
    # sleep(0.5)