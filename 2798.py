#첫째줄에 N과 M
#둘째줄에 카드에 쓰여있는 숫자 (개수는 N개)
#N을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합을 구해 출력하시오.



N,M = map(int, input().split())
arr = list(map(int, input().split()))
answer = []
i = 0
arr.sort(reverse=True)
for i in range(0, len(arr)-2) :
    for k in range(i+1, len(arr)-1) :
        for j in range(k+1, len(arr)) :
            answer.append(arr[i]+arr[k]+arr[j])
answer.sort(reverse=True)
while (True) :
    if not answer[0] > M :
        print(answer[0])
        break
    else :
        del answer[0]

'''
a[0] a[1] a[2]
a[0] a[1] a[3]
a[0] a[1] a[len(a)]
a[0] a[2] a[3]
a[0] a[2] a[len(a)]
a[0] a[3] 

'''
