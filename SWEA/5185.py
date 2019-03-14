#
# 첫  줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50

# 다음 줄부터 테스트 케이스의 별로 자리 수 N과 N자리 16진수가 주어진다. 1<=N<=100

# 16진수 A부터 F는 대문자로 표시된다.

T = int(input())
X = 1
while T:
    N, num = list(map(str,input().split()))
    print('#',end = '')
    print(X,end = ' ')
    for i in num:
        print(bin(int(i,16))[2:].zfill(4),end ='')
    print('')
    X += 1
    T -= 1
