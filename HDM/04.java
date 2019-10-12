태농이는 한 손가락으로 키보드를 사용합니다. 태농이 키보드의 알파벳 배열은 다음과 같습니다.

keyboard_1.png

태농이는 처음에 "J"키를 누르면서 손가락을 올려 놓았습니다. 이제 손가락을 상, 하, 좌, 우 방향으로 한 칸씩 이동하면서 글자를 하나씩 입력합니다. 태농이는 정확히 T번 손가락을 이동하며, 이동할 때마다 키를 눌러 문자를 입력합니다. 단, 마지막에 누르는 키는 반드시 "J"키여야 합니다. 또, 손가락이 키보드 밖이나, 알파벳이 없는 키로는 이동하지 않습니다.

이때 태농이가 손가락을 움직이는 방법에 따라 다양한 문장이 입력 될 수 있습니다. 예를 들어 T = 2인 경우 다음과 같이 4가지 문장을 만들 수 있습니다.

"JUJ"
"JKJ"
"JMJ"
"JHJ"
예를 들어 첫 번째 문장의 경우 손가락을 [상, 하]방향으로 이동하면 만들 수 있습니다.

태농이가 손가락을 움직인 횟수 T가 매개변수로 주어질 때, 만들 수 있는 서로 다른 문장의 개수를 return 해주세요.

제한사항
T는 1 이상 100,000 이하인 자연수입니다.
정답이 커질 수 있으므로 1,000,000,007로 나눈 나머지를 return 해주세요.
입출력 예
T	result
2	4
4	30
1	0
입출력 예 설명
입출력 예 #1

문제 예시와 같습니다.

입출력 예 #2

태농이가 만들 수 있는 문장 중 하나는 "JUIKJ"입니다. 또 다른 예시로는 "JHJHJ"가 있습니다. 손가락을 4번 움직여 만들수 있는 서로 다른 문장의 개수는 30가지 입니다.

입출력 예 #3

손가락을 한 번만 움직여 다시 'J'로 돌아오는 방법은 없습니다.

class Solution {
   	static int []dro = {1,0,-1,0};
	static int []dco = {0,-1,0,1};
	static boolean [][] qwert = new boolean[3][10];
	static int [][] qwerty = {{7,6,5,4,3,2,1,2,3,4},{6,5,4,3,2,1,0,1,2,-1,-1},{7,6,5,4,3,2,1,-1,-1,-1}};
	static int [][] qwerty2 = {{7,6,5,4,3,2,1,2,3,3},{1,1,1,1,1,1,0,1,1,-1,-1},{7,6,5,4,3,2,1,-1,-1,-1}};
	static int jr = 1;
	static int jc = 6;
	static int ans = 0;
	static void dfs(int r, int c, int count) {
		if(count == qwerty[r][c])
		{
			ans+=qwerty2[r][c];
			return;
		}
		else if(count < qwerty[r][c]) {
			return;
		}
		for(int i=0;i<4;i++) {
			int nro = r+dro[i];
			int nco = c+dco[i];
			if(0<=nro&&nro<3&&0<=nco&&nco<10) {
				if(qwerty[nro][nco]>=0) {
					dfs(nro, nco, count-1);
				}
			}
		}
	}
	static int solution(int T) {
		qwert[1][9] = true;
		qwert[2][7] = true;
		qwert[2][8] = true;
		qwert[2][9] = true;
	    int answer = -1;
	    if(T%2 != 0){
	        return 0;
	        // 3개맞음
	    }else{
	        dfs(jr,jc,T);
	    }
	    return ans;
	}
}
