//백준 11720
//
#include <stdio.h>

int main(void)
{
	char input[100] = {0,};//배열 초기화
	int length, i, result = 0;
	scanf("%d", &length);
	scanf("%s", input);

	for (i = 0; i < length; i++)
		result += (input[i] - '0');//char 변수에 -'0'을 해주면 숫자로 바뀐다!

	printf("%d\n", result);

	return 0;
}
