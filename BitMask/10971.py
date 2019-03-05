##10971 외판원 순회 비트마스크로 풀기
## dfs 롣도 풀수 있지만, 비트마스크가 훨씬 빠른 알고리즘 
from itertools import combinations
def convert(s):
    s = int(s)
    if s == 0:
        return float('inf')
    return s
#입력을 int형으로 바꿔주고, 0을 inf 로 바꿔줌
n = int(input())
w = [list(map(convert,input().split())) for i in range(n)]
C = {}#딕셔너리 선언

def TSP(n, w):
    #n은 도시의 개수, w는 비용
    for k in range(1, n):#k는 1부터 n-1
        C[(1+(1<<k),k)] = w[0][k]#딕셔너리 키값은 2의k승*1+1,k
    for s in range(2, n+1):#s는 1부터 n까지
        for S in combinations(range(1,n), s):#S는 1부터 n-1까지 중에 s개 조합 튜플
            val = sum(1<<k for k in S)+1
            for k in S:
                C[(val,k)] = min(C[(val-(1<<k),m)]+w[m][k] for m in S if m!=0 and m!=k)
    return min(C[((2<<n-1)-1,k)] + w[k][0] for k in range(1,n))

print(TSP(n,w)) 
