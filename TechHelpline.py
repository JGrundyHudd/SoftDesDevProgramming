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
    elif "Vista" in question:
        "Just let it die in peace, it's for the best"
    else:
        random_choice = random.randint(0, 5)
        if random_choice == 0:
            return "Are you sure it's on?"
        elif random_choice == 1:
            return "Try rerouting main power through the secondary coupling"
        elif random_choice == 2:
            return "Have you tried forcing an unexpected reboot?"
        elif random_choice == 3:
            return "Yeah that does sound pretty bad. Oh well."
        elif random_choice == 4:
            return "Sounds as if you need our new guide to troubleshooting, just £34.99 this week only"


def random_disconnect():
    return random.randint(1, 11)


input("Hello, what is your name? ")
while 1:
    question_input = input("Please enter your question: ")
    if random_disconnect() == 1:
        break
    if question_input.capitalize() == "Goodbye":
        print("Goodbye")
        break
    else:
        print(return_answer(question_input))
