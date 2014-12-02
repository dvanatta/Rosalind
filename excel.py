""" Regarding Interview on 11/25
Create a program to load a text file
Calculate values using rpn
Throw error if in loop
"""
input_data = open("test_data.txt", "r").readlines()
output_file = open("output.txt", "w")
output_file.write(input_data[0]) # transfer dimensions
size = map(int, input_data[0].split())
history = []


def mapping(pointer):
    """
    Takes in a reference (ie "A2") and returns value of that cell
    Also keeps track of history to detect loops
    """
    print "in mapping function to follow ref", pointer, "history is", history
    mapping_dict = {"A": 1, "B": 2}
    cell_value = (mapping_dict[pointer[0]]-1)*size[0]+int(pointer[1])
    print "pointer points to cell", cell_value
    new_cell = input_data[cell_value]
    print "new cell", new_cell
    if new_cell is None:
        # next case should handle this
        print "pointing to empty cell"
        return None 
    elif ' ' not in new_cell and not any(value.isalpha() for value in new_cell):
        # if no (spaces or letters) cell doesn't need more evaluation
        print "cell already evaluated"
        input_data[cell_value] = new_cell
        print "input_data now looks like", input_data
        return new_cell
    else:
        print "cell is not value need to do logic"
        if ' ' in new_cell:
            new_cell = new_cell.split()
        input_data[cell_value] = rpn(new_cell)
        return input_data[cell_value]
#    elif ' ' in new_cell or any(value.isalpha() for value in new_cell):
#            # only keep history is checking more pointers
#            print "cell is not value, need to do logic"
#            history.append(pointer.rstrip())
#            print "new cell adding", pointer, "to history which is now", history
#            if ' ' in new_cell:
#                new_cell = new_cell.split()
#            print "new_cell=", new_cell 
#            input_data[cell_value] =rpn(new_cell)
#            return rpn(new_cell)
#    else pointer in history:
#        print "Cyclic error"
#        return None
#        return map(str.strip, new_cell)


def rpn(cell):
    """
    Calculate Value of cell
    Loops over cell with 3 conditions:
    If cell[i] is ref (ie "A1"):
       evaluate
    if cell[i] is number:
        store value for calculation
    if cell[i] is operator:
        perform operation on stored numbers
    Cyclic loops set cell to None which breaks loop.
    """
    if ' ' in cell:
        cell = cell.split()
    number_list = []
    while cell:
        print "new call to rpn cell =", cell
        print "numberlist", number_list
        if cell[0] is None:
            return
        elif cell[0][0].isalpha():
            print "in pointer loop c0", cell[0]
            ref_cell = mapping(cell[0])
            if ref_cell is None:
                return
            print "are we here??"
            print ref_cell, cell
            cell[0] = ref_cell
        # pythonic method for case statements
        elif cell[0] == '+':
            number_list[0] += number_list.pop(1)
            cell.pop(0)
        elif cell[0] == '-':
            number_list[0] -= number_list.pop(1)
            cell.pop(0)
        elif cell[0] == '*':
            number_list[0] *= number_list.pop(1)
            cell.pop(0)
        elif cell[0] == '/':
            number_list[0] /= number_list.pop(1)
            cell.pop(0)
        else:
            number_list.append(float(cell[0]))
            cell.pop(0)
    print "end of cell loop numberlist", str(number_list)
    return str(number_list[0])


for i in range(1, len(input_data)):
    print "Starting New Cell"
    print "input data looks like", input_data
    final_value = rpn(map(str.strip, input_data[i].split()))
    input_data[i] = final_value
    print "Cell Evaluates to", final_value
    if final_value:
        output_file.write(final_value+"\n")
    else:
        output_file.write("Cyclic Error\n")
    history = []  # clear history after finishing cell evaluation
