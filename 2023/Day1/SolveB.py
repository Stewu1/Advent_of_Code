import re

def convert_number(numb_as_string):
    if numb_as_string == "zero":
        return "0"
    elif numb_as_string == "one":
        return "1"
    elif numb_as_string == "two":
        return "2"
    elif numb_as_string == "three":
        return "3"
    elif numb_as_string == "four":
        return "4"
    elif numb_as_string == "five":
        return "5"
    elif numb_as_string == "six":
        return "6"
    elif numb_as_string == "seven":
        return "7"
    elif numb_as_string == "eight":
        return "8"
    elif numb_as_string == "nine":
        return "9"
    else:
        return None


with open("input.txt", "r") as file:
    combArrays = []
    for line in file.readlines():
        arr = []
        print(line)
        x = re.findall("(?=(\d|zero|one|two|three|four|five|six|seven|eight|nine))", line)
        print(x)
        for i in x:
            if len(i)>1:
                arr.append(convert_number(i))
            else:
                arr.append(i)
        combNums = int(arr[0] + arr[-1])
        combArrays.append(combNums)

    print(sum(combArrays))
