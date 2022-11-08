
r = 31
M = 1234567891
answer = 0

L = int(input())
string = str(input())
string = list(string)

for i in range(len(string)) :
    answer += (ord(string[i])-96) * (r**i)
print(answer%M)
