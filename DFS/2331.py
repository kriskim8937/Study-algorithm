#2231 반복수열
import sys
visit = {}
def DFS(From,rule,count):
    if visit.get(From)== None:
        visit[From] = 0
    To = 0
    for k in str(From).strip():
        To += int(k)**rule 
    #print(To) 
    if visit.get(To) != None:
        print(visit.get(To))
        return 
    if visit.get(To)== None:
        visit[To] = count
        count +=1
        DFS(To,rule,count)



A, B = map(int, sys.stdin.readline().split())
DFS(A,B,1)
print(visit)

## 주의할점
##맨처음에 넣는 값을 visit 
