import sys
def collatz(number):
    if number % 2 == 0:
        number = number // 2
        print(number)
        return number

    elif number % 2 == 1 :
        number = 3 * number + 1
        print(number)
        return number

iValue = input('Enter an integer:')
while iValue != 1:
    try: # exception handling
        iValue = collatz(int(iValue))
    except:
        print('Not an integer, please try again!')
        break