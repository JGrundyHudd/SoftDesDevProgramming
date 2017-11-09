import random
question = ""
while question != "Goodbye":
    question = input("Enter a question: ")
    print(random.choice(["Yes", "no", "Maybe"]))
else: print("end")