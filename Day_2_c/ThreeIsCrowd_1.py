#Three is a Crowd Part One

friends = ['bob', 'kevin', 'stewart', 'otto']

def crowd_test(inlist):
    if len(inlist) > 3 : 
        print('The room is crowded')

crowd_test(friends)

friends.pop(0)
friends.pop(1)


crowd_test(friends)


