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
    if pointer in history:
        print "Cyclic error"
        return None
    else:
        history.append(pointer.rstrip())
        cell_value = (mapping_dict[pointer[0]]-1)*size[0]+int(pointer[1])
        print "new cell adding", pointer, "to history which is now", history
        print "pointer points to cell", cell_value
        return map(str.strip, input_data[cell_value].split())


def rpn(cell):
    """
    Calculate Value of cell
    Loops over cell with 3 conditions:
    If cell is ref (ie "A1"):
       evaluate
    if cell is number:
        store value for calculation
    if cell is operator:
        perform operation on stored numbers
    Cyclic loops set cell to None which breaks loop.
    """
    number_list = []
    while cell:
        if cell[0] is None:
            return
        elif cell[0][0].isalpha():
            ref_cell = mapping(cell[0])
            if ref_cell is None:
                return
            cell[0] = rpn(ref_cell)
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
    return str(number_list[0])


for i in input_data[1:]:
    print "Starting New Cell"
    final_value = rpn(map(str.strip, i.split()))
    print "Cell Evaluates to", final_value
    if final_value:
        output_file.write(final_value+"\n")
    else:
        output_file.write("Cyclic Error\n")
    history = []  # clear history after finishing cell evaluation
