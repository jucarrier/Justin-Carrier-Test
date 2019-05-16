def lines_overlap(line_1, line_2, points_overlap=True):
    # line_1 and line_2 are tuples containing two floats which represent x1 and x2.
    # points_overlap determines if only one point from the lines overlap then the lines overlap.
    # Set to true, (0,1) and (1,2) do overlap. Set to false, the sames lines don't.
    if points_overlap:
        if line_1[0] in line_2 or line_1[1] in line_2:
            return True
    if point_is_between(line_1[0], line_2) or point_is_between(line_1[1], line_2) \
            or point_is_between(line_2[0], line_1):
        # The only scenario where the first two checks would not detect overlap is if line two is
        # contained completely in line one. This is why we don't need to check
        # point_is_between(line_2[1], line_1)
        return True
    return False


def point_is_between(point, line):
    # returns true if given point is inside a line
    if line[0] > point > line[1] or line[0] < point < line[1]:
        return True
    return False


def input_to_tuple(line):
    # Checks and transforms input strings to tuples of type (float, float)
    # Returns None if the input was invalid
    line = line.replace(' ', '').replace('(', '').replace(')', '')
    try:
        out = (float(line.split(',')[0]), float(line.split(',')[1]))
        return out
    except ValueError:
        print("Invalid line formats. Please enter them in the form (x1,x2).")
        request_inputs()


def request_inputs():
    # Takes inputs from user. Both inputs must be valid to check overlapping
    line_1 = input_to_tuple(input("line 1 (x1,x2): "))
    if not line_1:
        return
    line_2 = input_to_tuple(input("line 2 (x3,x4): "))
    if not line_2:
        return
    print(lines_overlap(line_1, line_2))


if __name__ == "__main__":
    request_inputs()
