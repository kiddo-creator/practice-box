/*
작성자 : 김도현 
모듈명 : 컴퓨터과학 
날짜 : 20.09.18
Title : 이진탐색트리 구현 
*/

#include <stdio.h>

int BinarySearch(int *arr, int len, int target){  //이진탐색 arr배열, len배열의 크기, target 검색하고자하는대상 
	
	int first = 0; // 탐색 시작 인덱스 
	int last = len -1; // 탐색 마지막 인덱스 
	int mid;
	
	while(first<=last){
		mid = (first + last ) /2 ; // 탐색 리스트의 중간 인덱스 
		if (target == arr[mid]){
			return mid; // 검색하고자하는 target에 도달하였을경우 mid값 리턴 
		}
		else
		{
			if (target > arr[mid]){ 
				first = mid + 1; // 타겟이 더 크다면 first 의 위치를 옮김 
			}
			else{
				last = mid -1; // 타겟이 더 작다면 last 의 위치를 옮김
			}
		}
	}
	return -1; // arr내에서 탐색을 실패한경우 -1값 리턴 
}


int main(){ 
	int arr[] = {1,6,9,14,20,55}; // 탐색대상의 배열 
	int len = sizeof(arr) / sizeof(int); // arr배열의 크기 
	int index; //인덱스값 선언 

	index = BinarySearch(arr,len,14); //'14'값을 찾아본다.
	if (index == -1){
		printf("탐색실패하였습니다.\n");
	}
	else{
		printf("Target의 인덱스는 %d\n", index);
	}
	
	return 0;
		 
}

