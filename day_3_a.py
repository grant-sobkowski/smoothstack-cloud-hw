#Used for Problem 3
from audioop import reverse
import sys
import random

#Problem 1
def problem_one():
    num_list = []
    for num in range(1500, 2700, 7):
        if(num % 5 == 0):
            num_list.append(num)
    print(num_list)
    return(num_list)

#Problem 2
#Assuming format is in (temp)°C or (temp)°F
def problem_two(temp_string):
    num = float(temp_string[:-2])
    output = -1
    temp_units = ''
    if(temp_string[-1] == 'C'):
        output = (num * 9/5) + 32
        temp_units = 'Fahrenheit'
    elif(temp_string[-1] == 'F'):
        output = (num-32)*5/9
        temp_units = 'Celsius'
    else:
        print('Invalid Input!')
        return(-1)

    output = round(output, 2)

    retstring = '{} is {} in {}'.format(temp_string, output, temp_units)
    print(retstring)

#Problem 3  
def problem_three():
    #Creates a random number from 1-9
    supersecretnum = random.randint(1, 9)

    print('Guess any number 1-9')
    for line in sys.stdin:
        if int(line.rstrip()) == supersecretnum:
            break
        print('Wrong number, guess again')
    print('Well guessed!')

#Problem 4/5
def problem_four():
    count = 0
    for ind in range(10):
        row = []
        for ast in range(count):
            row.append('*')
        print(''.join(row))
        if ind > 4:
            count -= 1
        else: count += 1

#Problem 6
def problem_six():
    print('Enter a word to be reversed:')
    for line in sys.stdin:
        print(line[::-1])
        break
        

#Problem 7
def problem_seven(numbers=(1, 2, 3, 4, 5, 6, 7, 8, 9)):
    even = 0
    odd = 0
    for num in numbers:
        if num % 2 == 0:
            even+=1
        else: odd+=1
    
    print('Number of even numbers:', even)
    print('Number of odd numbers:', odd)



#Problem 8
def problem_eight(inplist):
    for elem in inplist:
        print(elem, type(elem))

#Problem 9
def problem_nine():
    for num in range(1, 7):
        if(num % 3 == 0):
            continue
        print(num)


def main():
    print('Problem 1:'); problem_one()
    print('Problem 2:'); problem_two('60°C')
    print('Problem 3:'); problem_three()
    print('Problem 4/5:'); problem_four()
    print('Problem 6:'); problem_six()
    print('Problem 7:'); problem_seven()
    inplist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]
    print('Problem 8:'); problem_eight(inplist)
    print('Problem 9:'); problem_nine()

if(__name__ == '__main__'):
    main()