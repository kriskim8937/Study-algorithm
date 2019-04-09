import itertools
import copy
# 빈 공간에 3개의 벽을 세우는 모든 경우의 마다 안전구역을 측정함 0이 n개라면 nC3 의 경우의 수가 있다
# 1. combination 을 이용하여 벽을 세운다.
# 2. 바이러스 근원지(2)에서 bfs 혹은 dfs 로 바이러스 확산(5할당)
# 3. Map에서 0의 개수를 세고, ans와 비교해서 클 경우에만 ans 갱신

# 팁
# 1. 바이러스 근원지(2)의 위치를 저장해 놈 -> 매번 탐색할 필요가 없음 -> 시간 단축
# 2. Map은 깊은 복사를 해야 만이 복사본에 값을 할당하거나 append 했을때 원본이 안바뀜

N,M = map(int, input().split()) #세로크기 , 가로 크기
Map = [list(map(int, input().split())) for _ in range(N)]
visit = [[-1]*M for _ in range(N)]
virus = []
empty = []
ans = [0]
def dfs(ro,co):
    for dro, dco in ((0, 1), (0, -1), (1, 0), (-1, 0)):  # 동서 남북 순서로 탐색
        if -1 < ro + dro < N and -1 < co + dco < M:
            nro, nco = ro + dro, co + dco
            if visit[nro][nco] < 0 and Map2[nro][nco] == 0:
                Map2[nro][nco] = 5
                visit[nro][nco] += 1
                dfs(nro,nco)

for i in range(N):
    for j in range(M):
        if Map[i][j] == 2:
            virus.append((i,j))
        if Map[i][j] == 0:
            empty.append((i,j))
for emp in list(itertools.combinations(empty,3)):
    count = 0
    Map2 = copy.deepcopy(Map)  # 깊은 복사를 하지않으면 내부 값에 할당, append등 사용하면 원본도 바뀜
    for cor in emp:
        Map2[cor[0]][cor[1]] = 3
    for ro,co in virus:
        dfs(ro,co)
    for ro,co in empty:
        if Map2[ro][co] == 0:
            count += 1
    ans[0] = max(ans[0],count)
    visit = [[-1] * M for _ in range(N)]

print(ans[0])
