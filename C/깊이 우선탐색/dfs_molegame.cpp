#include <stdio.h>
int a[25][25];
int o[10]={0};
int n,cnt=1;
void input()
{
	int i,j;
	scanf("%d",&n);
	for(i=0;i<n;i++)
	{
		for(j=0;j<n;j++)
		{
			scanf("%d",&a[i][j]);
		}
	}
}
/*
7
0 1 1 0 1 0 0
0 1 1 0 1 0 1
1 1 1 0 1 0 1
0 0 0 0 1 1 1
0 1 0 0 0 0 0
0 1 1 1 1 1 0
0 1 1 1 0 0 0
*/
int safe(int x, int y)
{
	return x>=0 && x<n && y>=0 &&y<n;
}
void dfs(int x, int y, int c)
{
	a[x][y]=c;
	o[c-2]++;
	if(a[x][y+1]==1 && safe(x,y+1)) //right
		dfs(x,y+1,c);
	if(a[x][y-1]==1 && safe(x,y-1)) //left
		dfs(x,y-1,c);
	if(a[x-1][y]==1 && safe(x-1,y)) //up
		dfs(x-1,y,c);
	if(a[x+1][y]==1 && safe(x+1,y)) //down
		dfs(x+1,y,c);	
}

void search(){
	int i,j;
	for(i=0;i<n;i++)
	{
		for(j=0;j<n;j++)
		{
			if(a[i][j]==1)
			{
				cnt++;
				dfs(i,j,cnt);
			}
		}
	}
}

void output()
{
	int i,j;
	for(i=0;i<n;i++)
	{
		for(j=0;j<n;j++)
		{
			printf("%d ",a[i][j]);
		}
		printf("\n");
	}
	printf("%d\n",cnt-1);
	for(i=0;i<cnt-2;i++)
	{
		for(j=i+1;j<cnt-1;j++)
		{
			if(o[i] < o[j])
			{
				int t=o[i];
				o[i]=o[j];
				o[j]=t;
			}
		}
	}
	
	for(i=0;i<cnt-1;i++)
		printf("%d\n",o[i]);
}

int main(){
	input();
	search();
	output();
	return 0;
}

/*
7 8 9
*/
