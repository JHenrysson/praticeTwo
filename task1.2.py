#The function checks if
#the shot x is greater or equal to the smallest ship x and smaller or equal
#to the biggest ship x.



def is_Hit (x,y):
    if x >= 3 and x <= 5:
        if y <= 2 and y <=2:
            return True

    if x >= 6 and x <= 6:
        if y >= 7 and y <=9:
            return True

    return False

print(is_Hit(9,9))

