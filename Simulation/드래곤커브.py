#드래곤 커브의 정보 x,y,d,g x,y는 드래곤 커브의 시작 점, d는 시작 방향,g는 세대
# 드래곤 커브는 격자 밖으로 벗어나지 않고 겹칠 수 있다.
# 15685 
#
# 1. 방향 리스트와 좌표리스트를 따로 만든다.
# 2. 주어진 시작좌표와 방향에따라 1세대 드래곤
# 3. for d in range(num-1,-1,-1): 방향 배열에 90도 돌려서, 역순으로 계속 추가 시킴
# 4. 방향배열 추가 할때마다 맵에 드래곤 표시
# 5. 완료후 사각형을 세어준다.
#
# Tip
# 1. 이동방향이 [(0,1),(-1,0),(0,-1),(1,0)] 일 경우 90 도 회전하면 [(-1,0),(0,-1),(1,0),(0,1)]
# 2. x,y = co,ro 이다. 
# 3. 90도 회전했을때, 방향 순서가 1203 이면 0132가 추가 된다.
#
# f
#

dro = [0,-1,0,1]
dco = [1,0,-1,0]
N = int(input()) #드래곤 커브의 개수
DC = [list(map(int,input().split())) for _ in range(N)]
Map = [[0]*101 for _ in range(101)]

direct = []
current = [0,0]
for co,ro,dire,gene in DC: #x = co, y = ro
    direct = []
    Map[ro][co] = 1
    direct.append(dire)
    nro = ro + dro[dire]
    nco = co + dco[dire]
    Map[nro][nco] = 1
    current[0] = nro
    current[1] = nco
    for i in range(gene):
        num = len(direct)
        for d in range(num-1,-1,-1):
            nro = current[0] + dro[(direct[d]+1)%4]
            nco = current[1] + dco[(direct[d]+1)%4]
            if 0 <= nro <= 100 and 0 <= nco <= 100:
                Map[nro][nco] = 1
                current[0] = nro
                current[1] = nco
                direct.append((direct[d]+1)%4)
    # print(direct)
    # print(Map)

ans = 0
for i in range(100):
    for j in range(100):
        if Map[i][j] == 1:
            if Map[i+1][j] and Map[i][j+1] and Map[i+1][j+1]:
                ans += 1
print(ans)
