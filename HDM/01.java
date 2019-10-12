택시기사인 A씨는 회사에서 쏘나타를 제공받아 한달에 n일간 택시를 운행하고 있습니다. 택시에 주입할 휘발유를 구입해야 하는데, 구입 가격은 날짜별로 변화가 있습니다. 이에 이 택시 회사에서는 휘발유 구입 비용을 줄이기 위해 n일을 운행하는데 필요한 최소 비용을 구하려고 합니다. 즉 n일간의 휘발유 가격 변화가 주어질 때, 가장 적은 비용이 드는 경우의 총액을 계산하고자 합니다. 택시를 운행할 날의 수 n과 택시를 하루 운행하는데 소요되는 휘발유의 당일 가격 목록 P가 매개변수로 주어질 때, 가장 적은 비용이 드는 경우의 총액을 return 하도록 solution 함수를 완성하세요.

제한사항
n은 1이상 100,000 이하의 자연수입니다.
P의 길이는 n 이고, P의 원소인 휘발유 가격은 1이상 10,000,000 이하의 자연수입니다.
입출력 예
n	P	result
10	[5, 4, 3, 2, 1, 6, 7, 8, 9, 10]	20
10	[5, 7, 8, 2, 4, 6, 1, 8, 9, 10]	25
입출력 예 설명
입출력 예 #1

제1일부터 제4일까지는 매일 구매하고, 제5일에 6일치를 한꺼번에 구입할 수 있습니다.

5 * 1 + 4 * 1 + 3 * 1 + 2 * 1 + 1 * 6 = 20
이와 같이 구입할 경우 10일 동안 운행할 때 필요한 휘발유의 최소 비용은 20입니다.

입출력 예 #2

제1일에 3일치, 제4일에 3일치, 제7일에 4일치를 구매할 수 있습니다.

5 * 3 + 2 * 3 + 1 * 4 = 25
이와 같이 구입할 경우 10일 동안 운행할 때 필요한 휘발유의 최소 비용은 25입니다.

import java.util.ArrayList;
class Solution {
	static int solution(int n, int[]P) {
		int min = P[0];
		ArrayList<Integer> arrayList = new ArrayList<Integer>();  
		arrayList.add(0);
		for(int i = 1;i<n;i++) {
			if(P[i]<min) {
				arrayList.add(i);
				min = P[i];
			}
		}
		arrayList.add(n);
		int answer = 0;
		for(int i = 0;i<arrayList.size()-1;i++) {
			int x = arrayList.get(i);
			answer += P[x]*(arrayList.get(i+1)-x);
		}
	    System.out.println(answer);
	    return answer;
	}
}
