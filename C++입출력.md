# 입력 :

1. 표준입력
```
scanf("%d %d", &a, &b);
```
2. 배열 입력

```c++
int a[30];
for (int i = 0; i < n; i++)
{
  scanf("%d", &a[i]);
  sum += a[i];
} 
char map[101][101];
for (int i = 0; i < N; i++) {
	scanf("%s", map[i]);
}
```
3. 공백 구분 없이 입력
```
scanf("%[^\n]s",input);//[^\n]은 엔터만 빼고 입력받음 한줄로 [^]
```
5. cin 문자와 문자열 모두 입력 받을 수 있다. 엔터가 나오거나 공백이 나오면 입력 종료
4.gets()- Enter키를 누르기 전까지 공백을 포함한 모든 문자열을 입력
```
	char myArray[20];

	puts("아무 글이나 입력하시오~");

	gets(myArray);

	puts(myArray);
```
5.getline -
```
char a[10];
getline(a,10);
```
# 출력 :
1. 줄바꿈 출력
```
printf("%d\n", a+b);
printf("%s\n", a); // 문자열 출력
%f 실수, float
%c 문자, char
\n 줄바꿈
\t 탭
```
2. puts() - puts() 함수는 문자열을 화면에 출력하고 printf()함수와는 다르게 자동으로 줄이 바뀝니다.
3.2차원 문자열 출력
```
	for (i = 0; i < N; i++) {
			printf("%s", map[i]);
	}
```
