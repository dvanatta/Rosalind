""" Regarding Interview on 11/15
Create a program to load a text file 
Calculate values using rpn
Throw error if in loop
"""

input_data = open("test_data.txt", "r").readlines()
#input_data = open("norec.txt", "r").readlines()
output = []
size = map(int,input_data[0].split())

def mapping(pointer, history):
#    print "in making function, history, pointer", history, pointer.rstrip()
    mapping = {"A": 1, "B": 2}
    if pointer in history:
        history = []
        print "Cyclic error"
        return None, history 
    else: 
        history.append(pointer.rstrip())
#        print "new spot, appending", pointer, "to history which is now", history
#    print pointer
#    print "pointer points to cell", (mapping[pointer[0]]-1)*size[0]+int(pointer[1])
        return input_data[(mapping[pointer[0]]-1)*size[0]+int(pointer[1])], history
number_list = []
histroy = []
def rpn(cell):
    global history
#    print cell
    for i in cell:
#        print i,number_list
        if i[0].isalpha():
#            print "global history", history
            new_cell, history2 = mapping(i,history)
#            print "new_cel", new_cell.rstrip(), history2
            if new_cell:
                new_cell = map(str.strip, new_cell.split())
                rpn(new_cell)
        elif i == '+':
            number_list[0] += number_list.pop(1) 
#            print "i added! z =",number_list[0] 
        elif i == '-':
            number_list[0] -= number_list.pop(1) 
#            print "i subtracted z =", number_list[0]
        else:
            z = float(i)
            number_list.append(z)
    history = []
    return number_list


for i in input_data[1:]:
    number_list = []
#    print "before rpn i =", i
    i = map(str.strip, i.split())
    print "cell", i,
    final = rpn(i)
    print "FINAL VALUE", final

