#미완

T = int(input()) # testcase

arr = []
res = 0
for i in range(T*2) :
    arr.append(int(input()))


for i in range(0,len(arr),2) :
    if arr[i] == 1 :
        for j in range(1,arr[i+1]+1) :
            res += j
        print(res)
        del arr[i]
        del arr[i+1]
