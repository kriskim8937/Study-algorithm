#include <algorithm>
#include <iostream>
#include <stdio.h>
#include <string>

using namespace std;

int main() {
	char str1[20];
	char str2[20];
	printf("문자열 입력 1: ");
	scanf("%s", str1);
	printf("문자열 입력 2: ");
	scanf("%s", str2);

	if (!strcmp(str1, str2)) {
		puts("두 문자열은 완벽히 동일합니다.");
	}
	else {
		puts("두 문자열은 일치하지 않습니다");
		if (!strncmp(str1, str2, 3))
			puts("그러나 앞 세글자는 동일 합니다.");
	}
	return 0;
}
