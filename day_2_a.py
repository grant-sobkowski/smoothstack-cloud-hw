#Problem 1
def problem_one():
    print('Hello World'[-3])

#Problem 2  
def problem_two():
    my_string = 'thinker'
    print(my_string[2:5])
    print('hello'[1])

#Problem 3  
def problem_three():
    my_string = 'Sammy'
    print(my_string[2:])

#Problem 4
def problem_four(word = 'Mississippi'):
    new_word = []
    for letter in word:
        if letter in new_word:
            continue
        else:
            new_word.append(letter)
    
    print(''.join(new_word))

#Problem 5
def problem_five(num, phrases):
    return_string = []
    phrases = phrases.splitlines()
    for phrase in phrases:
        if(is_palindrome(phrase)):
            return_string.append('Y')
        else:
            return_string.append('N')

    print (' '.join(return_string))
    return (' '.join(return_string))

def is_palindrome(phrase):
    newString = []
    #parses phrase into lowercase word without punctiation
    for letter in phrase:
        if(letter.isalpha()):
            newString.append(letter.lower())

    newString = ''.join(newString)

    if newString == '':
        print(False)
        return False

    isOdd = len(newString) % 2 == 1
    mid = (len(newString)//2)
    left = right = ''
    if isOdd:
        left = newString[:mid+1][::-1]
        right = newString[mid:]
    else:
        left = newString[:mid][::-1]
        right = newString[mid:]
    
    return(left == right)

def main():
    print('Problem 1:'); problem_one()
    print('Problem 2:'); problem_two()
    print('Problem 3:'); problem_three()
    print('Problem 4:'); problem_four()
    print('Problem 5:')
    problem_five(3,
    """Stars
    O, a kak Uwakov lil vo kawu kakao!
    Some men interpret nine memos""")

if(__name__ == '__main__'):
    main()