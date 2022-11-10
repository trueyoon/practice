#math라이브러리 없이 구현하기

a, b = map(int, input().split())

# gcd

for i in range(min(a,b), 0, -1) : #a
    if a%i == 0 and b%i == 0 :
        print(i)
        break

#lcm

for i in range(max(a,b), a*b+1) :
    if i%a == 0 and i%b==0 :
        print(i)
        break
