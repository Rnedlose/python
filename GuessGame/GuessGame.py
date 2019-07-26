import os
from random import randint

def num_gen():
    return randint(1, 100)

def num_guess():
    
    num = num_gen()

    flag = 0
    
    guesses_left = 5

    print("\tLet's playing a guessing game!!!!!\n")            
    print("\tPlease guess a number between 1 and 100.\n")
    print("\tAfter each wrong guess, you will be given a hint!!!\n")
    print("\tFive guesses await you.  Get it done!!!\n")

    while guesses_left > 0:

            guess = int(input("\tChoose your number!!\n"))
            
            if guess == num:
                flag = 1
                break
            
            elif guess < num:
                print("\tYour guess was less than the number.\n")

            elif guess > num:
                print("\tThat guess was bigger than the number.\n")

            guesses_left -= 1

    if flag is 1:
        print("\tYou win!! Congratulations!!\n")

    else:
        print("\tYou win.... a big fat L cause you lost!!\n")
    print("\tThe number was: " + str(num))

num_guess()


