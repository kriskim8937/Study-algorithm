#1*1 땅에 나무가 많을수도 있다 
#봄에 나이 1증가
#나이가 어린 나무부터 양분 먹음
#자기 나이만큼 양분을 먹어야함, 아니면 죽ㅇㅁ
#여름에는 죽은나무가 양분 죽은나무 나이/2
#가을에는 나무가 번식 , 나무나이 5의 배수 인접 8칸 나이 1인 나무 생김 
#겨울에는 로봇이 땅에 양분을 추가

import sys
read = lambda : sys.stdin.readline().strip()
N,M,K = map(int, read().split())#NxN의 땅에, M개의 나무를 심음,K년이 지난후 살아있는 나무의 개수를 구하라
A = [list(map(int, read().split())) for _ in range(N)]#겨울에 심는 양분의 양과 좌표
B = {} #좌표를 key로 가지고, 나무의 나이를 value 로 하는 dictionary
for j in range(1, N+1):
    for i in range(1, N+1):
        B[(j,i)]=[]

for i in range(M):
    ro,co,age = map(int, read().split())
    B[(ro,co)].append(age)

energy = [[5]*N for _ in range(N)]
# SumrEnergy = [[0]*N for _ in range(N)]
# print (energy)
# print(A)

def Spring():
    for j in range(1,N+1):
        for i in range(1, N+1):
            # if B.get((i,j)) != None:
            B[(i,j)].sort()
            #lilen = len(B[(i,j)])
            for k in range(len(B[(i,j)])):
                # print(B[(i,j)][k],energy[i-1][j-1])
                if B[(i,j)][k] <= energy[i-1][j-1]:
                    energy[i-1][j-1] -= B[(i,j)][k]
                    B[(i,j)][k] += 1
                    # print('TreeGrow!!')
                else :
                    for P in B[(i,j)][k:]:
                        energy[i-1][j-1] += P//2
                        # print('At the (',i,j,')Energy' ,SumrEnergy[i-1][j-1],'saved!')
                    B[(i,j)] = B[(i,j)][:k]
                    break
                     

# def Summer() :
#     for i in range(N):
#         for j in range(N):
#             energy[i][j] += SumrEnergy[i][j]

def Autumn() :
    for j in range(1,N+1):
        for i in range(1, N+1):
            # if B.get((i,j)) != None:
                for k in range(len(B[(i,j)])):
                    if B[(i,j)][k]%5 == 0:
                        dro = [-1,-1,-1,0,0,1,1,1]
                        dco = [-1,0,1,-1,1,-1,0,1]
                        for p in range(8):
                            nro = dro[p]+i
                            nco = dco[p]+j
                            if 0 < nro <= N and 0 < nco <= N:
                                # print(nro,nco)
                                B[(nro,nco)].append(1)
                            
def Winter() :
    for i in range(N):
        for j in range(N):
            energy[i][j] += A[i][j]
    # print(energy)

while K:
    Spring()
    # Summer()
    Autumn()
    Winter()
    K -= 1

#### 남은 나무 숫자세기
TreeNum = 0
for j in range(1,N+1):
    for i in range(1, N+1):
        # if B.get((i,j)) != None:
            TreeNum += len(B[(i,j)])

print(TreeNum)

### 시간초과 발생
### 여름 함수를 없애고, 봄이랑 합쳐 중복 제거를 통해 해결!
