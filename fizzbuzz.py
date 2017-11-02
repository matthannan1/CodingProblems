"""
    2 Nov 2017, Matt Hannan
    I've heard about this FizzBuzz test before, but I never saw it
    spelled out until I read this page:

    https://blog.codinghorror.com/why-cant-programmers-program/    

    "Write a program that prints the numbers from 1 to 100.
    But for multiples of three print "Fizz" instead of the number
    and for the multiples of five print "Buzz". For numbers which
    are multiples of both three and five print "FizzBuzz"."

    Something in the back of my mind is yelling at me about using 
    text formatting as part of the solution, but this is what I came
    up with in a hurry. I am sure there is a better way to do this,
    but this is mine.
"""


for x in range(1, 101):
    if x % 3 == 0 and x % 5 == 0:
        print("FizzBuzz")
    elif x % 3 == 0 and x % 5 != 0:
        print("Fizz")
    elif x % 5 == 0 and x % 3 != 0:
        print("Buzz")
    else:
        print(x)
    