import random
x=random.randrange(1,21)
name=input("Hello! What is your name?\n")
guess=int(input("Well, "+name+", I am thinking of a number between 1 and 20.\nTake a guess.\n"))
count=1
while True:
    if  guess==x:
        print("Good job, "+name+"! You guessed my number in "+str(count)+" guesses!")
        break
    elif guess < x :
        print("Your guess is too low.\nTake a guess")
        count+=1
    else:
        print("Your guess is too high.\nTake a guess") 
        count+=1
    guess=int(input())     