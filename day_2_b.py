#Problem 1
def problem_one():
    my_list = [3, 'banana', 3.14]
    print(my_list)

#Problem 2  
def problem_two():
    example_list = [1, 1, [1, 2]]
    print(example_list[2][1])

#Problem 3  
def problem_three():
    lst=['a', 'b', 'c']
    print(lst[1:])

#Problem 4
def problem_four():
    week = {
        'Monday': 0,
        'Tuesday': 1,
        'Wednesday': 2,
        'Thursday': 3,
        'Friday': 4,
        'Saturday': 5,
        'Sunday': 6
    }
    print(week)

#Problem 5
def problem_five():
    d = {'k1': [1,2,3]}
    print(d['k1'][1])

#Problem 6
def problem_six():
    my_list = [1, [2,3]]
    my_tuple = tuple(my_list)
    print(my_tuple)

#Problem 7
def problem_seven(word = 'Mississippi'):
    new_word = set()
    for letter in word:
        new_word.add(letter)
    
    print(new_word)

#Problem 8
    new_word.add('X')
    print(new_word)

#Problem 9
def problem_nine():
    my_set = {1, 1, 2, 3}
    print(my_set)

def problem_ten():
    return_list = []
    for number in range(2000, 3200):
        if(number % 7 == 0 and not number % 5 == 0):
            return_list.append(number)
    print(return_list)


def main():
    print('Problem 1:'); problem_one()
    print('Problem 2:'); problem_two()
    print('Problem 3:'); problem_three()
    print('Problem 4:'); problem_four()
    print('Problem 5:'); problem_five()
    print('Problem 6:'); problem_six()
    print('Problem 7/8:'); problem_seven()
    print('Problem 9:'); problem_nine()
    print('Problem 10:'); problem_ten()
    # print('Problem 10:'); problem_five()

if(__name__ == '__main__'):
    main()