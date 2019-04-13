from collections import deque
import sys
sys.setrecursionlimit(100000)
N = int(input())
K = int(input())
apples = []
directions = []
for _ in range(K):
    r,c = map(int,input().split())
    apples.append([r,c])


L = int(input())
for _ in range(L):
    x,c = map(str,input().split())
    directions.append([x,c])

# print(apples)
# print(directions)


dirs = [[0,1],[-1,0],[0,-1],[1,0]] #동,북,서,남 (반시계)

count = [0]

def snake (r,c,dir,sbody):
    if len(sbody) == 0:
        sbody.append([r,c])
    # print(sbody)
    for i in range(len(directions)):
        if count[0] == int(directions[i][0]):
            if directions[i][1] == 'L':
                dir += 1
            else: dir -=1
    if 0 <= r+dirs[dir][0] <N and 0 <= c+dirs[dir][1] <N:
        nro = r+dirs[dir][0]
        nco = c+dirs[dir][1]
        if [nro, nco] in sbody:
            return
        sbody.append([nro, nco])
        count[0] += 1
        if [nro+1,nco+1] not in apples:
            sbody.popleft()

        snake(nro,nco,dir,sbody)
    else:
        return
body = deque()
snake(0,0,0,body)
print(count[0]+1)
