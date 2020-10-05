# main function: use try except else = to catch errors
def main ():
    number = 0


#add a while loop around the try-except else
correct_input = False
while not correct_input:
    try:
        number = float(input('Enter a floating point number: '))
    except ValueError:
         print('Oups, that was not the correct format. Try again!')
    else:
        print('Great! You entered ' + str(number))



main()