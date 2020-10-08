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
	printf("ȯ�� ť \n");
	printf("���� 1: ");enQueue(1);printQueue();
	printf("���� 2: ");enQueue(2);printQueue();
	printf("���� 3: ");enQueue(3);printQueue();
	printf("���� 4: ");enQueue(4);printQueue();
	printf("���� 5: ");enQueue(5);printQueue();
	printf("���� 6: ");enQueue(6);printQueue();
	printf("���� 7: ");enQueue(7);printQueue();
	printf("���� 8: ");enQueue(8);printQueue();
	printf("���� 9: ");enQueue(9);printQueue();	
	
	printf("ù��° ������ : ");searchQueue();			
	printf("����: ");deQueue();printQueue();
	printf("����: ");deQueue();printQueue();
	printf("����: ");deQueue();printQueue();
	printf("����: ");deQueue();printQueue();
	printf("���� 10: ");enQueue(10);printQueue();
	printf("���� 11: ");enQueue(11);printQueue();
	printf("���� 12: ");enQueue(12);printQueue();
	printf("���� 13: ");enQueue(13);printQueue();
	printf("���� 14: ");enQueue(14);printQueue();			
	return 0;
}
