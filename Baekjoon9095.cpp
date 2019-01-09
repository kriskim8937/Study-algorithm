#include <iostream>
using namespace std;

int num[10000];
int findnum(int num);

int main()
{
	int num,count;
	scanf("%d", &count);
	while (count--)
	{
		scanf("%d", &num);
		printf("%d\n", findnum(num));
	}
	return 0;
}
int findnum(int n)
{
	if (num[n] > 0)
		return num[n];
	num[1] = 1;
	num[2] = 2;
	num[3] = 4;
	if (n > 3)
	{
		num[n] = findnum(n - 1) + findnum(n - 2) + findnum(n - 3);
		num[n] %= 10007;
	}
	return num[n];

}
/*
1. 방법의 경우의 수의 총 합을구한다
2. n-1경우의 수를 구함
3. n-2경우의 수 , n-3의 경우의 수 
4. 2번과 3번을 더하기
*/
