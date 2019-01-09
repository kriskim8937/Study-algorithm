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
	recnum[2] = 2;
	if (num > 2)
	{
		recnum[num] = findrecnum(num - 1) + findrecnum(num - 2);
		recnum[num] %= 10007;
	}
	return recnum[num];

}
