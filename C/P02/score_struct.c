/*
�ۼ��� : �赵�� 
���� : �ڷᱸ��
��¥ : 20.09.05
Title : �����͸� ����� �Ǽ��� �� ���� ��ȯ�Ͽ� �����ϰ� ����ϴ� �Լ�
*/

#include <stdio.h>


//���ο� temp ������ Ȱ�� x,y���� �����ϴ� �޼ҵ�
// x,y�� ��巹������ �����Ϳ� �Է¹޾� swap 
void Swap(float *pX, float *pY){
	
	float temp;
	
	temp = *pX;
	*pX = *pY;
	*pY = temp;
	
	printf("�޼ҵ� ����Ϸ�");
}

// main

int main(){
	
	float x;
	float y;

	printf("x �Ǽ����� �Է��ϼ���.\n" );
	scanf("%f", &x);

	printf("y �Ǽ����� �Է��ϼ���.\n");
	scanf("%f", &y);

	printf("ù��° �Ǽ����� %f, �ι�° �Ǽ����� %f�Դϴ�.\n",x,y);

	Swap(&x,&y);
	
	printf("��ȯ�� ù��° �Ǽ����� %f, �ι�° �Ǽ����� %f�Դϴ�.\n",x,y);
	
} 
	
