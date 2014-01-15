"""
Cameron Little
14 Jan 2014

Microsoft Code4Cash
"""

f = open('SampleInput.txt', 'r')
f_str = f.read()
f.close()
instructions = f_str.lower().split('\r\n')
pos = [0, 0] # starting pos [n/s, e/w]
directions = ['n', 'e', 's', 'w']
facing = 0 # index of direction I'm facing

for instruction in instructions:
    components = instruction.split(' ')
    # assuming n/e is positive
    if components[0] == 'move':
        if facing == 0: # n
            pos[0] += int(components[1])
        elif facing == 2: # s
            pos[0] -= int(components[1])
        elif facing == 1: # e
            pos[1] += int(components[1])
        elif facing == 3: # w
            pos[1] -= int(components[1])
    elif components[0] == 'turn':
        if components[1] == 'left':
            facing = (facing - 1) % 4
        elif components[1] == 'right':
            facing = (facing + 1) % 4

f = open('FollowDirections.txt', 'w')
f.write(str(pos[1]) + ',' + str(pos[0]) + '\r\n')
f.close()
