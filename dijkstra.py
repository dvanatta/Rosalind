# for 2,2 starting at 1,3,2 should be 13
# need to store position, orientation, and score
# output = [i,j,score,[t,s,w]]
import numpy

die = [1,3,2]

  
#output_array
def initialize(x,y):
    scores = numpy.zeros((x,y))+float('inf')
    scores[0,0] = 1
    dice = []  
    for i in range(x):
        dice.append([[0,0,0]]*y)
        for j in range(y+1):
             pass        
#            v[(i,j)]= [[]]
#            v.append([[i,j],[]])
#            scores.append(float('inf'))
    dice[0][0] = die
#    print dice[0][0], scores[0,0]

#    print dice[0][0]
    return dice, scores

def move_up(x):
    return [x[1],7-x[0],x[2]]

def move_right(x):
    return [x[2],x[1],7-x[0]]


#look at pseudo code, you might need some equivalent for v. 
def run(x,y):
    dice, scores = initialize(x,y)
    while scores.max() == float('inf'):
        lowest_score = scores.min()
        print scores, scores.min()
        i,j = numpy.where(scores == lowest_score)
        print numpy.where(scores == lowest_score)
#        scores[i,j] = 100000
        print i, x
        if i+1 < x:
                die1 = move_right(dice[i][j])
                if scores[i+1,j] >= scores[i,j] + die1[0]:
                    scores[i+1,j] = scores[i,j] + die1[0]
                    dice[i+1][j] = die1
                    scores[i,j] = 1000000  # OH GOD THIS IS TERRIBLE I'M SO SORRY
                    pass
        if j+1 < y:
                die1 = move_up(dice[i][j])
                if scores[i,j+1] >= scores[i,j] + die1[0]:
                    scores[i,j+1] = scores[i,j] + die1[0]
                    dice[i][j+1] = die1
                    scores[i,j] = 1000000  # OH GOD THIS IS TERRIBLE I'M SO SORRY
                    pass
#            die1 = move_up(die)
#            die2 = move_right(die)
        print x,y
        if scores[x-1,y-1] != float('inf'): 
            break
    print scores, lowest_score        
    return scores.min()    

#init_np(2,2)
print run(5,5)


