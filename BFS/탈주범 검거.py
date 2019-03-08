from collections import deque
read = lambda : input().strip()

T = int(read())

pipe ={
    1:[[1,-1,0,0],[0,0,1,-1]],
    2:[[1,-1],[0,0]],
    3:[[0,0],[1,-1]],
    4:[[-1,0],[0,1]],
    5:[[1,0],[0,1]],
    6:[[1,0],[0,-1]],
    7:[[-1,0],[0,-1]]}

toca = [0]

def bfs(r,c,l):
    count = 0
    q = deque([(r,c,count)])
    t = 1
    Map2[r][c] = 1
    while q:
        ro,co,count = q.popleft()
        if count == (l-1):
            Map2[r][c] == 0
            return
        num = Map[ro][co]
        for i in range(len(pipe[num][0])):
            nro = ro + pipe[num][0][i]
            nco = co + pipe[num][1][i]
            if 0 <= nro < N and 0 <= nco < M:
                if Map[nro][nco] != 0:
                    num2 = Map[nro][nco]
                    for i in range(len(pipe[num2][0])):
                        nro2 = nro + pipe[num2][0][i]
                        nco2 = nco + pipe[num2][1][i]
                        if nro2 == ro and nco2 == co:
                            if Map2[nro][nco] == 0: 
                                Map2[nro][nco] = 1
                                toca[0] += 1
                                t += 1
                                q.append((nro,nco,count+1))
                                break
X = 1
while T:
    N, M, R, C, L = map(int, read().split())
    Map = [list(map(int, read().split())) for _ in range(N)]
    Map2 = [[0]*M for _ in range(N)]
    bfs(R,C,L)
    print('#',end = '')
    print(X,toca[0]+1)
    toca[0] =0 
    T -=1
    X +=1
