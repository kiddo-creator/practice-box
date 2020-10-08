/*
작성자 : 김도현 
모듈명 : 자료구조
날짜 : 20.09.05
Title : 포인터를 사용해 실수값 두 개를 교환하여 저장하고 출력하는 함수
*/

#include <stdio.h>


//새로운 temp 변수를 활용 x,y값을 변경하는 메소드
// x,y의 어드레스값을 포인터에 입력받아 swap 
void Swap(float *pX, float *pY){
	
	float temp;
	
	temp = *pX;
	*pX = *pY;
	*pY = temp;
	
	printf("메소드 실행완료");
}

// main

int main(){
	
	float x;
	float y;

	printf("x 실수값을 입력하세요.\n" );
	scanf("%f", &x);

	printf("y 실수값을 입력하세요.\n");
	scanf("%f", &y);

	printf("첫번째 실수값은 %f, 두번째 실수값은 %f입니다.\n",x,y);

	Swap(&x,&y);
	
	printf("교환된 첫번째 실수값은 %f, 두번째 실수값은 %f입니다.\n",x,y);
	
} 
	
