/*
작성자 : 김도현 
모듈명 : 자료구조
날짜 : 20.09.07
Title : 입력받은 n번째까지의 피보나치 수열을 출력하고 , An값을 출력한다. 
*/


#include <stdio.h>

int fib(int num) ;

int main(void){

        int num, i;
        printf("입력받은 n번째까지의  피보나치수열을 출력합니다.  :  " );
        scanf("%d" , & num) ;

        for(i = 0 ; i <= num ; i++ ){
                printf("%d " , fib(i));
        }
        
        printf("\n n번째의 피보나치 수열의 An값 :  \n");
        printf("%d", fib(num));
        
    return 0;
}



int fib(int num){
        if(num == 0) return 0;
        else if(num == 1) return 1;
        else return fib(num-1) + fib(num-2);
}

