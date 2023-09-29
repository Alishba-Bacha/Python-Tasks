#Fun with If-Else and Loops - Guess the Number Game

#Develop a "Guess the Number" game in Python. The program generates a random number, and the user must guess it. 
#Use if-else statements for checking if the guess is correct and loops to allow multiple guesses until the user 
#gets it right.Provide hints for each incorrect guess to make it more engaging.

import random
#lower and upper bound for range to guess number
lower_bound = int(input("Enter lower bound"))
Upper_bound = int(input("Enter upper bound"))

#Generate random number in given range
num = random.randint(lower_bound, Upper_bound)
z = 10
count = 0
while count!= z:
    count += 1
    guess = int(input("Guess a number"))

    #warning for guessing higher number
    if guess > num:
        print("Try again! You guessed too high.")
    elif guess < num:
        print("Try again! You guessed too small")
    elif guess == num:
        print("congratulations! You guessed the correct number in",count," try")

        break;
#for count>10
if count >= z:
    print("The number is: ", num)
    print("Better Luck next time!")
