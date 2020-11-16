#include <stdio.h>
#define N 10
int Queue[10];
int front=0, rear=0;

void enQueue(int n){
	if((rear+1)%N==front)
		printf("Queue is full!\n");
	else	
		Queue[++rear%N]=n;	
}

void printQueue(){
	int i,first,last;
	first=(front+1)%N;
	last=(rear+1)%N;
	i=first;
	printf("[");
	while(i!=last){
		printf("%d ",Queue[i]);
		i=(i+1)%N;
	}
	printf("]\n");
}
void deQueue(){
	if(front==rear) printf("Queue is empty!");
	else front=(front+1)%N;
}
void searchQueue(){
	if(front==rear) printf("no data\n");
	else
		printf("%d\n",Queue[(front+1)%N]);
}

int main(){
	printf("È¯Çü Å¥ \n");
	printf("»ğÀÔ 1: ");enQueue(1);printQueue();
	printf("»ğÀÔ 2: ");enQueue(2);printQueue();
	printf("»ğÀÔ 3: ");enQueue(3);printQueue();
	printf("»ğÀÔ 4: ");enQueue(4);printQueue();
	printf("»ğÀÔ 5: ");enQueue(5);printQueue();
	printf("»ğÀÔ 6: ");enQueue(6);printQueue();
	printf("»ğÀÔ 7: ");enQueue(7);printQueue();
	printf("»ğÀÔ 8: ");enQueue(8);printQueue();
	printf("»ğÀÔ 9: ");enQueue(9);printQueue();	
	
	printf("Ã¹¹øÂ° µ¥ÀÌÅÍ : ");searchQueue();			
	printf("»èÁ¦: ");deQueue();printQueue();
	printf("»èÁ¦: ");deQueue();printQueue();
	printf("»èÁ¦: ");deQueue();printQueue();
	printf("»èÁ¦: ");deQueue();printQueue();
	printf("»ğÀÔ 10: ");enQueue(10);printQueue();
	printf("»ğÀÔ 11: ");enQueue(11);printQueue();
	printf("»ğÀÔ 12: ");enQueue(12);printQueue();
	printf("»ğÀÔ 13: ");enQueue(13);printQueue();
	printf("»ğÀÔ 14: ");enQueue(14);printQueue();			
	return 0;
}
