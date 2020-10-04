#A quite famous number sequence is the Fibonacci Sequence (Links to an external
# site.) where one gets the next number in the sequence by adding the two previous numbers.
#As described on the linked webpage the first two numbers are 0 and 1,
# using these numbers it is now easy to continue the sequence.
#The task is to develop a function that takes one parameter,
# the number of Fibonacci numbers to display.
# The goal of the function is to display the specified amount of numbers from the
# sequence on the screen. An example can be seen below:

def fib (x):
    n1 = 0
    n2 = 1
    print(n1)
    print(n2)
    for i in range(x-2):
        n3 = n1 + n2
        n1 = n2
        n2 = n3


        print(n3)

fib(9)