#include<iostream>
using namespace std;

int in[10][10];
int dir[4][2] = {{1,0},{0,1},{-1,0},{0,-1}};

void print(){
	for(int i=0;i<10;i++){
		for(int j=0;j<10;j++){
			if(in[i][j]){
				cout<<'*';
			}
			else{
				cout<<'_';
			}
		}
		cout<<"\n";
	}
}

void fill(int a,int b){
	if(in[a][b]){
		return;
	}
	in[a][b]=1;
	
	for(int i=0;i<4;i++){
		int na=a+dir[i][0], nb=b+dir[i][1];
		
		if(in[na][nb] || na>=10 || nb>=10 || na<0 || nb<0){
			continue;
		}
		
		fill(na,nb);		
	}
}

int main(){
	for(int i=0;i<10;i++){
		for(int j=0;j<10;j++){
			char tmp;
			cin>>tmp;
			if(tmp=='*'){
				in[i][j]=1;
			}
		}
	}

	int a,b;
	cin>>a>>b;
	fill(b,a);
	print();
}
