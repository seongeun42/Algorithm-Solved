#include<cstdio>
#include<vector>
#include<queue>
#include<string>
using namespace std;
char arr[101][101];
bool vis[101][101];
int dx[4]={0,0,-1,1};
int dy[4]={1,-1,0,0};
int bfs(int x, int y,int n){
    if(vis[x][y])
        return 0;
    vis[x][y]=1;
    queue<pair<int,int>> q;
    char comparedChar = arr[x][y];
    q.push(make_pair(x,y));
    while(!q.empty())
    {
        int cx= q.front().first;
        int cy= q.front().second;
        q.pop();
        for (int i = 0; i < 4; i++)
        {
            int nx = cx+dx[i];
            int ny = cy+dy[i];
            if(nx<0||ny<0||nx>=n||ny>=n)
                continue;
            if(vis[nx][ny]||arr[nx][ny]!=comparedChar)
                continue;
            q.push(make_pair(nx,ny));
            vis[nx][ny]=1;
        }
    }
    return 1;
}

int main(){
    int n;
    scanf("%d",&n);

    for(int i=0;i<n;i++)
        scanf("%s",arr[i]);

    int sum=0,sum1=0;

    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            sum+=bfs(i,j,n);
  
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            if(arr[i][j]=='G')
                arr[i][j] = 'R';
            vis[i][j]=0;
        }
    }

    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            sum1+=bfs(i,j,n);
            
    printf("%d %d\n",sum,sum1);
    return 0;
}
