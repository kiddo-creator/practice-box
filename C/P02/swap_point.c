/*
�ۼ��� : �赵�� 
���� : �ڷᱸ��
��¥ : 20.09.05
Title :�л� 3���� ����, ����, ���� ������ ó���Ͽ� ÷�ε� �׸��� ���� ����ϴ� ���α׷�
*/

#include<stdio.h>

typedef struct scorelist{
	
	int num,korean,english,math,avg,sum; 
	
}score;

void main(){
	
	score sco[3];
	int i;
	
	printf("�� �л��� ������ �Է��ϼ���.\n");
	for(i=0;i<3;i++){
		printf("�й�, ����, ����, ���� ������ �Է��ϼ���.\n");
		scanf("%d %d %d %d",&sco[i].num, &sco[i].korean, &sco[i].english, &sco[i].math);
		
		sco[i].sum=(sco[i].korean+sco[i].english+sco[i].math);
		sco[i].avg=(sco[i].sum)/3;
	}
	
	printf("\n�й�  ����  ����  ����  ����  ���\n");
	
	for(i=0;i<3;i++){
		printf(" %d %6d %5d %6d %5d %4d\n",sco[i].num, sco[i].korean, sco[i].english, sco[i].math, sco[i].sum, sco[i].avg);
	}
}
	
