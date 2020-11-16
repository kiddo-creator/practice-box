#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAX_STACK_SIZE 100
 
typedef char Element;
 
Element data[MAX_STACK_SIZE];
int top;
 
void error(char str[])
{
	 printf("%s ", str);
	 exit(1);
}
 
void init_stack() {
 top = -1; 
}
 
int is_empty(){
	return top == -1;
}
int is_full(){
	return top == MAX_STACK_SIZE - 1;
}
int size(){
return top + 1;
}
 
void push(Element e)
{
 if (is_full())
  error("���� ��ȭ ����");
 data[++top] = e;
}
Element pop()
{
 if (is_empty())
  error("���� ���� ����");
 return data[top--];
}
Element peek()
{
 if (is_empty())
  error("���� ���� ����");
 return data[top];
}
void print_stack(char msg[])
{
 int i;
 printf("%s[%d]= ",msg,size());
 for (i = 0; i < size(); i++)
  printf("%c", data[i]);
 printf("n");
}
 
int main()
{
 int i;
 char a[MAX_STACK_SIZE];
 init_stack();
 printf("����Ȥ�� ���ڿ��� �Է��ϼ��� : ");
 scanf("%s", a);
 for (i = 0; a[i]; i++)
  push(a[i]);
 printf("�������� ��ȯ ");
 while (!is_empty())
  putchar(pop());
 return 0;
}
