//백준 11721
// 열개씩 끊어 출력하기 
// strlen 
#include <stdio.h>
#include <string.h>

int main(void)
{
	char string[100];
	int i = 0, length = 0;

	scanf("%s", string);

	length = strlen(string);
	for (i = 0; i < length; i++) {
		printf("%c", string[i]);
		if ((i + 1) % 10 == 0)
			printf("\n");
	}


	return 0;
}
