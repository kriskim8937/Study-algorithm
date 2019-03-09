#삼성기출문제 
read = lambda : input().strip()
N, L, R = map(int, read().split())
Map = [list(map(int, read().split())) for _ in range(N)]

visit = [[0]*N for _ in range(N)]

Unions = []
dro = [1,-1,0,0]
dco = [0,0,1,-1]

def dfs(r,c):
    stack = [[r,c]]
    Union = [[r,c]]
    visit[r][c] = 1
    while stack:
        ro, co = stack.pop()
        for i in range(4):
            nro = dro[i] + ro
            nco = dco[i] + co
            if 0 <= nro < N and 0 <= nco < N:
                if L<= abs(Map[nro][nco]-Map[ro][co]) <=R:
                    if visit[nro][nco] == 0:
                        visit[nro][nco] = 1
                        stack.append([nro,nco])
                        Union.append([nro,nco])
    if len(Union) > 1:
        Unions.append(Union)

def Unite():
    sum = 0
    for uni in Unions:
        for nara in uni:
            sum += Map[nara[0]][nara[1]]
        for nara in uni:
            Map[nara[0]][nara[1]] = sum//len(uni)
        sum = 0



count = 0
while True:
    for i in range(N):
        for j in range(N):
            if visit[i][j] == 0:
                dfs(i,j)
    if len(Unions) == 0:
        print(count)
        break
    
    Unite()
    Unions = []
    Union = []
    visit = [[0]*N for _ in range(N)]
    count += 1

