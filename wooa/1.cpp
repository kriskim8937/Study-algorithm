#include <algorithm>
#include <iostream>
#include <stdio.h>
#include <string>

using namespace std;

int main(void) {
	int moneyList[] = { 50000, 10000, 5000, 1000, 500, 100, 50, 10, 1 };
	int ans[9] = {0,};
	int K = 0;
	scanf("%d", &K);
	for (int i = 0; i < 9; i++) {
		if (K  >= moneyList[i]) {
			ans[i] = K / moneyList[i];
			K %= moneyList[i];
		}
		printf("%d ", ans[i]);
	}

	return 0;
}
