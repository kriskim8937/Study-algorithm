알파벳 대문자로만 이루어진 N x N 크기 격자에서 가장 큰 X 모양을 찾으려 합니다. X 모양이란 다음과 같이 같은 알파벳으로 이루어진 두 대각선이 한 문자를 중심으로 교차하며, 교차점을 중심으로 네 방향의 길이가 같은 형태를 말합니다(흰 칸에는 A를 제외한 다른 알파벳이 적혀있다고 가정합니다).

largest_x_3.png

위 그림은 왼쪽 부터 순서대로 크기 3, 크기 5, 크기 7인 X 모양을 나타냅니다. X 모양의 크기는 3부터 시작하며, 항상 홀수입니다.

다음 그림은 X 모양이 아닌 예시를 나타냅니다.

largest_x_4.png

첫 번째의 경우 두 대각선이 한 문자에서 교차하지 않습니다. 두 번째의 경우 교차점을 중심으로 네 방향의 길이가 같지 않습니다. 단, 두 번째 그림의 경우 가장 우측 하단에 있는 A를 포함하지 않으면 크기 5인 X 모양을 만들 수 있습니다.

N x N 크기 격자가 문자열 형태로 담긴 배열 board가 매개변수로 주어질 때, 가장 큰 X 모양을 찾아 크기를 return 하도록 solution 함수를 완성해주세요.

제한사항
board의 각 원소는 격자의 가로(열)를 나타내는 문자열입니다.
board의 원소인 각 문자열의 길이는 board의 세로(행)길이와 같습니다.
board의 크기 N은 3 이상 1,000 이하입니다.
모든 문자는 알파벳 대문자로만 이루어져 있습니다.
X 모양의 크기는 한 대각선을 이루는 문자의 개수입니다.
X 모양이 없는 경우 0을 return 하면 됩니다.
입출력 예
board	result
[ABCBA,DABAG,EBABH,FAJAI,AKLMA]	5
[ABCBA,DABAG,ENABH,FAJAI,AKLMO]	3
입출력 예 설명
입출력 예 #1

입력으로 주어진 격자에 X 모양은 다음과 같이 두 개가 있습니다.

largest_X_5.png

따라서 가장 큰 X 모양의 크기는 5입니다.

입출력 예 #2

입력으로 주어진 격자에 X 모양은 다음과 같이 한 개가 있습니다.

largest_X_6.png

따라서 가장 큰 X 모양의 크기는 3입니다.
class Solution {
	static boolean boundaryCheck(int r, int c, int N) {
		if (r < N && 0 <= r && c < N && 0 <= c) {
			return true;
		} else
			return false;
	}

	static int checkCross(String[] map, int r, int c, int N) {
		int len = 1;
		char a = map[r].charAt(c);
		int r1 = r, r2 = r, r3 = r, r4 = r;
		int c1 = c, c2 = c, c3 = c, c4 = c;
		while (true) {
			if (!boundaryCheck(++r1, ++c1, N) || map[r1].charAt(c1) != a) {
				break;
			}
			if (!boundaryCheck(++r2, --c2, N) || map[r2].charAt(c2) != a) {
				break;
			}
			if (!boundaryCheck(--r3, ++c3, N) || map[r3].charAt(c3) != a) {
				break;
			}
			if (!boundaryCheck(--r4, --c4, N) || map[r4].charAt(c4) != a) {
				break;
			}
			len+=2;
		}
		return len;
	}

	static int solution(String[] board) {
		int n = board.length;
		int center = n / 2;
		int max = n;
		int hlen = 1;
		boolean[][] visited = new boolean[n][n];
		int answer = 1;
		out:
		while (true) {
			for (int i = center; i < center + hlen; i++) {
				for (int j = center; j < center + hlen; j++) {
					if (visited[i][j] == false) {
						visited[i][j] = true;
						int temp = checkCross(board, i, j, n);
						if( temp >answer) {
							answer = temp;
						}
						if (temp == max) {
							break out;
						}
					}
				}
			}
			max -=2;
			center -=1;
			hlen +=2;
			if(center == 0 || max <= answer) {
				break out;
			}
		}
        if(answer == 1){
            return 0;
        }
		else return answer;
	}
}
