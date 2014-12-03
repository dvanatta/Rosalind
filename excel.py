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
    Takes in a reference (ie "A2") and returns location of that cell (ie 2)
    """
    print "in mapping function to follow ref", pointer, "history is", history
    history.append(pointer) 
    mapping_dict = {"A": 1, "B": 2}
    cell_value = (mapping_dict[pointer[0]]-1)*size[0]+int(pointer[1])
    return cell_value


def rpn(i):
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
    cell = input_data[i]
    print "New call to rpn, cell=", cell
    if cell is None:
        return None
    elif ' ' not in cell and not any(value.isalpha() for value in cell):
        # if no (spaces or letters) cell doesn't need more evaluation
        print "Cell already evaluated"
        return cell
    elif ' ' not in cell:
        # i think this loop needs to be removed because this first case of the logic evaluation will catch this.  
        # cell has letter but no spaces; must be just pointer
        # check for cyclic errors 
        if cell.rstrip() in history:
            print "Cyclic Error"
            return None
        else:
            print "Cell is pointer"
#            history.append(cell.rstrip())
            new_cell = rpn(mapping(cell.rstrip()))
    else:
        # cell is expresssion, need to do logic
        cell = cell.split()
        number_list = []
        print "Cell is expression"
        while cell:
            if cell[0][0].isalpha():
                 print "cell was", cell
                 cell[0] = rpn(mapping(cell[0].rstrip()))
                 print "cell is now", cell
 #                input_data[i] = cell
                 print "input data is now", input_data
                 if cell[0] is None:
                     return None
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
        input_data[i] = str(number_list[0])
        print "Finished Evaluating cell #", i, "value is", input_data[i]
        return str(number_list[0])


for i in range(1, len(input_data)):
    print "Starting New Cell"
    print "input data looks like", input_data
    final_value = rpn(i)
#    final_value = rpn(map(str.strip, input_data[i].split()))
    input_data[i] = final_value
    print "Cell #",i, "Evaluates to", final_value
    if final_value:
        output_file.write(final_value+"\n")
    else:
        output_file.write("Cyclic Error\n")
    history = []  # clear history after finishing cell evaluation
