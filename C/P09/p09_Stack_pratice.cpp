/*
작성자 : 김도현 
모듈명 : 자료구조
날짜 : 20.10.02
Title : 스택 활용문제 
*/

#include <stdio.h>
int stack [100000];
int top = -1;

void push(int n){
	if(top==100000){
		printf("Stack is full!");
		return;
	}
	else{
		stack[++top]=n;
	}
}

void pop(){
	if(top==-1){
		printf("Stack is empty!");
		return;
	}
	else{
		top--;
	}
}
int main(){
	int k,i,n,j,sum = 0;
	scanf("%d",&k);
	for(i=0;i<k;i++){
		scanf("%d",&n);
		if(n>0) push(n);
		else pop();
		printf("[");
		for(j=0;j<=top;j++){
			printf("%d ", stack[j]);
		}
		printf("]\n");
	}
	for(i=0;i<=top;i++){
		sum+=stack[i];
		printf("%d",sum);
	 	return 0;
	}
}
/*
10
1
3
5
4
0
0
7
0
0
6
*/
