from collections import deque
import copy
read = lambda : input().strip()
T = int(read())
dro = [-1,1,1,-1]
dco = [1,1,-1,-1]
top = [-1]


def dfs(ro,co,state,BM,c1,c2,ct):
    if state == 3:#c1은 이미 0인 상태임
        # print(bin(BM>>1))
        # print(ro,co,state)
        if c1 > 0:
            nro = ro + dro[2] #2번 방향만 가능 
            nco = co + dco[2]
            if 0 <= nro < N and 0 <= nco < N :
                val = A[nro][nco]
                if BM & (1<<val) == 0 :
                    dfs(nro,nco,state,BM+(1<<val),c1-1,c2,ct+1)
        if c1 == 0:
            if c2 == 1:
                # print(bin(BM>>1))
                # print(ro + dro[3],co + dco[3],'end')
                # print(ct+1)
                if top[0] < ct+1:
                    top[0] = ct+1
                return 
            nro = ro + dro[3] #3번 방향만 가능 
            nco = co + dco[3]
            val = A[nro][nco]
            if BM & (1<<val) == 0 :
                dfs(nro,nco,state,BM+(1<<val),c1,c2-1,ct+1)
    if state == 0 :
        # print(ro,co,state)
        BM += (1<<A[ro][co])
        nro = ro + dro[0] #오른쪽 위 방향 
        nco = co + dco[0] 
        if 0 <= nro < N and 0 <= nco < N :
                val = A[nro][nco]
                if BM & (1<<val) == 0 :
                    dfs(nro,nco,state+1,BM+(1<<val),c1+1,c2,ct+1)
    if state == 1 :
        # print(bin(BM>>1))
        # print(ro,co,state)
        for j in range(2):
            nro = ro + dro[state-j] #지금 방향과 그 전 방향만 가능 
            nco = co + dco[state-j] #지금 방향과 그 전 방향만 가능
            if j == 0: #꺾는 경우    
                if 0 <= nro < N and 0 <= nco < N :
                    val = A[nro][nco]
                    if BM & (1<<val) == 0 :
                        dfs(nro,nco,state+1,BM+(1<<val),c1,c2+1,ct+1)
            if j == 1: #같은 방향
                
                if 0 <= nro < N and 0 <= nco < N :
                    val = A[nro][nco]
                    if BM & (1<<val) == 0 :
                        dfs(nro,nco,state,BM+(1<<val),c1+1,c2,ct+1)
    if state == 2:
        # print(bin(BM>>1))
        # print(ro,co,state)
        for j in range(2):
            nro = ro + dro[state-j] #지금 방향과 그 전 방향만 가능 
            nco = co + dco[state-j] #지금 방향과 그 전 방향만 가능
            if j == 0: #꺾는 경우    
                if 0 <= nro < N and 0 <= nco < N :
                    val = A[nro][nco]
                    if BM & (1<<val) == 0 :
                        dfs(nro,nco,state+1,BM+(1<<val),c1-1,c2,ct+1)
            if j == 1: #같은 방향
                if 0 <= nro < N and 0 <= nco < N :
                    val = A[nro][nco]
                    if BM & (1<<val) == 0 :
                        dfs(nro,nco,state,BM+(1<<val),c1,c2+1,ct+1)


## 비트 연산 (10101011,1111)(먹은디저트,방향4가지)



X = 1
while T:
    N = int(read())
    A = [list(map(int, read().split())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            dfs(i,j,0,0,0,0,0)
    print('#', end = '')
    print(X,top[0])
    top[0] = -1
    T -=1
    X +=1
