# 연산자 끼워넣기 [14888]
# 1. 수의 개수, N 순열 Nums, 사칙연산의 개수를 입력 받는다.
# 2. 중복순열을 어떻게 만들지?
# 3. 백트랙킹 사용
#
# Tip
# 1. 식의 계산은 연산자 우선 순위를 무시하고 앞에서부터 진행
# 2. 나눗셈은 정수 나눗셈으로 몫만 취한다.
# 3. 음수를 양수로 나눌때는 양수로 바꾼 뒤 몫을 취하고 그 몫을 음수로 바꾼것
# 4. 나눗셈을 c++ 과 같은 방식으로 하기 위해서 는   int(amount / num[idx])) 처럼 정수로 바꿔준다.
#

maxN = [-10000000000]
minN = [10000000000]

def dfs(idx, amount ):
    if idx == N:
        maxN[0] = max(maxN[0], amount)
        minN[0] = min(minN[0], amount)
        return

    if op[0] > 0 :
        op[0] -=1
        dfs(idx + 1, amount + num[idx])
        op[0] +=1

    if op[1] > 0 :
        op[1] -=1
        dfs(idx + 1, amount - num[idx])
        op[1] +=1

    if op[2] > 0 :
        op[2] -=1
        dfs(idx + 1, amount * num[idx])
        op[2] +=1

    if op[3] > 0 :
        op[3] -=1
        dfs(idx + 1, int(amount / num[idx]))
        op[3] +=1

        return 0




N = int(input())
num = list(map(int, input().split()))
op = list(map(int, input().split()))
dfs(1,num[0])
print(maxN[0])
print(minN[0])
