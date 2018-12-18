#!/usr/bin/env python3
import random


def randomNum():
    num = random.randint(1, 10)
    return num


rand = randomNum()


def check(rand):
    correct = False
    count = 1
    while not correct:
        uGuess = int(input('What is your guess?'))
        if uGuess < rand:
            print('Your Guess is too low')
            correct = False
            count += 1
        elif uGuess > rand:
            print('Your guess is too high')
            correct = False
            count += 1
        elif uGuess == rand:
            print('You did it! Your guess of ' + str(uGuess) + ' is the correct. You guessed it in ' + str(count) + ' turns.')
            correct = True


check(rand)
