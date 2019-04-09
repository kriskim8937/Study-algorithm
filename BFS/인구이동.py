from collections import deque
#ctrl + R 문자 변경
# 1. 모든 지도 상의 국가를 하나씩 참조, visit 이 아닌 경우 bfs 실해
# 2. bfs를 통해서 인근 국가와 국경이 열리는지 파악
# 3. 모든 나라를 한번씩 순회후 만약 국경이 열렸었다면 인구수 합쳐서 나누고 그 값을 각각 나라에 저장
# 4. 다시 1부터 반복, 국경이 안열린다면 종료
# 백준 16234


N, L, R = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(N)]
visit = [[-1]*N for _ in range(N)]
ans = 0
update = [0]

def bfs(i,j):
    union = deque([(i,j)])
    q = deque([(i,j)])
    q_size = 1  # q 는 국경 열린 국가들 개수임
    while q:
        ro,co = q.popleft()
        for dro, dco in ((0, 1), (0, -1), (1, 0), (-1, 0)):#동서 남북 순서로 탐색
            if -1 < ro + dro < N and -1 < co + dco < N:
                nro, nco = ro + dro, co + dco
                if visit[nro][nco] < ans and L <= abs(Map[ro][co] - Map[nro][nco]) <= R:
                    #조건 충족
                    visit[nro][nco] += 1
                    q.append((nro, nco))
                    union.append((nro, nco))
                    q_size += 1
        #조건이 충족되는 다음 노드가 없으면 break
    if q_size > 1:
        update[0] += 1
        val = 0
        for ro, co in union:#q안에 국경열린 국가들 좌표 다 들어 있음
            val += Map[ro][co]
        val = val // q_size #국경 열린 국가들 개수임
        #결과값 구함
        for ro, co in union:
            Map[ro][co] = val

while True:
    update[0] = 0
    for i in range(N):
        for j in range(N):
            if visit[i][j] < ans:  # visit 을 초기화 시키지 않고 계속 쓸수 있는 꿀팁
                visit[i][j] += 1
                bfs(i,j)
    if update[0] > 0: #update 가 발생했다면,
        ans += 1
    else:
        break
print(ans)

#####################################################################################
#bfs 보다 빠른 알고리즘 사용
#함수를 사용하지 않음
#dequed와 popleft를 사용하지않고, 노드 리스트를 새로 만들어냄 -> 그래서 더빠름



N, L, R = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(N)]
visit = [[-1]*N for _ in range(N)]
ans = 0






while True:
    update = 0 #update 초기화
    for i in range(N):
        for j in range(N):
            if visit[i][j] < ans: #visit 을 초기화 시키지 않고 계속 쓸수 있는 꿀팁
                visit[i][j] += 1
                union, _q, q_size = [(i, j)], [(i, j)], 1 #q 는 국경 열린 국가들 개수임
                while True:
                    temp = []
                    for ro, co in _q:#이렇게 하면 _q안에 여러쌍의 (ro,co)가 있어도 전부 참조함
                        #앞의 값, 먼저 들어간 값부터 참조하니 bfs의 일종임
                        for dro, dco in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                            if -1 < ro + dro < N and -1 < co + dco < N:
                                nro, nco = ro + dro, co + dco
                                if visit[nro][nco] < ans and L <= abs(Map[ro][co] - Map[nro][nco]) <= R:
                                    #조건 충족
                                    visit[nro][nco] += 1
                                    temp.append((nro, nco))
                                    union.append((nro, nco))
                                    q_size += 1
                    if temp == []: break
                    #조건이 충족되는 다음 노드가 없으면 break
                    _q = temp
                if q_size > 1:
                    update += 1
                    val = 0
                    for ro, co in union:#q안에 국경열린 국가들 좌표 다 들어 있음
                        val += Map[ro][co]
                    val = val // q_size #국경 열린 국가들 개수임
                    #결과값 구함
                    for ro, co in union:
                        Map[ro][co] = val
    if update > 0: #update 가 발생했다면,
        ans += 1
    else: break
print(ans)
