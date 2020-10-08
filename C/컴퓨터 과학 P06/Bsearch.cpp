/*
�ۼ��� : �赵�� 
���� : ��ǻ�Ͱ��� 
��¥ : 20.09.18
Title : ����Ž��Ʈ�� ���� 
*/

#include <stdio.h>

int BinarySearch(int *arr, int len, int target){  //����Ž�� arr�迭, len�迭�� ũ��, target �˻��ϰ����ϴ´�� 
	
	int first = 0; // Ž�� ���� �ε��� 
	int last = len -1; // Ž�� ������ �ε��� 
	int mid;
	
	while(first<=last){
		mid = (first + last ) /2 ; // Ž�� ����Ʈ�� �߰� �ε��� 
		if (target == arr[mid]){
			return mid; // �˻��ϰ����ϴ� target�� �����Ͽ������ mid�� ���� 
		}
		else
		{
			if (target > arr[mid]){ 
				first = mid + 1; // Ÿ���� �� ũ�ٸ� first �� ��ġ�� �ű� 
			}
			else{
				last = mid -1; // Ÿ���� �� �۴ٸ� last �� ��ġ�� �ű�
			}
		}
	}
	return -1; // arr������ Ž���� �����Ѱ�� -1�� ���� 
}


int main(){ 
	int arr[] = {1,6,9,14,20,55}; // Ž������� �迭 
	int len = sizeof(arr) / sizeof(int); // arr�迭�� ũ�� 
	int index; //�ε����� ���� 

	index = BinarySearch(arr,len,14); //'14'���� ã�ƺ���.
	if (index == -1){
		printf("Ž�������Ͽ����ϴ�.\n");
	}
	else{
		printf("Target�� �ε����� %d\n", index);
	}
	
	return 0;
		 
}

