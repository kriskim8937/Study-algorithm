// <그림 1>과 같이 정사각형 모양의 지도가 있다. 1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다. 철수는 이 지도를 가지고 연결된 집들의 모임인 단지를 정의하고, 단지에 번호를 붙이려 한다. 여기서 연결되었다는 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우를 말한다. 대각선상에 집이 있는 경우는 연결된 것이 아니다. <그림 2>는 <그림 1>을 단지별로 번호를 붙인 것이다. 지도를 입력하여 단지수를 출력하고, 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하는 프로그램을 작성하시오.

// DFS나 BFS 알고리즘을 이용해서 어떻게 이어져있는지 확인 가능
// d[i][j]=)i,j를 방문 안했으면 0,했으면 단지번호
#include <cstdio>
#include <algorithm>
#include <queue>
using namespace std;
int a[30][30];
int group[30][30];
int dx[] = {0,0,1,-1};
int dy[] = {1,-1,0,0};
int n;
int ans[25*25];
void bfs(int x, int y, int cnt) {
    queue<pair<int,int>> q;//pair 사용 
    q.push(make_pair(x,y));
    group[x][y] = cnt; //방문한 그래프라고 표시
    while (!q.empty()) {//queue가 비어있지 않은 동안
        x = q.front().first;//pair안에 들어있는 것에 접근하기 위함
        y = q.front().second;
        q.pop();
        for (int k=0; k<4; k++) {
            int nx = x+dx[k]; //선택된 노드에 동서남북을 다확인하기 위함, 
            int ny = y+dy[k];
            if (0 <= nx && nx < n && 0 <= ny && ny < n) {//n은 지도의 크기 지금 있는 노드의 동서남북이 범위를 벗어나쓴ㄴ지 확인
                if (a[nx][ny] == 1 && group[nx][ny] == 0) {//이확인미 방문한 그래프인지 확인
                    q.push(make_pair(nx,ny));
                    group[nx][ny] = cnt; //방문한 그래프라고 표시
                }
            }
        }
    }
}
int main() {
    scanf("%d",&n);
    for (int i=0; i<n; i++) {//행
        for (int j=0; j<n; j++) {//열
            scanf("%1d",&a[i][j]);
        }
    }
    int cnt = 0;
    for (int i=0; i<n; i++) {
        for (int j=0; j<n; j++) {
            if (a[i][j] == 1 && group[i][j] == 0) {
                bfs(i, j, ++cnt);
            }
        }
    }
    printf("%d\n",cnt);
    for (int i=0; i<n; i++) {
        for (int j=0; j<n; j++) {
            ans[group[i][j]]+=1;
        }
    }
    sort(ans+1, ans+cnt+1);
    for (int i=1; i<=cnt; i++) {
        printf("%d\n",ans[i]);
    }
    return 0;
}
//ctrl+alt+c == compiling
//ctrl+alt+r == execute
//cirl+k+f == align 
//cirl+/ == 주석처리
