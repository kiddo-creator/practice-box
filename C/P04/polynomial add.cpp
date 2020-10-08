/*
작성자 : 김도현 
모듈명 : 자료구조
날짜 : 20.09.11
Title : 과제에 주어진 다항식을 합산하여 출력한다. 
*/

#include <stdio.h>
#define MAX(px1,px2) (((px1)>(px2))?(px1):(px2))

//구조체 최고차항 dgree와 각 항의 해당하는 계수를 입력받을 coef 선언 
typedef struct{
    int degree;
    int coef[10];
} polynomial;
 
//세 항 px1,px2,px3중 px1과 px2 를 더하는 계산식 
polynomial poly_add1(polynomial px1, polynomial px2)
{
    int i;
    polynomial A;
    int px1pos = 0, px2pos = 0, Apos = 0;
    int degree_px1 = px1.degree, degree_px2 = px2.degree;
    A.degree = MAX(px1.degree, px2.degree);
    
    while (px1pos <= px1.degree && px2pos <= px2.degree) {
        if (degree_px1 > degree_px2) {
            A.coef[Apos++] = px1.coef[px1pos++];
            degree_px1--;
        }
        else if (degree_px1 == degree_px2) {
            A.coef[Apos++] = px1.coef[px1pos++] + px2.coef[px2pos++];
            degree_px1--; degree_px2--;
        }
        else {
            A.coef[Apos++] = px2.coef[px2pos++];
            degree_px2--;
        }
    }
    while (A.coef[0] == 0)
    {
        for (i = 0; i < A.degree; i++)
        {
            A.coef[i] = A.coef[i + 1];
        }
        A.degree--;
 
    }
    return A;
}
//세 항 px1,px2,px3중 px1과 px2 를 더한 결과값과 px3를 더하는 계산식 
polynomial poly_add2(polynomial px3, polynomial A)
{
    int i;
    polynomial B;
    int px3pos = 0, Apos = 0, Bpos = 0;
    int degree_px3 = px3.degree, degree_A = A.degree;
    B.degree = MAX(px3.degree, A.degree);
    
    while (px3pos <= px3.degree && Apos <= A.degree) {
        if (degree_px3 > degree_A) {
            B.coef[Bpos++] = px3.coef[px3pos++];
            degree_px3--;
        }
        else if (degree_px3 == degree_A) {
            B.coef[Bpos++] = px3.coef[px3pos++] + A.coef[Apos++];
            degree_px3--; degree_A--;
        }
        else {
            B.coef[Bpos++] = A.coef[Apos++];
            degree_A--;
        }
    }
    while (B.coef[0] == 0)
    {
        for (i = 0; i < B.degree; i++)
        {
            B.coef[i] = B.coef[i + 1];
        }
        B.degree--;
 
    }
    return B;
}
// 더한 결과값을 최고차항순으로 나열하여 출력 
void print_poly1(polynomial b){
	
    int i;
    int exponent = b.degree;
 
    for (i = 0; i <= b.degree; i++){
        if (b.coef[i] != 0){
	        printf("%dx^%d+ ", b.coef[i], exponent);
	        exponent--;
    	}
	}
	
	printf("\n");
}

//메인 메소드 
int main(void) {
    polynomial px1 = { 2,{ 3, 2, 3} };
    polynomial px2 = { 4,{ 5, 0, 0, 0, 3} };
    polynomial px3 = { 3,{ 1, 0, 1, 7} };
    
    polynomial a;
    polynomial b;
    
    a = poly_add1(px1, px2);
    b = poly_add2(px3,a);
    
	printf("주어진 각 다항식의 합 \n : ");
    printf("result = "); print_poly1(b);
}
