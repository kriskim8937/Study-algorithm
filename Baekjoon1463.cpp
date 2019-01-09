#include <iostream>
#include <string>
using namespace std;

int togo(int num);
int min[10000];

int main() {
	int num = 0;
	scanf("%d", &num);
	int min = togo(num);
	printf("%d", min);
	return 0;
}

int togo(int num)
{
	
	if(num == 1)
	{
		return 0;
	}
	if (min[num] > 0)
		return min[num];
	min[num] = togo(num-1) + 1;
	if (num % 2 == 0)
	{
		//min[num] = togo(num / 2)+1;
		int temp = togo(num / 2) + 1;
		if (temp < min[num])
		{
			min[num] = temp;

		}

	}
	if (num % 3 == 0)
	{
		int temp = togo(num / 3) + 1;
		if (temp < min[num])
		{
			min[num] = temp;
			
		}

	}
	return min[num];
	 
}
/*
Top down method
1. 배열을 만들어서, 연산을 사용하는 횟수의 최솟값을 전부 저장
2. n번째의 최솟값은, n-1번째의 최솟값과, n/2번째의 최솟값, n/3번째의 최솟값 +1을 비교하여 가장 작은 값이다.
*/
