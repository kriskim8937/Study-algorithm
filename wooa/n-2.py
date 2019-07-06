# 문제 설명
# 배열 arr1과 arr2가 주어집니다. 각 배열의 원소는 숫자 1부터 13까지로 이루어져 있습니다.
# 이 배열에서 2번 이상 페어로 나오는 숫자들을 비교해서 둘 중에 어느 쪽이 더 큰 값인지 확인해야 합니다.
# arr1 배열이 더 큰 값을 포함하면 1을, arr2 배열이 더 큰 값을 포함하고 있으면 2를 반환 하는 solution 함수를 완성해 주세요.
#
# 양쪽 배열에 모두 페어가 없으면 0을 반환하세요.
# 같은 숫자 2개가 페어로 나오는 경우보다는 3개가 페어로 나오는 경우가 더 큰 값이다.
# 같은 숫자 3개가 페어로 나오는 경우보다는 4개가 페어로 나오는 경우가 더 큰 값이다.
# 같은 숫자 5개이상 페어로 나오는 경우는 4개가 페어로 나오는 경우와 동일하게 취급한다.
# 양쪽 모두 같은 개수의 페어라면 더 큰 숫자가 큰 값이다.
# 숫자 페어가 2벌이 나오는 경우에는 더 큰 숫자로 되어있는 페어만 고려한다.
# 양쪽 배열에서 페어 숫자가 같으면 비교를 할 수 없으니 0을 반환하세요.
# 예를들면
# arr1 = [1, 5, 7, 2, 9, 13, 10]이고, arr2 = [2, 3, 9, 10, 4, 8, 11] 이면 페어가 없으니 0를 반환합니다.
# arr1 = [1, 4, 1, 3, 5, 6, 10]이고, arr2 = [9, 2, 3, 1, 3, 4, 10] 이면 숫자 3이 페어로 나온 2를 반환합니다.
# arr1 = [1, 1, 9, 4, 1, 3, 11]이고, arr2 = [2, 3, 3, 13, 12, 9, 9] 이면 숫자 1이 3번 페어로 나온 1을 반환합니다.
# arr1 = [1, 4, 9, 4, 1, 10, 13]이고, arr2 = [11, 13, 9, 3, 1, 9, 1] 이면 페어중에 큰 숫자 9가 나온 2를 반환합니다.
# arr1 = [1, 4, 4, 4, 1, 10, 4]이고, arr2 = [11, 13, 11, 3, 11, 9, 1] 이면 4가 4번 페어가 나온 1을 반환합니다.
# arr1 = [1,2,2,3,2,2,2]이고, arr2 = [4,5,4,5,4,5,4] 이면 4가 4번 페어가 나온 2를 반환합니다.
#
# solution 함수 이외에 필요한 함수를 추가해서 코드를 의미있는 단위로 분리해보세요.
#
# 제한사항
# 각 배열 arr의 크기 : 7
# 각 배열 arr의 원소의 크기 : 1보다 크거나 같고 13보다 작거나 같은 정수

import operator
def solution(arr1,arr2):
    A = countPair(arr1)
    B = countPair(arr2)
    answer = compareCard(A,B)
    return answer

def countPair(arr):
    cnt = []
    for i in range(1,14):
        if arr.count(i) <5:
            cnt.append((i,arr.count(i)))
        else:
            cnt.append((i, 4))
    # print(cnt)
    sortedCnt = sorted(cnt, key = operator.itemgetter(1),reverse = True)
    # print(sortedCnt)
    bestcard = sorted(pickBestPair(sortedCnt), reverse = True)[0]
    if bestcard[1] < 2:
        bestcard =()
    return bestcard

def pickBestPair(arr):
    cards = [arr[0]]
    for i in range(1,len(arr)):
        if arr[0][1] == arr[i][1]:
            cards.append(arr[i])
        else :
            return cards
    return cards

def compareCard(a,b):
    # lis = [a,b]
    # # print(lis)

    if a == b:
        return 0
    elif len(a) == 0:
        print('ss')
        return 2
    elif len(b) == 0:
        print('ff')
        return 1
    elif b[1] == a[1]:
        if a[0]>b[0]:
            return 1
        else : return 2
    else :
        if a[1]>b[1]:
            return 1
        else: return 2


arr1 = [1,1, 5, 7, 2, 9, 13, 10]
arr2 = [2, 3, 9, 10, 4, 8, 11] #이면 페어가 없으니 0를 반환합니다.
# arr1 = [1, 4, 1, 3, 5, 6, 10]
# arr2 = [9, 2, 3, 1, 3, 4, 10] #이면 숫자 3이 페어로 나온 2를 반환합니다.
# arr1 = [1, 1, 9, 4, 1, 3, 11]
# arr2 = [2, 3, 3, 13, 12, 9, 9] #이면 숫자 1이 3번 페어로 나온 1을 반환합니다.
# arr1 = [1, 4, 9, 4, 1, 10, 13]
# arr2 = [11, 13, 9, 3, 1, 9, 1] #이면 페어중에 큰 숫자 9가 나온 2를 반환합니다.
# arr1 = [1, 4, 4, 4, 1, 10, 4]
# arr2 = [11, 13, 11, 3, 11, 9, 1] #이면 4가 4번 페어가 나온 1을 반환합니다.
# arr1 = [1,2,2,3,2,2,2]
# arr2 = [4,5,4,5,4,5,4] #이면 4가 4번 페어가 나온 2를 반환합니다.
print(solution(arr1,arr2))
