""" Regarding Interview on 11/15
Create a program to load a text file 
Calculate values using rpn
Throw error if in cyclic loop
"""

input_data = open("test_data.txt", "r").readlines()
outfile = open("rpn_output.txt", "w")
size = map(int,input_data[0].split())
number_list = []
histroy = []

def mapping(pointer, history):
    """
    Takes in a reference (ie "A2") and returns the value of that cell
    Also keeps track of history to detect loops
    """
    mapping = {"A": 1, "B": 2}
    if pointer in history:
        history = []
        print "Cyclic error"
        return None, history 
    else: 
        history.append(pointer.rstrip())
        return input_data[(mapping[pointer[0]]-1)*size[0]+int(pointer[1])], history


def rpn(cell):
    """
    Calculate Value of cell
    """
    global history
    cell = map(str.strip, cell.split())
    for i in cell:
        if i[0].isalpha():
            new_cell, history = mapping(i,history)
            if new_cell:
                rpn(new_cell)
        elif i == '+':
            number_list[0] += number_list.pop(1) 
        elif i == '-':
            number_list[0] -= number_list.pop(1) 
        elif i == '*':
            number_list[0] *= number_list.pop(1) 
        elif i == '/':
            number_list[0] /= number_list.pop(1) 
        else:
            number_list.append(float(i))
    history = []
    return number_list


for i in input_data[1:]:
    number_list = []
    final = rpn(i)
    if final:
        outfile.write(str(final[0])+'\n')
    else:
        outfile.write("Error"+"\n")
