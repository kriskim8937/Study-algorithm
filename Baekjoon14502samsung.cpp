// 인체에 치명적인 바이러스를 연구하던 연구소에서 바이러스가 유출되었다. 다행히 바이러스는 아직 퍼지지 않았고, 바이러스의 확산을 막기 위해서 연구소에 벽을 세우려고 한다.

// 연구소는 크기가 N×M인 직사각형으로 나타낼 수 있으며, 직사각형은 1×1 크기의 정사각형으로 나누어져 있다. 연구소는 빈 칸, 벽으로 이루어져 있으며, 벽은 칸 하나를 가득 차지한다.

// 일부 칸은 바이러스가 존재하며, 이 바이러스는 상하좌우로 인접한 빈 칸으로 모두 퍼져나갈 수 있다. 새로 세울 수 있는 벽의 개수는 3개이며, 꼭 3개를 세워야 한다.

// 예를 들어, 아래와 같이 연구소가 생긴 경우를 살펴보자.
#include <algorithm>
#include <queue>
#include <iostream>
#include <vector>
using namespace std;
int a[30][30];
int a2[30][30];
int group[30][30] = {
    0,
}; //방문했는지 확인,2차원 배열 초기화
int dx[] = {0, 0, 1, -1};
int dy[] = {1, -1, 0, 0};
vector<pair<int, int>> v;
int row, col;
int ans[25 * 25];
int wall[10001];
int anser;
void bfs(int x, int y, int cnt)
{
    
    queue<pair<int, int>> q; //pair 사용
    q.push(make_pair(x, y));
    group[x][y] = cnt; //방문한 그래프라고 표시
    while (!q.empty())
    {                        //queue가 비어있지 않은 동안
        x = q.front().first; //pair안에 들어있는 것에 접근하기 위함
        y = q.front().second;
        q.pop();
        for (int k = 0; k < 4; k++)
        {
            int nx = x + dx[k]; //선택된 노드에 동서남북을 다확인하기 위함,
            int ny = y + dy[k];

            if (0 <= nx && nx < row && 0 <= ny && ny < col)
            { //n은 지도의 크기 지금 있는 노드의 동서남북이 범위를 벗어나쓴ㄴ지 확인
                if (a2[nx][ny] == 0 && group[nx][ny] == 0)
                { //이미 방문한 그래프인지 확인
                    printf("%d %d\n", nx, cnt);
                    a2[nx][ny] = 3;
                    q.push(make_pair(nx, ny));
                    group[nx][ny] = cnt; //방문한 그래프라고 표시
                }
            }
        }
    }
    group[30][30] = {0,};
}
// void wall(int cnt){
//     //3개의 벽이 세워졌을 때, 바이러스를 퍼트린다.
//     if(cnt == 3){
//         virusSpread();
//         return;
//     }
//     //벽 세우는 부분.
//     for (int i = 0; i < n; i++) {
//         for (int j = 0; j < m; j++) {
//             if(tempLab[i][j]==0){
//                 tempLab[i][j] = 1;
//                 wall(cnt+1);
//                 //모든 경우의 수를 넣어야하므로 기존의 1을 0으로 바꾸어주는 역활
//                 tempLab[i][j] = 0;
//             }
//         }
//     }
// }
int main()
{
    scanf("%d %d", &row, &col);
    for (int i = 0; i < col; i++)
    { //행
        for (int j = 0; j < row; j++)
        {                           //열
            scanf("%1d", &a[i][j]); //붙어있는 숫자를 하나씩 입력받고 싶을때
            if (a[i][j] == 0)
            {
                v.push_back(make_pair(i, j));
            }
        }
    }

    int vsize = v.size();

    ////////////////////////똑가튼행렬 만듬

    for (int x = 0; x < (vsize - 2); x++)
    {
        for (int y = 1; y < (vsize - 1); y++)
        {
            for (int z = 2; z < vsize; z++)
            {
                //원본과가튼행렬 만듬
                for (int i = 0; i < col; i++)
                { //행
                    for (int j = 0; j < row; j++)
                    { //열
                        a2[i][j] = a[i][j];
                    }
                }
                //////////////벽을 세움
                a2[v[x].first][v[x].second] = 1;
                a2[v[y].first][v[y].second] = 1;
                a2[v[z].first][v[z].second] = 1;
                ///////바이러스 확산
                int cnt =0;
                for (int i = 0; i < col; i++)
                {
                    for (int j = 0; j < row; j++)
                    {
                        if (a2[i][j] == 2 && group[i][j] == 0)
                        {
                            bfs(i, j, ++cnt);
                        }
                    }
                }
                /////////////출력
                for (int i = 0; i < col; i++)
                { //행
                    for (int j = 0; j < row; j++)
                    { //열
                        printf("%d ", a2[i][j]);
                    }
                    printf("\n");
                }
                printf("\n");
            }
        }
    }
    ///////////////////////

    //printf("itis %d itis",vsize); 벡터의 길이 출력
    // int walnum = 3;

    //     for (int i = 0; i < row; i++)
    //     { //행
    //         for (int j = 1; j < col; j++)
    //         { //열
    //             for(int k =2; k< ; k++)
    //         }
    //     }

    int cnt = 0;
    for (int i = 0; i < row; i++)
    {
        for (int j = 0; j < col; j++)
        {
            if (a[i][j] == 2 && group[i][j] == 0)
            {
                bfs(i, j, ++cnt);
            }
        }
    }

    // printf("%d ",cnt);
    // for (int i=0; i<n; i++) {
    //     for (int j=0; j<n; j++) {
    //         ans[group[i][j]]+=1;싶을때
    //     }
    // }
    // sort(ans+1, ans+cnt+1);

    printf("\n");

    for (int i = 0; i < col; i++)
    { //행
        for (int j = 0; j < row; j++)
        { //열
            printf("%d ", a[i][j]);
        }
        printf("\n");
    }
    int num = 0;
    for (int i = 0; i < row; i++)
    { //행
        for (int j = 0; j < col; j++)
        { //열
            if (a[i][j] == 0)
                num++;
        }
    }
    printf("%d", num);
    return 0;
}
//ctrl+alt+c == compiling
//ctrl+alt+r == execute
//cirl+k+f == align
//cirl+/ == 주석처리
//1억이 1초로
