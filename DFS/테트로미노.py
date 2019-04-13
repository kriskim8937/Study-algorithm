#테트로미노
#그냥 길이4로 dfs 때리기 
#
#
#



N, M= map(int,input().split())
Matrix = [list(map(int,input().split())) for _ in range (N)]
visit = [[0]*M for _ in range(N)]


ans = [0]


def dfs(r,c,count,temp):
    if count == 3:
        ans[0] = max(ans[0],temp)
        return
    visit[r][c] = 1
    dro = [0,0,1,-1]
    dco = [1,-1,0,0]
    for i in range(4):
        nro = dro[i] + r
        nco = dco[i] + c
        if (0 <= nro < N) and (0 <= nco < M):
            if visit[nro][nco] == 0:
                visit[nro][nco] = 1
                dfs(nro,nco,count+1,temp+Matrix[nro][nco])
                dfs(r, c, count+1, temp + Matrix[nro][nco])
                visit[nro][nco] = 0


for i in range(N):
    for j in range(M):
        dfs(i, j, 0, Matrix[i][j])

print(ans[0])
