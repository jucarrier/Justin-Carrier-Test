import re


def sanitize_input(str):
    # Remove superfluous separators
    str = " ".join(re.split("\s+", str, flags=re.UNICODE))
    str = " ".join(re.split(",{2,}", str, flags=re.UNICODE))
    if str.count(',') > 1 or str.count(' ') > 1:
        print("You must only enter two numebrs")
        return -1
    try:
        if ',' in str:
            num_1 = str.replace(' ', '').split(',')[0]
            num_2 = str.replace(' ', '').split(',')[1]
        else:
            num_1 = float(str.split(' ')[0])
            num_2 = float(str.split(' ')[1])
        if num_1 == "" or num_2 == "":
            raise IndexError
        num_1 = float(num_1)
        num_2 = float(num_2)
        if num_1 is None or num_2 is None:
            raise ValueError
        if num_1 == num_2:
            comparator = "equal to"
        elif num_1 > num_2:
            comparator = "larger than"
        else:
            comparator = "smaller than"
        return "%g is %s %g" % (num_1, comparator, num_2)
    except ValueError:
        # Values entered were not floats or ints
        print("You must enter numbers.")
        return -1
    except IndexError:
        # Checks if user only entered one number
        print("You must enter two numbers")
        return -1
    except:
        # Should never execute
        print("Invalid input.")
        return -1


def request_input():
    s = input("Numbers to compare: ")
    res = sanitize_input(s)
    if res != -1:
        print(res)
        return res
    else:
        request_input()


if __name__ == "__main__":
    request_input()
