/*
작성자 : 김도현 
모듈명 : 자료구조
날짜 : 20.09.18
Title : 지난번에 했던 addpoly를 연결리스트로 표현 
*/

#include <stdio.h>
#include <stdlib.h>

typedef struct ListNode{
	float coef;
	int expo;
	struct ListNode* next;
}listnode;

typedef struct {
	listnode* head;
}listnode_h;
listnode_h* createLinkedList(){
	listnode_h* L;
	L=(listnode_h*)malloc(sizeof(listnode_h));
	L->head=NULL;
	return L;
}
void printPoly(listnode_h* L){
	listnode* p=L->head;
	for(;p;p=p->next){
		printf("%3.0fx^%d",p->coef,p->expo);
		if(p->next!=NULL){
			printf(" +");
		}
	}
	printf("\n");
}
void appendTerm(listnode_h* L,float coef,int expo){
	listnode* newNode;
	listnode* p;
	newNode=(listnode*)malloc(sizeof(listnode));
	newNode->coef = coef;
	newNode->expo = expo;
	newNode->next = NULL;
	if(L->head==NULL){
		L->head=newNode;
		return;
	}
	else{
		p=L->head;
		while(p->next !=NULL){
			p=p->next;
		}
		p->next=newNode;
	}
}
void addPoly(listnode_h* A,listnode_h* B,listnode_h* C){
	listnode* pA=A->head;
	listnode* pB=B->head;
	float sum;
	while(pA && pB){
		if(pA->expo==pB->expo){
			sum=pA->coef+pB->coef;
			appendTerm(C,sum,pA->expo);
			pA=pA->next;
			pB=pB->next;
		}
		else if(pA->expo > pB->expo){
			appendTerm(C,pA->coef,pA->expo);
			pA=pA->next;
		}
		else{
			appendTerm(C,pB->coef,pB->expo);
			pB=pB->next;		
		}
	}
	for(;pA!=NULL;pA=pA->next){
		appendTerm(C,pA->coef,pA->expo);
	}
	for(;pB!=NULL;pB=pB->next){
		appendTerm(C,pB->coef,pB->expo);
	}
}
int main(){
	listnode_h *A,*B,*C;
	A=createLinkedList();
	B=createLinkedList();
	C=createLinkedList();
	
	appendTerm(A,4,3);
	appendTerm(A,3,2);
	appendTerm(A,5,1);
	printf("A(x)=");
	printPoly(A);
	
	appendTerm(B,3,4);
	appendTerm(B,1,3);
	appendTerm(B,2,1);
	appendTerm(B,1,0);
	printf("B(x)=");
	printPoly(B);

	addPoly(A,B,C);
	printf("C(x)=");
	printPoly(C);
	return 0;
}

