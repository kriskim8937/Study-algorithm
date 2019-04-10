# 1.구슬의 위치, 벽의 위치, 빈칸, 구멍의 위치를 입력받는다
# 2. 10번안에 못 옮기면 -1 출력
# 3. 10번의 경우의 수는 동서남북 4^10 = 2^20 == 100만
#
# Tip
# 1. 빨간 구슬 파란 구슬은 겹치지 않는다.
# 2. 빨간 파란 구슬은 동서남북 네가지 방향중 하나로 함께 움직인다
# 3. 파란구슬이 구멍에 들어가면 실패한다.
# 4. 문자열을 분해해서 입력 받아야한다.
# 5. B좌표, R 좌표, count 를 입력으로 받는 재귀 함수로 구현
# 6. 최단 이동을 찾아야 하기 때문에 bfs가 유리하다.

from collections import deque

R = []
B = []
O = []
Flag = [0,0,0] #구멍 위를 지나가는지에대한 플래그  A만 셋되면 count 출력 B가 셋되면 -1

def left(r1,r2,b1,b2):
    n = 2
    while n:
        while Map[r1][r2-1] == '.' and (r1 != b1 or r2-1 != b2):
            r2 -= 1
            if r1 == O[0] and r2 == O[1]:
                Flag[0] = 1
        while Map[b1][b2 - 1] == '.' and (b1 != r1 or b2-1 != r2):
            b2 -= 1
            if b1 == O[0] and b2 == O[1]:
                Flag[1] = 1
                return -1,-1,-1,-1
        n -= 1
    return r1,r2,b1,b2

def right(r1,r2,b1,b2):
    n = 2
    while n:
        while Map[r1][r2+1] == '.' and (r1 != b1 or r2+1 != b2):
            r2 += 1
            if r1 == O[0] and r2 == O[1]:
                Flag[0] = 1
        while Map[b1][b2 + 1] == '.' and (b1 != r1 or b2+1 != r2):
            b2 += 1
            if b1 == O[0] and b2 == O[1]:
                Flag[1] = 1
                return -1,-1,-1,-1
        n -= 1
    return r1, r2, b1, b2

def up(r1,r2,b1,b2):
    n = 2
    while n:
        while Map[r1-1][r2] == '.' and (r1-1 != b1 or r2 != b2):
            r1 -= 1
            if r1 == O[0] and r2 == O[1]:
                Flag[0] = 1
        while Map[b1-1][b2] == '.'and (b1-1 != r1 or b2 != r2):
            b1 -= 1
            if b1 == O[0] and b2 == O[1]:
                Flag[1] = 1
                return -1,-1,-1,-1
        n -= 1
    return r1, r2, b1, b2

def down(r1,r2,b1,b2):
    n = 2
    while n:
        while Map[r1+1][r2] == '.' and (r1+1 != b1 or r2 != b2):
            r1 += 1
            if r1 == O[0] and r2 == O[1]:
                Flag[0] = 1
        while Map[b1+1][b2] == '.'and (b1+1 != r1 or b2 != r2):
            b1 += 1
            if b1 == O[0] and b2 == O[1]:
                Flag[1] = 1
                return -1,-1,-1,-1
        n -= 1
    return r1, r2, b1, b2

