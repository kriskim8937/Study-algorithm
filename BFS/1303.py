import sys
from collections import deque
read = lambda : sys.stdin.readline().strip()
N,M = map(int, read().split())
matrix = [list(map(str,[*read()])) for _ in range(M)]
check = [list([int(0)]*N) for _ in range(M)]
count= [0,0]#W,B

def bfs(i,j):
    
    dro = [1,-1,0,0]
    dco = [0,0,1,-1]
    q = deque([(i,j)])
    t = 1
    check[i][j] = 1
    while q:
        ro, co = q.popleft()
        for i in range(4):
            nro = ro + dro[i]
            nco = co + dco[i]
            if 0 <= nro <M and 0 <= nco <N:
                if matrix[nro][nco] == matrix[ro][co]:
                    
                    if check[nro][nco] == 0:
                        check[nro][nco] = 1 
                        
                        q.append((nro,nco))
                        t+=1
    return t
W,B = 0,0
for j in range(N):
    for i in range(M):
        if check[i][j] == 0:
            ans = bfs(i,j)
            if matrix[i][j]=='W': W+=ans**2
            else: B+=ans**2

print(W,B)
