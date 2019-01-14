
//n 번째 까지의 피보나치 수를 전부 출력하는 함수
#include <iostream>
#include <vector>
using namespace std;


int memo[100];
int fibonacci(int n) {
	if (n <= 1) { return n; }
	else {
		if (memo[n] > 0) { return memo[n]; }
		memo[n] = fibonacci(n - 1) + fibonacci(n - 2);
		return memo[n];
	}
}
int main()
{
	int num = 0;
	scanf("%d", &num);
	for(int i = 1; i<=num; i++)
	{
		printf("%d ", fibonacci(i));
	}
	
	


	return 0;
}
