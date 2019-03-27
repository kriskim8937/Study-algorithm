import itertools

def compute_min_chick_dist(houses_idx,ways):
    min=-1#초기화, 무조건 0보단 크다
    for way in ways:#한가지 방법 선택
        cur=0
        for house_idx in houses_idx:
            house_chick_min=-1
            for chick_idx in way:
                dis=distance(house_idx,chick_idx)
                if(house_chick_min==-1):
                    house_chick_min=dis
                if(house_chick_min>dis):
                    house_chick_min=dis

            cur+=house_chick_min
        if(min==-1):
            min=cur
        if(cur<min):
            min=cur
    return min

def distance(idx1,idx2):
    return abs(idx1[0]-idx2[0])+abs(idx1[1]-idx2[1])
n, m = map(int,input().split())#n 은 도시 크기, m 은 남아야하는 치킨집

arr=[]
for _ in range(n):
    arr.append(list(map(int,input().split())))

house_idx=[]
chick_idx=[]
for i in range(n):
    for j in range(n):
        if(arr[i][j]==1):#집
            house_idx.append((i,j))
        elif(arr[i][j]==2):#치킨집
            chick_idx.append((i,j))

way=list(itertools.combinations(chick_idx,m))#치킨집 중에서 m 개만 선택함

result=compute_min_chick_dist(house_idx,way)

print(result)
