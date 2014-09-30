

total = 1
rep_age = 0
iteration = 0
def count_rabbits(n,k):    
    
    global iteration
    iteration += 1
    print iteration, n
    if iteration <= n:
        count_rabbits(total, rep_age)
    else:
        return total


count_rabbits(5,3)
