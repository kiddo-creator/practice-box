#include <stdio.h>
#include <algorithm>  //sort
using namespace std;
int arr[100000];
int n;

int binary_search(int k){
	int l=0,r=n-1,m; //L:왼쪽, r:오른쪽, m:검색위치 
	while(l <= r)
	{
		
		m=(l+r)/2;
		
		if(arr[m] > k){
			r=m-1;	
		}
		
		else if(arr[m] < k){
			l=m+1;
		}
	
		else{ //찾은경우 
			return 1; 
		}
	}
	return 0; 
}
int main(){
	int i,m,k;
	scanf("%d",&n);
	for(i=0;i<n;i++){
		scanf("%d",&arr[i]);	
	}
	sort(arr,arr+n); //정렬
	
	scanf("%d",&m);
	 
	for(i=0;i<m;i++){
		scanf("%d",&k);
		
		printf("%d\n",binary_search(k));
	}
	return 0;
}
