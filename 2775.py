

T = int(input())


for t in range(T):
    k = int(input())
    n = int(input())
    room = []

    for i in range(n):
        room.append(i+1)

    for j in range(k):
        addnum = [1]
        for i in range(n-1):
            addnum.append(addnum[i]+room[i+1])
        room = addnum

    print(addnum[n-1])
