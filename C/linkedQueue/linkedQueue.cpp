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
	if(LQ->front==NULL){ //�Է� �Ұ��� 
		LQ->front = newNode;
		LQ->rear= newNode;
	}
	else //�Է� ���� 
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
	else{ //�������� 
		LQ->front=LQ->front->next;
		if(LQ->front==NULL){
			LQ->rear=NULL;
		free(old);
		}
	}
}
int main(){
	LQueueType *LQ=creatLinkedQueue();
	printf("����ť ����\n");
	printf("���� 1");enQueue(LQ,1);printLQ(LQ);
	printf("���� 2");enQueue(LQ,2);printLQ(LQ);
	printf("���� 3");enQueue(LQ,3);printLQ(LQ);
	
	printf("����");deQueue(LQ);printLQ(LQ);
	printf("����");deQueue(LQ);printLQ(LQ);
	printf("����");deQueue(LQ);printLQ(LQ);
	printf("����");deQueue(LQ);printLQ(LQ);				 
}

