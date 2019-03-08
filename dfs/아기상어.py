import sys, copy
from collections import deque
read = lambda : sys.stdin.readline()

N = int(read())
matrix = [list(map(int, read().split())) for i in range(N)]
visitBFS = copy.deepcopy(matrix)
Flag = [True]
answer = [0]
#dfs를 이용해서 자기봗 작은 물고기의 위치들을 구한다
# 이중에 최고로 가까운 거리에 있는 물고기를 먹으로 간다

nextstart = [0,0,2,0,0]#row,col좌표,현재 물고기 사이즈, 총 이동거리, 먹은 물고기 수 
#최단거리는 bfs를 사용 하여 구할 수 있다.
def bfs(ro,co,size,count):#아기 상어의 좌표와 사이즈 , 이동거리 
    
    visitBFS = copy.deepcopy(matrix)#초기화
    # visitBFS = [list(map(int, visitBFS[i])) for i in range(N)]
    # print(visitBFS)
    flag2 = True
    for j in range (N):
        for i in range (N):
            if visitBFS[i][j] != 0:
                # print(visitBFS[i][j])
                flag2 = False
                break 
    if flag2 == True:
        Flag[0] = False
        # print('out of fish')
        print(answer[0])
        return
    q= deque()
    q.append([ro,co,count])
    if visitBFS[ro][co] == 0:    
        visitBFS[ro][co] = 99#지나온 길이라는 의미
    while q:
        nextNode = q.popleft()
        #######################
        # if nextNode[2] == 62:
        #     Flag[0] = False
        #     return
        #########################
        # print(nextNode)
        if 0 < matrix[nextNode[0]][nextNode[1]] < size:
            nextstart[0] = nextNode[0] #상어 row 좌표
            nextstart[1] = nextNode[1] #상어 col 좌표
            nextstart[3] = nextNode[2] #상어 총 이동 칸수
            matrix[nextNode[0]][nextNode[1]] = 0#상어가 먹은칸0으로 
            # print('ate 1 fish')
            nextstart[4] += 1#상어가 먹은 물고기 수
            if nextstart[4] == nextstart[2]:
                # print('Grow up!!')
                nextstart[4] = 0 #먹은 물고기 리셋
                nextstart[2] +=1 #상어 크기 업
            return 
        dro = [-1,0,0,1]
        dco = [0,-1,1,0]
        for i in range(4):
            nro =nextNode[0]+dro[i]
            nco = nextNode[1]+dco[i]
            if 0 <= nro < N and 0 <= nco < N :
                if visitBFS[nro][nco] <=size:
                    q.append([nro,nco,nextNode[2]+1])
                    visitBFS[nro][nco] = 8
                    count += 1
    # print('out of fish')
    print(answer[0])
    Flag[0] = False
    return

def hunt (ro,co,size,count):
    bfs(ro,co,size,count)
    while Flag[0]:
        # print (nextstart)
        answer[0] = nextstart[3]
        bfs(nextstart[0],nextstart[1],nextstart[2],nextstart[3]) 
        


# print(visitBFS)
for j in range(N):
    for i in range(N):
        if matrix[i][j] == 9:
            matrix[i][j] = 0
            hunt(i,j,2,0)
# print(visitBFS)
# print(matrix)
# print(nextstart)
#메모리 초과 오류 발생 : 

