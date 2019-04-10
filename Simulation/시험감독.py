# 시험 감독
# 백준 13458
# 1. 각 시험장 인원수에서 시험감독관이 커버할수 있는 수 B를 뺀다.
# 2. 남은 수가 1 이상이면 보조 감독관이 커버할수 있는수 C로 나누고 1을더함
# 3. 그 수들을 전부 더한 것이 답

N = int(input())
test = list(map(int, input().split()))
B,C = list(map(int, input().split()))

count = 0

for i in range(len(test)):
    test[i] -= B
    count += 1
    temp  = test[i]
    if temp > 0 :
        count += (temp // C)
        if (temp%C) != 0:
            count += 1
print (count)
