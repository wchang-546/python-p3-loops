#!/usr/bin/env python3

#Counts down from 10 and prints Happy New Year! 
def happy_new_year():
    i = 10
    while i > 0: 
        print(i)
        i -= 1
        if i == 0:
            print("Happy New Year!")

#returns the list of squared integers
def square_integers(int_list):
    square_integers = [i * i for i in int_list]
    return square_integers

def fizzbuzz():
    i = 1
    while i <= 100: 
        if i % 3 == 0 and i % 5 == 0:
            print ("FizzBuzz")
        elif i % 3 == 0: 
            print ("Fizz")
        elif i % 5 == 0: 
            print ("Buzz")
        else:
            print (i)
        i += 1
