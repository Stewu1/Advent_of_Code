
with open("input.txt", "r") as file:
    combArrays = []
    for line in file.readlines():
        arr = []
        for char in line:
            #print(char,end="")
            if char.isdigit():
                #print("true")
                arr.append(char)
            else:
                #print("false")
                pass
        #print(arr)
        combNums = int(arr[0] + arr[-1])
        #print(combNums)
        combArrays.append(combNums)
    print(sum(combArrays))