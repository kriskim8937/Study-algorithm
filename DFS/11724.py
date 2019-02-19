# 연결 요소의 개수문제
# 

import sys
sys.setrecursionlimit(10**6)
adjLst = {}
visit = {}
def DFS(start):
    visit[start] = True
    #print(start, end = ' ')
    if adjLst.get(start) == None:
        return
    for i in adjLst[start]:
        if visit.get(i) == None:
            DFS(i)




N, M = map(int,sys.stdin.readline().split())
for _ in range(M):
    From, To = map(int,sys.stdin.readline().split())
    if adjLst.get(From) == None:
        adjLst[From] = []
    adjLst[From].append(To)
    if adjLst.get(To) == None:
        adjLst[To] = []
    adjLst[To].append(From)
#print(adjLst)
DFS(1)
count = 1
for i in range(1,N+1):
    if visit.get(i) == None:
        DFS(i)
        count += 1
        #print()
print(count)

# 테스트 케이스 
# 6 2
# 3 4
# 4 2
# 
