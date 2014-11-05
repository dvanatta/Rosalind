# need to store orientation and score for each vert
import numpy

# input [Top, South, East]
die = [1, 3, 2]


def initialize(x, y):
    vert_list = []
    for i in range(x):
        for j in range(y):
            vert_list.append([i, j])
    scores = numpy.zeros((x, y)) + float('inf')
    scores[0, 0] = die[0]
    dice = []
    for i in range(x):
        dice.append([[0, 0, 0]] * y)
    dice[0][0] = die
    return vert_list, dice, scores


def move_up(x):
    return [x[1], 7 - x[0], x[2]]


def move_right(x):
    return [x[2], x[1], 7 - x[0]]


def lowest_unchecked(vert_list, scores):
    min_val = float('inf')
    i, j = 0, 0
    for vert in vert_list:
        if scores[(vert[0], vert[1])] < min_val:
            min_val = scores[(vert[0], vert[1])]
            i, j = vert[0], vert[1]
    return min_val, i, j


def run(x, y):
    x += 1  # Oops, implemented for starting at 1,1 instead of 0,0
    y += 1
    vert_list, dice, scores = initialize(x, y)
    while vert_list:
        lowest_score, i, j = lowest_unchecked(vert_list, scores)
        vert_list.remove([i, j])
        if i + 1 < x:
            die1 = move_right(dice[i][j])
            if scores[i + 1, j] >= scores[i, j] + die1[0]:
                scores[i + 1, j] = scores[i, j] + die1[0]
                dice[i + 1][j] = die1
        if j + 1 < y:
            die1 = move_up(dice[i][j])
            if scores[i, j + 1] >= scores[i, j] + die1[0]:
                scores[i, j + 1] = scores[i, j] + die1[0]
                dice[i][j + 1] = die1
    print scores, lowest_score
    return lowest_score

print run(2, 3)
