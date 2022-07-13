

# Problem 1 :
def problem_one():
    num_one = 50+50
    num_two = 100-10
    print(num_one + num_two)

# Problem 2
def problem_two():
    try:
        print(eval('print(30+*6)'))
    except:
        print('Syntax Error')

    print(6^6)

    print(6**6)

    print(6+6+6+6+6+6)

# Problem 3:
def problem_three():
    print("Hello World")
    print("Hello World : 10")

# Problem 4:
def problem_four(p, r, l):
    r /= 100
    i = r/12
    compint = (1+i) ** l
    mpay = p*(i*(compint))/(compint-1)
    mpay = round(mpay)
    print("Joel's monthly payment will be $" + str(mpay))

    return mpay

def main():
    print('Problem 1:'); problem_one()
    print('Problem 2:'); problem_two()
    print('Problem 3:'); problem_three()
    print('Problem 4:'); problem_four(800000, 6, 103)


if(__name__ == '__main__'):
    main()
