#include <stdio.h>
#include <stdlib.h>

typedef struct Queue{
	int data;
	struct Queue *next;
}Queue;

typedef struct{
	Queue *front,*rear;
}LQueueType;
LQueueType *creatLinkedQueue()
{
	LQueueType *LQ;
	LQ=(LQueueType *)malloc(sizeof(LQueueType));
	LQ->front = NULL;
	LQ->rear = NULL;
}
void enQueue(LQueueType *LQ,int d){
	Queue *newNode=(Queue *)malloc(sizeof(Queue));
	newNode->data=d;
	newNode->next=NULL;
	if(LQ->front==NULL){ //입력 불가능 
		LQ->front = newNode;
		LQ->rear= newNode;
	}
	else //입력 가능 
	{
		LQ->rear->next=newNode;
		LQ->rear=newNode;
	}
}
void printLQ(LQueueType *LQ){
	Queue *temp=LQ->front;
	printf("[");
	while(temp){
		printf("%d ",temp->data);
		temp=temp->next;
	}
	printf("]\n");
}	
void deQueue(LQueueType *LQ){
	Queue *old=LQ->front;
	if(LQ->front==NULL){
		printf("Linked Queue is empty!\n");
		return;
	}
	else{ //삭제가능 
		LQ->front=LQ->front->next;
		if(LQ->front==NULL){
			LQ->rear=NULL;
		free(old);
		}
	}
}
int main(){
	LQueueType *LQ=creatLinkedQueue();
	printf("연결큐 연산\n");
	printf("삽입 1");enQueue(LQ,1);printLQ(LQ);
	printf("삽입 2");enQueue(LQ,2);printLQ(LQ);
	printf("삽입 3");enQueue(LQ,3);printLQ(LQ);
	
	printf("삭제");deQueue(LQ);printLQ(LQ);
	printf("삭제");deQueue(LQ);printLQ(LQ);
	printf("삭제");deQueue(LQ);printLQ(LQ);
	printf("삭제");deQueue(LQ);printLQ(LQ);				 
}

