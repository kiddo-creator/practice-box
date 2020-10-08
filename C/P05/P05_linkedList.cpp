/*
�ۼ��� : �赵�� 
���� : �ڷᱸ��
��¥ : 20.09.18
Title : ���Ḯ��Ʈ�� �Է�,���,����,�˻�,���� �� 
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
		printf("���� �Ҵ� ����. \n");
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

void display(ListNode *phead) // ����Ʈ�� Ȯ���ϴ� �Լ� ( ����Ʈ �� Ȯ�� )
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

void search(ListNode *phead, int num) // ����Ʈ�� ���ϴ� ���� �ִ��� Ȯ���ϴ� �Լ�
{
	while (phead != NULL) {
		if (phead->data == num) {
			printf("������%d �߰�..\n", num);
		}
		phead = phead->link;
	}
  }

ListNode *concat(ListNode *head1, ListNode *head2) // �� ����Ʈ�� �����ϴ� �Լ�
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
	insert_Node(&list1, create_Node(50));�� 
	insert_Node(&list1, create_Node(60));
	display(list1);

	list = concat(list, list1);
	display(list);

	removeNode(&list);
	display(list);

	search(list, 40);

	return 0;
}
