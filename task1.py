#Write a script that asks the user to input three numbers.
# After reading the user input the script shall display the following:

#The smallest number
#The biggest number
#The average of the three numbers
#The sum of the three numbers
#Create a main function that calls four other functions that perform the
# calculations listed above. When calling the four functions, the three numbers shall be
# sent as arguments. The functions shall return
#the result of their calculations and the answers shall be displayed on the screen.


def add (x,y,z):
    return (x + y + z)

def average (x,y,z):
    return (x+y+z)/3

def small (x,y,z):
    if x < y and x < z:
        return x
    elif y < z:
     return y
    else: return z

def biggest (x,y,z):
    if x > y and x > z:
        return x
    elif y > z:
        return y
    else: return z

def main():
    number_one = int(input("Enter a number: "))
    number_two = int(input("Enter a number: "))
    number_three = int(input("Enter a number: "))

    print("\nSum: " + str(add(number_one, number_two, number_three)))
    print("Average: " + str(average(number_one, number_two, number_three)))
    print("Smallest: " + str(small(number_one,number_two,number_three)))
    print("Biggest: " + str(biggest(number_one,number_two,number_three)))

if __name__ == '__main__':
    main()
