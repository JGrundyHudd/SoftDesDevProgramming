import random
attempts = 0
for problem_no in range(1, 6):
    correct = 0
    operand_one = random.randint(0, 13)
    operand_two = random.randint(0, 13)
    while correct == 0:
        answer = input(str(operand_one) + "x" + str(operand_two) + "=")
        if answer == str(operand_one*operand_two):
            correct = 1
            print("Well Done")
        else:
            print("Try again")
        attempts = attempts + 1
print("Your average attempts per problem was: " + str(attempts/5))
