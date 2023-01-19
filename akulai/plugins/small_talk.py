# Chat with Chatterbot :)
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot("AkulAI")
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english.greetings",
              "chatterbot.corpus.english.conversations")

def handle(akulai, command):
    response = chatbot.get_response(command)
    akulai.speak(response)
