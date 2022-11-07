T = int(input())   
arr = []
for i in range(T):
    number = list(map(int, input().split()))
    arr.append(number)


for i in range(len(arr)):

    y = int(arr[i][2]%arr[i][0])*100

    if arr[i][2] == 1:
        y = 100
        x = 1
    elif y == 0 and arr[i][0] == 1 :
        y = 100
        x = arr[i][2]
    elif y == 0 :
        y = arr[i][0] * 100
        x = int(arr[i][2]/arr[i][0])
    else :
        x = int(arr[i][2]/arr[i][0]) + 1
    
    print(y+x)
