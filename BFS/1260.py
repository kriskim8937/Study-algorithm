#1260 BFS
from collections import deque


visitDFS = {}
visitBFS = {}
adLst = {}

def DFS(start) :
    visitDFS[start] = True
    print(start, end = ' ')
    for i in adLst[start]:
        if visitDFS.get(i) == None:
            DFS(i)


def BFS(start) :
    q = deque()
    q.append(start)
    visitBFS[start] = True
    while q:
        nextNode= q.popleft()
        print(nextNode, end = ' ')
        for i in adLst[nextNode]:
            if visitBFS.get(i) == None:
                q.append(i)
                visitBFS[i] = True
                







N, M, V  = map(int,input().split())
for _ in range(M):
    From, To =  map(int,input().split())
    if adLst.get(From) == None:
        adLst[From] =[]
    if adLst.get(To) == None:
        adLst[To] =[]
    adLst[From].append(To)
    adLst[To].append(From)

for i in adLst:
    adLst[i].sort()

DFS(V)
print()
BFS(V)
