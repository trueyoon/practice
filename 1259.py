

while (True) :
    res = 0
    string = str(input())
    if string == '0' :
        break
    string = list(string)
    length = int(len(string)/2)
    for i in range(length):
        if string[i] == string[-(i+1)] :
            res += 1
    if res == length :
        print("yes")
    else :
        print("no")
