import random

def randint ()

chances = random.randint(1,5)

guess = input ("Enter your number")

number = random.randint (1,5)

#While loop to count the number of chances
while chances < 5:

    if guess == number:
        print ("Congratulations. You won!!!")
        break

    if not chances < 5:
        print ("You lose. The number is", number)

randint ()