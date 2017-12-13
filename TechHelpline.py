import random


def return_answer(question):
    if "Windows" in question:
        return "Brimble my doobletip"
    elif "Apple" in question:
        "please kill yourself"
    else:
        return "GIT"


def random_disconnect():
    if random.randint(1,11) == 1:
        return 1


input("Please enter your name: ")
while 1:
    print(return_answer(input("Please enter your question: ")))
    if random_disconnect() == 1:
        break
