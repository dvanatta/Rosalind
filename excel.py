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


# need to figure out where th history call goes. needs to be called only if cell isnt a number

def mapping(pointer):
    """
    Takes in a reference (ie "A2") and returns value of that cell
    Also keeps track of history to detect loops
    """
    print "in mapping function to follow ref", pointer, "history is", history
    mapping_dict = {"A": 1, "B": 2}
    cell_value = (mapping_dict[pointer[0]]-1)*size[0]+int(pointer[1])
    new_cell = input_data[cell_value]
    return input_data[cell_value], cell_value


def rpn(cell):
    """
    Calculate Value of cell
   If cell is none -> error condition
   If cell is number -> no evaluation required
   If cell is just ref -> follow ref (store history)
   If cell is expression -> loop over cell
       If cell[i] is ref (ie "A1"):
          evaluate
       if cell[i] is number:
           store value for calculation
       if cell[i] is operator:
           perform operation on stored numbers
    """
    print "fresh call to rpn, cell =", cell
    print "input is", input_data
    if cell is None:
        return None
    elif ' ' not in cell and not any(value.isalpha() for value in cell):
        # if no (spaces or letters) cell doesn't need more evaluation
        print "cell already evaluated"
        return cell
    elif ' ' not in cell:
        # cell has letter but no spaces; must be just pointer
        if cell.rstrip() in history:
            print "before error cell, history", cell, history
            print "Cyclic Error"
            return None
        else:
            #input_data[cell_value] = rpn(new_cell)
            print "cell is pointer"
            new_cell, k = rpn(mapping(cell))
            print "points to", new_cell
            if ' ' not in new_cell and not any(value.isalpha() for value in new_cell):
                return new_cell
            else:
                history.append(cell.rstrip())
                return new_cell
            
    else:
    # cell is expresssion, need to do logic
        cell = cell.split()
        number_list = []
        while cell:
            print "entering cell eval loop cell=", cell
            print "numberlist", number_list
            if cell[0][0].isalpha():
                 cell[0] = rpn(cell[0])
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
        input_data[cell_value] = str(number_list[0])
        print "end of cell loop numberlist", str(number_list)
        return str(number_list[0])


for i in range(1, len(input_data)):
    print "Starting New Cell"
    print "input data looks like", input_data
    final_value = rpn(input_data[i])
#    final_value = rpn(map(str.strip, input_data[i].split()))
    input_data[i] = final_value
    print "Cell Evaluates to", final_value
    if final_value:
        output_file.write(final_value+"\n")
    else:
        output_file.write("Cyclic Error\n")
    history = []  # clear history after finishing cell evaluation
