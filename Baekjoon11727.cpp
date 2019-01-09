#include <iostream>
using namespace std;

int recnum[10000];
int findrecnum(int num);

int main()
{
	int num;
	scanf("%d", &num);
	printf("%d", findrecnum(num));
	return 0;
}
int findrecnum(int num)
{
	if (recnum[num] > 0)
		return recnum[num];
	recnum[1] = 1;
	recnum[2] = 3;
	if (num > 2)
	{
		recnum[num] = findrecnum(num - 1) + 2*findrecnum(num - 2);
		recnum[num] %= 10007;
	}
	return recnum[num];

}
/*
1. 방법의 경우의 수의 총 합을구한다
2. n-1경우의 수를 구함
3. (n-2경우의 수)*2 
4. 2번과 3번을 더하기
5. n=1일 경우 1, n=2일 경우 2가 되야함
*/
