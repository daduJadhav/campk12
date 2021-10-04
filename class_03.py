import random

rand = random.randint(1, 10)

name = input("Hello! what's Your name ?   ")
print("ok "+name+" I have choose the numbers between 1 to 10")
print("You have 5 turns to gess the numbers")

no_of_guess = 0

while no_of_guess < 5 :
    guess = int(input())
    no_of_guess = no_of_guess + 1

    if guess > rand:
        print("You enter the larger Number")
    elif guess < rand:
        print("You enter the smaller Number")
    else:
        break

if(guess == rand):
    print("Win!, You took " + str(no_of_guess) + " turns to guess the number")
else:
    print("Opps ! , you loose the game ")