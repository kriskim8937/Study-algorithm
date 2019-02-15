
# import sys
# import itertools
# while True :
#     n = list(map(int,sys.stdin.readline().split()))
#     a = n[0]
#     if a == 0:
#         break
#     b = n[1:]
#     combi = list(itertools.combinations(b, 6))
#     for i in range(len(combi)) :
#         for j in combi[i]:
#             print(j, end=' ')
#         print('')
#     print('')    
   


#1_ n = 5, path = [5]
        #2_ n = 4, path = [5,4]
        #3_ n = 10, path = [5,10]
        #4_ n = 6, path = [5,6]
#print(bfs(5,17))
# 
#         
# import sys
# def bfs(start,end):
#     queue = [(start,[start])]
#     while queue:
#         n, path = queue.pop(0)        
#         if n == end:
#             return path
#         else:
#             for m in set([n*2,n+1,n-1]) - set(path):
#                 queue.append((m,path + [m]))
# n, m = list(map(int,sys.stdin.readline().split()))
# print(len(bfs(n,m))-1)

import sys
import queue
def bfs(start,end):
    visited =[None]*100001
    dis = 0
    q = queue.Queue()
    q.put((start,dis))
    while q:
        n, dis = q.get(0)        
        if n == end:
            return dis
        if visited[n+1] != True:
            visited[n+1] = True
            q.put((n+1,dis+1))
        if visited[n-1] != True and n>0:
            visited[n-1] = True
            q.put((n-1,dis+1))
        if visited[n*2] != True:
            visited[n*2] = True
            q.put((n*2,dis+1))
            
                       
n, m = list(map(int,sys.stdin.readline().split()))
print((bfs(n,m)))
