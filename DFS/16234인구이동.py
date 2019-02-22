#삼성기출문제 
import sys
sys.setrecursionlimit(10**6)
visit = [[0]*1000 for i in range(1000)]
lis =  [0,0] #총 인구수 , 연합 국가수
lis2 = []
def DFS(matrix,x,y,count):
  if visit[x][y] == 1:
    return
  visit[x][y] = 1
  lis[0] += matrix[x][y]
  lis[1] += 1
  lis2.append([x,y])
  #print(lis)
  d_x = [1,-1,0,0]
  d_y = [0,0,-1,1]
  for i in range(4):
    nx = x+d_x[i]
    ny = y+d_y[i]
    if nx >= 0 and nx < N and ny >=0 and ny < N:
      #print(matrix[x][y]-matrix[nx][ny])
      if L <= abs(matrix[x][y]-matrix[nx][ny]) <= R:
        if visit[nx][ny]== 0:
          DFS(matrix,nx,ny,count+1)
  return




read = lambda : sys.stdin.readline().strip()
#split()을 사용하면 리스트로 만들어줌 
N,L,R = map(int, read().split())
matrix = [list(map(int,read().split())) for _ in range(N)]
move = False# 인구이동이 있었는가
moveCount = 0#총 인구 이동 횠수
Flag = True
while Flag:
  for i in range(N):
    for j in range(N):
      DFS(matrix,i,j,1)
      if lis[1] > 1:
        for t in lis2:
          matrix[t[0]][t[1]]=lis[0]//lis[1]
        move = True
      lis = [0,0]
      lis2 = []
      #print(matrix)
  if move == True: 
    moveCount +=1
    move = False
  else: #이동이 한번도 없으면 while문 탈출
    Flag = False
  #print(moveCount)
  visit = [[0]*1000 for i in range(1000)]
print(moveCount)


