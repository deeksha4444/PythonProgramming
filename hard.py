def typeOfTrainage(side1,side2,side3):
    if side1==side2 or side1==side3:
        if side2==side3:
          return('equilateral')  #this if is nested in one before it
        else:
            return('isoceles')

    elif side2==side3:
        return('isoceles')
    else:
        return('scalene')


print('enter side1:')
side1=int(input())
print('enter side2:')
side2=int(input())
print('enter side3:')
side3=int(input())

jingle=typeOfTrainage(side1,side2,side3)
print(jingle)
#
# def numberSum(number1,number2):
#     return(number1 + number2)
#
# print('enter number1: ')
# number1=float(input())       #HAD TO ADD THE INT/ FLOAT SIGN
# print('enter number2: ')
# number2=int(input())
#
# numbersAdded=numberSum(number1,number2)
# print(numbersAdded) #its not supposed to be a string LOLLLLLL



/Users/deekshachaudhery/PycharmProjects/untitled5