/*
�ۼ��� : �赵�� 
���� : �ڷᱸ��
��¥ : 20.09.11
Title : ������ �־��� ���׽��� �ջ��Ͽ� ����Ѵ�. 
*/

#include <stdio.h>
#define MAX(px1,px2) (((px1)>(px2))?(px1):(px2))

//����ü �ְ����� dgree�� �� ���� �ش��ϴ� ����� �Է¹��� coef ���� 
typedef struct{
    int degree;
    int coef[10];
} polynomial;
 
//�� �� px1,px2,px3�� px1�� px2 �� ���ϴ� ���� 
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
//�� �� px1,px2,px3�� px1�� px2 �� ���� ������� px3�� ���ϴ� ���� 
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
// ���� ������� �ְ����׼����� �����Ͽ� ��� 
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

//���� �޼ҵ� 
int main(void) {
    polynomial px1 = { 2,{ 3, 2, 3} };
    polynomial px2 = { 4,{ 5, 0, 0, 0, 3} };
    polynomial px3 = { 3,{ 1, 0, 1, 7} };
    
    polynomial a;
    polynomial b;
    
    a = poly_add1(px1, px2);
    b = poly_add2(px3,a);
    
	printf("�־��� �� ���׽��� �� \n : ");
    printf("result = "); print_poly1(b);
}
