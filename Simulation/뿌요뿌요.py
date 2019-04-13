# 뿌요뿌요
#
# 1. board != '.'인경우 즉 뿌요가 있는 경우 체인 탐색
# 2. 색깔이 같으면 그 좌표값을 chain에 계속 추가
# 3. 다음 좌표 탐색 ( 이전에 탐색한 방향으로 돌아가지 못하게 함)
# 4. chain의 길이가 4이상 되면 뿌요들을 전부 . 로 바꾸어줌 그리고 chains에 chain 저장
# 5. 1-4를 반복하고 chains의 길이가 0이 아니면 카운트 += 리빌드 실행
# 6. 길이 12의 큐를 만들고, 거기에 뿌요들만 탐색해서 집어넣음, 그대로 다시 그줄에 삽입.. 오
# 7. chain 길이가 0 이면 break
#
#
# Tip
# 1. chain을 for 문 안에 정의해서 각각 탐색 할때마다 자동 초기화.


directions = [[-1, 0], [0, 1], [1, 0], [0, -1]] # north, east, south, west

board = [list(map(str, [*input()])) for _ in range (12)]

def color_chain(x, y, color, route, pre_dir):
    if 0 <= x < 12 and 0 <= y < 6:
        if board[x][y] == color:
            if [x, y] not in route: # 이거 좋음
                route += [[x, y]]
                for dir in directions:
                    if dir != pre_dir*(-1): # 다음 좌표 탐색 ( 이전에 탐색한 방향으로 돌아가지 못하게 함)
                        color_chain(x + dir[0], y + dir[1], color, route, dir)

def rebuild():
    for i in range(12):
        for j in range(6):
            que = ['.'] * 12
            for i in range(12):
                if board[i][j] != '.':
                    que.remove('.')##?
                    que.append(board[i][j])
            for i in range(12):
                board[i][j] = que[i]
count = 0

while True:
    chains = []
    for x in range(12):
        for y in range(6):
            if board[x][y] != '.':
                chain = []
                color_chain(x, y, board[x][y], chain, [0, 0])
                if len(chain) > 3:
                    for idx in chain:
                        board[idx[0]][idx[1]] = "."
                    chains += chain
    if len(chains) > 0:
        count += 1
        rebuild()
    else:
        break

print(count)
