/*
�ۼ��� : �赵�� 
���� : �ڷᱸ��
��¥ : 20.09.07
Title : �Է¹��� n��°������ �Ǻ���ġ ������ ����ϰ� , An���� ����Ѵ�. 
*/


#include <stdio.h>

int fib(int num) ;

int main(void){

        int num, i;
        printf("�Է¹��� n��°������  �Ǻ���ġ������ ����մϴ�.  :  " );
        scanf("%d" , & num) ;

        for(i = 0 ; i <= num ; i++ ){
                printf("%d " , fib(i));
        }
        
        printf("\n n��°�� �Ǻ���ġ ������ An�� :  \n");
        printf("%d", fib(num));
        
    return 0;
}



int fib(int num){
        if(num == 0) return 0;
        else if(num == 1) return 1;
        else return fib(num-1) + fib(num-2);
}

