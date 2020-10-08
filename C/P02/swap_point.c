/*
작성자 : 김도현 
모듈명 : 자료구조
날짜 : 20.09.05
Title :학생 3명의 국어, 영어, 수학 성적을 처리하여 첨부된 그림과 같이 출력하는 프로그램
*/

#include<stdio.h>

typedef struct scorelist{
	
	int num,korean,english,math,avg,sum; 
	
}score;

void main(){
	
	score sco[3];
	int i;
	
	printf("각 학생의 정보를 입력하세요.\n");
	for(i=0;i<3;i++){
		printf("학번, 국어, 영어, 수학 성적을 입력하세요.\n");
		scanf("%d %d %d %d",&sco[i].num, &sco[i].korean, &sco[i].english, &sco[i].math);
		
		sco[i].sum=(sco[i].korean+sco[i].english+sco[i].math);
		sco[i].avg=(sco[i].sum)/3;
	}
	
	printf("\n학번  국어  영어  수학  총점  평균\n");
	
	for(i=0;i<3;i++){
		printf(" %d %6d %5d %6d %5d %4d\n",sco[i].num, sco[i].korean, sco[i].english, sco[i].math, sco[i].sum, sco[i].avg);
	}
}
	
