/*
작성자 : 김도현 
모듈명 : 자료구조
날짜 : 20.09.18
Title : 연결리스트의 입력,출력,삭제,검색,병합 구 
*/

#include <stdio.h>

typedef struct ListNode {
	int data;
	struct ListNode *link;
}ListNode;

ListNode *create_Node(int data)
{
	ListNode *new_Node;
	new_Node = (ListNode *)malloc(sizeof(ListNode));
	if (new_Node == NULL) {
		printf("동적 할당 에러. \n");
		return;
	}

	new_Node->data = data;
	new_Node->link = NULL;

	return new_Node;
}

void insert_Node(ListNode **phead, ListNode *newNode)
{
	if (*phead == NULL) {
		newNode->link = NULL;
		*phead = newNode;
	}

	else {
		newNode->link = *phead;
		*phead = newNode;
	}
}

void display(ListNode *phead) // 리스트를 확인하는 함수 ( 리스트 값 확인 )
{
	while (phead != NULL) {
		printf("%d ", phead->data);
		phead = phead->link;
	}
	printf("\n");
}

void removeNode(ListNode **phead)
{
	ListNode *removeNode = *phead;
	*phead = (*phead)->link;
	
	free(removeNode);
}

void search(ListNode *phead, int num) // 리스트에 원하는 값이 있는지 확인하는 함수
{
	while (phead != NULL) {
		if (phead->data == num) {
			printf("데이터%d 발견..\n", num);
		}
		phead = phead->link;
	}
  }

ListNode *concat(ListNode *head1, ListNode *head2) // 두 리스트를 연결하는 함수
{
	ListNode *p;
		if (head1 == NULL) return head2;
		else if (head2 == NULL) return head1;
		else {
			p = head1;
			while (p->link != NULL) {
				p = p->link;
			}
			p->link = head2;
			return head1;
		}
}

int main()
{
	ListNode *list = NULL, *list1 = NULL;

	insert_Node(&list, create_Node(10));
	insert_Node(&list, create_Node(20));
	insert_Node(&list, create_Node(30));
	display(list);

	insert_Node(&list1, create_Node(40));
	insert_Node(&list1, create_Node(50));현 
	insert_Node(&list1, create_Node(60));
	display(list1);

	list = concat(list, list1);
	display(list);

	removeNode(&list);
	display(list);

	search(list, 40);

	return 0;
}
