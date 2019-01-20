// 섬의 개수
// 정사각형으로 이루어져 있는 섬과 바다 지도가 주어진다. 섬의 개수를 세는 프로그램을 작성하시오.



// 한 정사각형과 가로, 세로 또는 대각선으로 연결되어 있는 사각형은 걸어갈 수 있는 사각형이다. 

// 두 정사각형이 같은 섬에 있으려면, 한 정사각형에서 다른 정사각형으로 걸어서 갈 수 있는 경로가 있어야 한다. 지도는 바다로 둘러쌓여 있으며, 지도 밖으로 나갈 수 없다.

#include<iostream>
#include<queue>
#include<algorithm>
using namespace std;
int w,h ;
int a[100][100] = {0,};
int d[100][100] = {0,};
int dx[] = {0,0,1,-1,1,1,-1,-1};
int dy[] = {1,-1,0,0,1,-1,1,-1};

void bfs(int i, int j, int cnt);

int main()
{
    while(true)
    {
        scanf("%d %d",&w,&h);
        if (w == 0 && h == 0) break;
        for(int i=0; i<h; i++)//hw랑w 순서 바꿔줘야함 헷갈릴수 있음 잘생각
        {
            for(int j=0; j<w; j++)
            {
                scanf("%1d", &a[i][j]);
                d[i][j] = 0;//초기화 시켜줘야됨
            }
        }
        int cnt = 0;
        for (int i=0; i<h; i++) {
            for (int j=0; j<w; j++) {
               if (a[i][j] == 1 && d[i][j] == 0) {
                    bfs(i, j, ++cnt);
                }
            }
        }
        printf("%d\n",cnt);
    }
    return 0;
}
//ctrl+alt+c == compiling
//ctrl+alt+r == execute
//cirl+k+f == align
//cirl+/ == 주석처리
//1억이 1초로


void bfs(int x, int y, int cnt) {
    queue<pair<int,int>> q;
    q.push(make_pair(x,y));
    d[x][y] = cnt;
    while (!q.empty()) {
        x = q.front().first;
        y = q.front().second;
        q.pop();
        for (int k=0; k<8; k++) {
            int nx = x+dx[k];
            int ny = y+dy[k];
            if (0 <= nx && nx < h && 0 <= ny && ny < w) {
                if (a[nx][ny] == 1 && d[nx][ny] == 0) {
                    q.push(make_pair(nx,ny));
                    d[nx][ny] = cnt;
                }
            }
        }
    }
}
//2차원 배열 입력하고 출력할때 잘생각해야함 
