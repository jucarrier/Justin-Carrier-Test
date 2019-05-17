import re


def sanitize_input(str):
    # Remove superfluous separators
    str = " ".join(re.split("\s+", str, flags=re.UNICODE))
    str = " ".join(re.split(",{2,}", str, flags=re.UNICODE))
    if str.count(',') > 1 or str.count(' ') > 1:
        return "You must only enter two numbers"
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
        return "You must enter numbers"
    except IndexError:
        # Checks if user only entered one number
        return "You must enter two numbers"


def request_input():
    s = input("Numbers to compare: ")
    res = sanitize_input(s)
    if any(char.isdigit() for char in res):
        print(res)
        return res
    else:
        request_input()


if __name__ == "__main__":
    assert (sanitize_input("5,1") == "5 is larger than 1")
    assert (sanitize_input("5, 1") == "5 is larger than 1")
    assert (sanitize_input("5 1") == "5 is larger than 1")
    assert (sanitize_input("5.9   1") == "5.9 is larger than 1")
    assert (sanitize_input("5,,,,1") == "5 is larger than 1")
    assert (sanitize_input("5.1,1.3") == "5.1 is larger than 1.3")
    assert (sanitize_input("5,1") == "5 is larger than 1")
    assert (sanitize_input("5,1") == "5 is larger than 1")
    assert (sanitize_input("1.8,    9") == "1.8 is smaller than 9")
    assert (sanitize_input("-2, -1") == "-2 is smaller than -1")
    assert (sanitize_input("0 0") == "0 is equal to 0")
    assert (sanitize_input("0,") == "You must enter two numbers")
    assert (sanitize_input("seven,") == "You must enter two numbers")
    assert (sanitize_input(",9") == "You must enter two numbers")
    assert (sanitize_input("abc,") == "You must enter two numbers")
    assert (sanitize_input("help") == "You must enter numbers")
    assert (sanitize_input("1,2,3") == "You must only enter two numbers")
    request_input()
