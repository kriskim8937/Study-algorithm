#include <iostream>
using namespace std;
char a[100];

int main() {

	while (scanf_s("%10s", a, sizeof(a)) == 1) {

		printf("%s\n", a);

	}

	return 0;

}


/*
긴 문자열을 입력 받았을 때, 열 개씩 끊어 출력하기
*/
