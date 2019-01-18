
// 문제
// 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

// 입력
// 첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.
//인접리스트, 간선리스트, 비재귀 구현등 3가지 방법을 이요해서 구현 가능 
//현재 구현한것은 인접리스트
//A[i] (i는정점) 과연결된 점들을 저장
#include <iostream>
#include <algorithm>
#include <cstring>
#include <vector>
#include <queue>

using namespace std;
vector<int> a[1001];//[]쓰면 벡터형으로 1001개 생성  
bool check[1001];
void dfs(int node){
    check [node] = true;//이번에 방문할 노드가 방문되었다고 세팅
    printf("%d ", node);
    for( int i =0; i < a[node].size(); i++){
        int next = a[node][i];
        if(check[next] == false) //다음에 방문할 노드가 아직 방문되지 않았다는 것을 의미,아니면 그 다음 노드로 고고
        {
            dfs(next);
        }
    }

}
void bfs(int start)
{
    queue<int> q;
    memset(check,false,sizeof(check));//아까사용한 check 행렬을 false로 초기화 시킴
    check[start] = true;//첫번째 방문할 곳을 다녀왔다고 set
    q.push(start);
    while(!q.empty()){//q가 전부 빌때 까지 진행 
        int node = q.front();
        q.pop();
        printf("%d ", node);
        for(int i=0; i<a[node].size(); i++)//현재 방문한 노드의와 연결된 노드들 탐색, 처음방문한 곳이면 check = false하고 push 한다.
        {
            int next = a[node][i];
            if (check[next] == false){
                check[next] = true;
                q.push(next);
            }
        }
    }
}
int main() {
    int n, m, start;
    scanf("%d %d %d", &n,&m, &start);
    for(int i =0;i<m; i++){
        int u,v;
        scanf("%d %d",&u,&v);
        a[u].push_back(v);
        a[v].push_back(u);
    }
    for(int i = 1; i<=n; i++){
        sort(a[i].begin(),a[i].end());
    }
    //인접리스트를 구현하였다. 
    dfs(start);
    puts(" ");
    bfs(start);
    puts(" ");
    return 0;
}

//ctrl+alt+c == compiling
//ctrl+alt+r == execute
//cirl+k+f == align 
//cirl+/ == 주석처리
