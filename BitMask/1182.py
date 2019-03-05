#부분 수열의 합
#비트 마스크는 모든 리스트에서 모든 부분 수열,집합 (조합)을 고를 수있음
#combination은 N개중에, M개의 조합을 구함
N, S = map(int, input().split())
L = list(map(int, input().split()))
ans = 0
for i in range(1,1<<N):# 0000 0001 0010 0011 0100 0101... 1111
    #0이 포한되지 않는 이유, 공집합이니까, 1<<N은 10000이므로 제외
    sum = 0
    for k in range(0,N):
        if i&(1<<k): #비트조회
            #1<<k의 의미, k는 0,1,2,3 즉 0001 0010 0100 1000 
            sum += L[k]# & = true면, 그 비트값을 더해라
    if sum == S:
        ans +=1

print(ans)
