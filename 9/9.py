import numpy as np

with open('data.txt', 'r') as file:
    input_ = file.readlines()

head = np.array([0, 0])
tail = np.array([0, 0])


def tail_moves(head, tail):
    moves_for_tail = {
        (2, 1): (1, 1),  # Head is 2 up and 1 right so tail follows just to be in range
        (1, 2): (1, 1),
        (2, 0): (1, 0),
        (2, -1): (1, -1),
        (1, -2): (1, -1),
        (0, -2): (0, -1),
        (-1, -2): (-1, -1),
        (-2, -1): (-1, -1),
        (-2, 0): (-1, 0),
        (-2, 1): (-1, 1),
        (-1, 2): (-1, 1),
        (0, 2): (0, 1),
    }
    new_tail_pos = tail + \
        np.array(moves_for_tail.get(tuple(head - tail), (0, 0)))
    return new_tail_pos


def head_moves(head, dir):
    if dir == 'R':
        head[1] += 1
    elif dir == 'L':
        head[1] -= 1
    elif dir == 'U':
        head[0] += 1
    elif dir == 'D':
        head[0] -= 1
    return head


tail_pos = set([tuple(tail)])

for i in input_:
    move = [(i.strip().split(' ')[0], int(i.strip().split(' ')[1]))]
    for dir, dist in move:
        while dist > 0:
            head = head_moves(head, dir)
            dist -= 1
            tail = tail_moves(head, tail)
            tail_pos.add(tuple(tail))
            print(head, tail)
print(len(tail_pos))
