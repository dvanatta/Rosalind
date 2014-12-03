""" Regarding Interview on 11/25
Create a program to load a text file
Calculate values using rpn
Throw error if in loop
"""
input_data = open("test_data.txt", "r").readlines()
output_file = open("output.txt", "w")
output_file.write(input_data[0])  # transfer dimensions
size = map(int, input_data[0].split())
history = []


def mapping(pointer):
    """
    Takes in a reference (ie "A2") and returns location of that cell (ie 2)
    """
    print "in mapping function to follow ref", pointer, "history is", history
    mapping_dict = {"A": 1, "B": 2}
    cell_value = (mapping_dict[pointer[0]]-1)*size[0]+int(pointer[1])
    return cell_value


def rpn(i):
    """
    Calculate Value of cell
    If cell is none -> error condition
    If cell is number -> no evaluation required
    If cell is expression -> loop over cell
       If cell[i] is ref (ie "A1"):
          evaluate
       if cell[i] is number:
           store value for calculation
       if cell[i] is operator:
           perform operation on stored numbers
    """
    global history
    cell = input_data[i]
    print "New call to rpn, cell=", cell
    if cell is None:
        # Error condition
        return None
    if ' ' not in cell and not any(value.isalpha() for value in cell):
        # if no (spaces or letters) cell doesn't need more evaluation
        print "Cell already evaluated, remove it from history"
        if len(history) > 0:
            history.pop()
        return cell
    else:
        print "Cell is expression, evaluating cell"
        cell = cell.split()
        number_list = []
        while cell:
            if cell[0][0].isalpha():
                print "Value is pointer"
                cell_index = mapping(cell[0].rstrip())
                if cell_index in history:
                    print "Cyclic Error"
                    return None
                else:
                    history.append(cell_index)
                    cell[0] = rpn(cell_index)
                if cell[0] is None:
                    return None
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
        print "Finished cell #", i, "in math loop. value is", input_data[i]
        return str(number_list[0])


for i in range(1, len(input_data)):
    print "Starting New Cell"
    print "Data is currently", input_data
    final_value = rpn(i)
    input_data[i] = final_value
    print "Cell #", i, "Evaluates to", final_value
    if final_value:
        output_file.write(final_value+"\n")
    else:
        output_file.write("Cyclic Error\n")
    history = []  # clear history after finishing cell evaluation
