from itertools import combinations
INF = float('INF')

def distance(a, b):
  return abs(a[0] - b[0]) + abs(a[1] - b[1])

n, m = map(int, input().split())

arr = [input().split() for i in range(n)]

house = []
chicken = []

for i in range(n):
  for j in range(n):
    if arr[i][j] == "1":
      house.append((i, j))
    elif arr[i][j] == "2":
      chicken.append((i, j))


dis = [ [INF] * len(chicken) for i in range(len(house)) ]

for i, h in enumerate(house): #반복문 사용시 몇 번째 반복문인지 확인이 필요할 수 있다. 이때 사용 (0,1) 리턴
  for j, c in enumerate(chicken):
    dis[i][j] = min(dis[i][j], distance(h, c))


ans = INF

for i in combinations(range(len(chicken)), m):
  s = 0
  for j in range(len(house)):
    c = INF
    for k in i:
      c = min(c, dis[j][k])
    s += c
  ans = min(ans, s)

print(ans)
