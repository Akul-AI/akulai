import os

def learn_response(text):
    responses_file = "data/learned_responses.txt"

    with open(responses_file, "a") as f:
        f.write(text + "\n")

    return "I'm sorry, I don't understand. Can you please rephrase that?"
