#Noah Gaviña
#2.22.19
#Guessing Game
while True:
    import random

    guessesTaken=0
    name=input("Hello user, what is your name?: ")
    if name == "whiteface":
        exit()
    number = random.randint(1,100)
    print("Ok " +name+ " let's play a guessing game.")
    print("The number is between 1 and 100 and you have about 50 guesses.")
    print("ONLY GUESS IN NUMBERS, OTHERWISE I WILL DIE.")
    while guessesTaken < 50:
        print("Take a guess now.:")
        guess = input()
        guess = int(guess)

        guessesTaken=guessesTaken+1

        if guess<number:
            print("Higher.")

        if guess>number:
            print("Lower.")

        if guess==number:
            break
    if guess == number:
        guessesTaken=str(guessesTaken)
        print("Good job " +name+ ". You guessed the number in " +guessesTaken+ " guess(es).")
        print("I am going to restart and forget you now, goodbye " +name+ ".")

    if guess != number:
        number = str(number)
        print("Wrong. The number I was thinking of was " +number)
        print("I am going to restart and forget you now, goodbye " +name+ ".")
