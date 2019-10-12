ABC 렌터카에서는 아반떼을 여러 대 보유하고 있습니다. 이 차량들을 골고루 활용하기 위해서 적산주행거리가 가장 작은 차량부터 고객들에게 대여해 주기로 합니다.

ABC 렌터카가 보유하고 있는 아반떼의 대수 n, 각 차량에 부여된 차량번호가 문자열의 형태로 들어있는 배열 plates, 각 차량의 적산 주행거리가 정수의 형태로 들어있는 배열 odo, ABC 렌터카에 순서대로 도착하여 차량을 대여하는 고객의 수 k, 각 고객이 차량을 대여하여 주행하는 거리가 들어있는 배열 drives가 매개변수로 주어질 때, 다음 고객에게 ABC 렌터카가 대여해 줄 차량의 차랑번호를 return하는 solution 함수를 완성하세요.

제한사항
n 은 10,000 이하의 정수입니다.
plates 의 원소인 차량번호는 영문 알파벳 두 글자와 네 자리 숫자로 이루어져 있습니다. 예를 들면 “AB1234” 와 같은 형식입니다.
odo 의 원소인 차량의 현재 적산주행거리는 1이상 100,000 이하의 자연수입니다.
plates 와 odo 의 길이는 n 입니다. plates[i] 의 차량번호를 가지는 차량의 현재 적산주행거리는 odo[i] 입니다.
k 는 10,000 이하의 정수입니다.
drives 의 원소인 한 고객이 한 번 차량을 대여하여 주행하는 거리는 1이상 500 이하의 자연수입니다.
한 고객이 대여한 차량은 다음 고객이 차량을 대여하기 전에 반납됩니다.
만약 적산주행거리가 가장 작은 차량이 두 대 이상 있는 경우에는 차량번호가 사전 순서로 앞서는 차량을 대여에 이용합니다.
입출력 예
n	plates	odo	k	drives	answer
6	[AZ3618, XP9657, SP6823, UH7515, TV6621, WZ8264]	[20, 16, 18, 20, 24, 19]	8	[3, 7, 5, 8, 6, 5, 10, 2]	SP6823
입출력 예시 설명
ABC 렌터카가 보유한 여섯 대의 차량에 대하여 각 차량의 적산주행거리 변화를 그림으로 나타내면 다음과 같습니다.

image

첫 고객이 도착했을 때 가장 작은 적산주행거리를 가지는 차량은 XP9657 (적산주행거리 16) 입니다. 이 고객은 이 차량을 대여하여 3 만큼 주행하고 반납하여, 이 차량의 적산주행거리는 19 가 됩니다.
두 번째 고객이 도착했을 때 가장 작은 적산주행거리는 18 이고 이 차량은 SP6823 입니다. 이 고객이 주행을 마치고 반납하면, 이 차량의 적산주행거리는 25 가 됩니다.
세 번째 고객이 도착했을 때 가장 작은 적산주행거리는 19 인데, 같은 적산주행거리를 가지는 차량이 두 대입니다. WZ8264 가 사전 순서로 XP9657 보다 앞서므로, WZ8264 번호를 가지는 차량을 대여합니다.
마찬가지 과정을 반복하여 여덟 명의 고객이 모두 차량의 대여와 주행, 반납을 완료한 뒤 가장 작은 적산주행거리는 25 입니다. 같은 적산주행거리를 가지는 두 대의 차량은 각각 차량번호 SP6823 과 UH7515 인데, 이 중 사전 순서로 앞서는 번호인 "SP6823” 의 차량이 다음 대여 대상입니다. 따라서 SP6823 을 return 하면 됩니다.

// plates_len, odo_len, drives_len은 각각 배열 plates, odo, drives의 길이입니다.
// solution 함수의 파라미터로 주어지는 문자열은 const로 주어집니다.
// 변경이 필요한 경우에는 문자열을 복사해서 사용하세요.0
import java.util.PriorityQueue;
class Node implements Comparable<Node> {
	int no;
	String name;

	public Node(int no, String name) {
		super();
		this.no = no;
		this.name = name;
	}

	@Override
	public int compareTo(Node o) {
		if(this.no == o.no) {
			if(0>this.name.compareTo(o.name)) {
				return -1;
			}
			else {
				return 1;
			}
		}
		else return this.no - o.no;
	}

	@Override
	public String toString() {
		return "Node [no=" + no + ", name=" + name + "]";
	}
	
}
class Solution {
    public String solution(int n, String[] plates, int[] odo, int k, int[] drives) {
    	PriorityQueue<Node> pq = new PriorityQueue<Node>();
		for (int j = 0; j < n; j++) {
			pq.add(new Node(odo[j], plates[j]));
		}
		for(int i=0;i<k;i++) {
			Node temp = pq.poll();
			pq.add(new Node(temp.no+drives[i],temp.name));
		}
        String answer = pq.peek().name;
        return answer;
        }
}
