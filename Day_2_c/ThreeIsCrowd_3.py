#Three is a Crowd Part Three

friends = ['bob', 'kevin', 'stuart', 'otto', 'dave', 'steve' ]

def crowd_test(inlist):
    if len(inlist) > 5:
        print("There's a Mob in here!")
    elif len(inlist) > 3 : 
        print('The room is crowded')
    elif len(inlist) > 0 :
        print('The room is not crowded')
    else:
        print('The room is empty')
    

crowd_test(friends)

friends.pop(0)
friends.pop(1)

crowd_test(friends)