# def escape(r1,r2,b1,b2,count,dire):
#     #기울이는 방향 dire 1,2,3,4 왼오위아래
#
#     # for dro,dco in [(1,0),(0,1),(-1,0),(0,-1)]:
#     #     if r1+dro == O[0] and r2+dco == O[1]:
#     #         print('finish')
#     #         print(count+1)
#     #         return
#     if flag[0] == 1:
#         return
#     if r1 == O[0] and r2 == O[1]:
#         print('finish')
#         print(count)
#         flag[0] = 1
#         return
#
#     if count == 10:
#         print(-1)
#         return
#     if dire == 0 or dire == 3 or dire == 4:
#         if Map[r1][r2-1] == '.'or Map[b1][b2 - 1] == '.':
#             rl1,rl2,bl1,bl2 = left(r1,r2,b1,b2)
#             print(rl1,rl2,bl1,bl2,count)
#             escape(rl1,rl2,bl1,bl2, count + 1, 1)
#     if dire == 0 or dire == 3 or dire == 4:
#         if Map[r1][r2+1] == '.'or Map[b1][b2 + 1] == '.':
#             rr1, rr2, br1, br2 = right(r1, r2, b1, b2)
#             print(rr1, rr2, br1, br2, count)
#             escape(rr1, rr2, br1, br2, count + 1, 2)
#     if dire == 0 or dire == 1 or dire == 2:
#         if Map[r1-1][r2] == '.'or Map[b1-1][b2] == '.':
#             ru1, ru2, bu1, bu2 = up(r1, r2, b1, b2)
#             print(ru1, ru2, bu1, bu2, count)
#             escape(ru1, ru2, bu1, bu2, count + 1, 3)
#     if dire == 0 or dire == 1 or dire == 2:
#         if Map[r1+1][r2] == '.'or Map[b1+1][b2] == '.':
#             rd1, rd2, bd1, bd2 = down(r1, r2, b1, b2)
#             print(rd1, rd2, bd1, bd2, count)
#             escape(rd1, rd2, bd1, bd2, count + 1, 4)

def escape(r1,r2,b1,b2,count,dire):
    q = deque([(r1,r2,b1,b2,count,dire)])
    while q:
        Flag = [0,0,0]
        if count == 10 :
            count = -1
            break
        if r1 == O[0] and r2 == O[1]:
            break
        r1,r2,b1,b2,count,dire = q.popleft()
        if dire == 0 or dire == 3 or dire == 4:
            if Map[r1][r2 - 1] == '.' or Map[b1][b2 - 1] == '.':
                rl1, rl2, bl1, bl2 = left(r1, r2, b1, b2)
                print(rl1, rl2, bl1, bl2, count)
                if Flag[1] == 1:
                    Flag[2] += 1
                elif Flag[0] == 1:
                    count += 1
                    break
                else:
                    q.append((rl1, rl2, bl1, bl2, count + 1, 1))
        if dire == 0 or dire == 3 or dire == 4:
            if Map[r1][r2 + 1] == '.' or Map[b1][b2 + 1] == '.':
                rr1, rr2, br1, br2 = right(r1, r2, b1, b2)
                print(rr1, rr2, br1, br2, count)
                if Flag[1] == 1:
                    Flag[2] += 1
                elif Flag[0] == 1:
                    count += 1
                    break
                else:
                    q.append((rr1, rr2, br1, br2, count + 1, 2))
        if dire == 0 or dire == 1 or dire == 2:
            if Map[r1 - 1][r2] == '.' or Map[b1 - 1][b2] == '.':
                ru1, ru2, bu1, bu2 = up(r1, r2, b1, b2)
                print(ru1, ru2, bu1, bu2, count)
                if Flag[1] == 1:
                    Flag[2] += 1
                elif Flag[0] == 1:
                    count += 1
                    break
                else:
                    q.append((ru1, ru2, bu1, bu2, count + 1, 3))
        if dire == 0 or dire == 1 or dire == 2:
            if Map[r1 + 1][r2] == '.' or Map[b1 + 1][b2] == '.':
                rd1, rd2, bd1, bd2 = down(r1, r2, b1, b2)
                print(rd1, rd2, bd1, bd2, count)
                if Flag[1] == 1:
                    Flag[2] += 1
                elif Flag[0] == 1:
                    count += 1
                    break
                else :
                    q.append((rd1, rd2, bd1, bd2, count + 1, 4))
        print(q)
        if Flag[2] == 4:
            count = -1
            break
    print('finish')
    print(count)
    return






N,M = map(int,input().split())
Map = [list(map(str,[*input()])) for _ in range(N)]

flag = [0,0] #구슬 찾음 플래그
print(Map)
for i in range(N):
    for j in range(M):
        if Map[i][j] == "R":
            Map[i][j] = "."
            R = [i,j]
        if Map[i][j] == "B":
            Map[i][j] = "."
            B = [i,j]
        if Map[i][j] == "O":
            Map[i][j] = "."
            O = [i,j]

print(R,B,O)
escape(R[0],R[1],B[0],B[1],0,0)
