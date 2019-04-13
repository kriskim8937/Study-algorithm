N = int(input())
Consult = [list(map(int, input().split())) for _ in range(N)]

maxN = [0]

def dfs(day, money) :
    if day == N:
        maxN[0] = max(money, maxN[0])
        return
    dfs(day+1, money)
    if day + Consult[day][0] <= N:
        dfs(day + Consult[day][0], money + Consult[day][1])

dfs(0,0)
print (maxN[0])
