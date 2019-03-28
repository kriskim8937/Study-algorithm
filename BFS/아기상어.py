
from sys import stdin
from heapq import heappush, heappop
input = stdin.readline

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
q = [] #heap 의 역할 

def init():
    for i in range(n):
        for j in range(n):
            if a[i][j] == 9: #9는 아기상어의 위치
                heappush(q, (0, i, j)) #q에다가 튜플을 넣음 
                a[i][j] = 0
                return

def bfs():
    body, eat, ans = 2, 0, 0
    check = [[False]*n for _ in range(n)]#간곳을 체크해주는 배열 
    while q:
        d, x, y = heappop(q)
        if 0 < a[x][y] < body:#칸에 물고기가 있고 몸보다 작으면 
            eat += 1
            a[x][y] = 0#먹어치움 
            if eat == body:#먹은 스택= 몸이면 성장 
                body += 1
                eat = 0
            ans += d #먹기까지 이동거리 = 시간 
            d = 0
            while q:
                q.pop()
            check = [[False]*n for _ in range(n)]
        for dx, dy in (-1, 0), (0, -1), (1, 0), (0, 1):
            nd, nx, ny = d+1, x+dx, y+dy
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if 0 < a[nx][ny] > body or check[nx][ny]:
                continue
            check[nx][ny] = True
            heappush(q, (nd, nx, ny))
    print(ans)

init()
bfs()
