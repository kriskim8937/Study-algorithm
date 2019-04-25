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
```
3. 공백 구분 없이 입력
```
scanf("%[^\n]s",input);
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
