#딕셔너리 써서 풀려다가 망함
# 충돌은 동일 좌표를 의미하는데 key는  동일 좌표를 같는 것이 불가능 

#원자 충돌 에너지 방출 소멸
#고유 움직이는 방향 상하 좌우
#1초에 1이동
#두개 이상 출동 에너지 방출  소멸

read = lambda : input().strip()
check = []
def time():
    for i in range(len(Keys)):
        if Atom[(Keys[i][0],Keys[i][1])][0] == 0:
            if Atom.get((Keys[i][0],Keys[i][1]+1)) != None :
                if Atom[(Keys[i][0],Keys[i][1]+1)][0] == 1:
                    explo()
                    continue
                else:
                    check.append([Keys[i][0], Keys[i][1], Keys[i][0], Keys[i][1]+1]+Atom[(Keys[i][0], Keys[i][1])]+[i])
                    Keys[i] = [0]
                    continue
            a = Atom.pop((Keys[i][0],Keys[i][1]))
            Atom[(Keys[i][0],Keys[i][1]+1)] = a
            Keys[i][1] += 1
        elif Atom[(Keys[i][0], Keys[i][1])][0] == 1:
            if Atom.get((Keys[i][0],Keys[i][1]-1)) != None :
                if Atom[(Keys[i][0],Keys[i][1]-1)][0] == 0:
                    explo()
                    continue
                else:
                    check.append([Keys[i][0], Keys[i][1], Keys[i][0], Keys[i][1]-1]+Atom[(Keys[i][0], Keys[i][1])]+[i])
                    Keys[i] = [0]
                    continue
            a = Atom.pop((Keys[i][0], Keys[i][1]))
            Atom[(Keys[i][0] , Keys[i][1]-1)] = a
            Keys[i][1] -= 1
        elif Atom[(Keys[i][0], Keys[i][1])][0] == 2:
            if Atom.get((Keys[i][0]-1,Keys[i][1])) != None :
                if Atom[(Keys[i][0]-1,Keys[i][1])][0] == 3:
                    explo()
                    continue
                else:
                    check.append([Keys[i][0], Keys[i][1], Keys[i][0]-1, Keys[i][1]]+Atom[(Keys[i][0], Keys[i][1])]+[i])
                    Keys[i] = [0]
                    continue
            a = Atom.pop((Keys[i][0], Keys[i][1]))
            Atom[(Keys[i][0]-1, Keys[i][1])] = a
            Keys[i][0] -= 1
        elif Atom[(Keys[i][0], Keys[i][1])][0] == 3:
            if Atom.get((Keys[i][0]+1,Keys[i][1])) != None :
                if Atom[(Keys[i][0]+1,Keys[i][1])][0] == 2:
                    explo()
                    continue
                else :
                    check.append([Keys[i][0], Keys[i][1],Keys[i][0]+1, Keys[i][1]]+Atom[(Keys[i][0], Keys[i][1])]+[i])
                    Keys[i] = [0]
                    continue
            a = Atom.pop((Keys[i][0], Keys[i][1]))
            Atom[(Keys[i][0]+1, Keys[i][1])] = a
            Keys[i][0] += 1
    print(check)
    for k in check:
        del Atom[(k[0],k[1])]
    for k in check:
        Atom[(k[2],k[3])] = [k[4],k[5]]
        Keys[k[6]] = [k[2],k[3]]
    print(Atom)



def explo():
    print('boom!')

T = int(read())
Atom = {}
Keys = []
while T:
    N = int(read())
    Map = [list(map(int, read().split())) for _ in range (N)]
    for i in range(N):
        if Atom.get((Map[i][0],Map[i][1])) == None:
            Atom[(Map[i][0],Map[i][1])] = [Map[i][2],Map[i][3]]
            Keys.append([Map[i][0],Map[i][1]])
    print(Atom)
    print(Keys)
    time()
    print(Atom)
    print(Keys)
    Atom = {}
    Keys = []
    T -= 1


