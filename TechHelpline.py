import random


def return_answer(question):
    if "Windows" in question:
        return "Have you tried turning it off and on again?"
    elif "Apple" in question:
        "Have you considered upgrading to the latest offering?"
    elif "Linux" in question:
        "What? You're on your own mate."
    elif "Android" in question:
        "Backup your data and do a factory reset."
    elif "Game" in question:
        "Update your graphics drivers"
    else:
        return "GIT"


def random_disconnect():
    return random.randint(1, 11)


input("Please enter your name: ")
while 1:
    question_input = input("Please enter your question: ")
    if random_disconnect() == 1:
        break
    if question_input.capitalize() == "Goodbye":
        print("Goodbye")
        break
    else:
        print(return_answer(question_input))

