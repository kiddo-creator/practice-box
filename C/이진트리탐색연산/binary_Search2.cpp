#include <stdio.h>
#include <algorithm>
using namespace std;
int n;
int arr[500000];

int lower_search(int k){
	int l=0,r=n-1,m,ans=-1;
	
	while( 1<= r){
		m=(l+r)/2;
		if(arr[m] > k){
			r=m-1;
		}
		else if(arr[m]<k){
			l=m+1;
		}
		else{
			ans=m;
			r=m-1;
		}
	}
	return ans;
}

int upper_search(int k){
	int l=0, r=n-1, m, ans= -1;
	while( l<= r){
		m=(l+r)/2;
		if(arr[m] > k){
			r=m-1;
		}
		else if(arr[m] <k){
			l=m+1;
		}
		else{
			ans=m;
			l=m+1;
		}
	}
	
	return ans;
}

int main(){
	int i,m,k,temp;
	scanf("%d",&n);
	for(i=0;i<n;i++){
		scanf("%d",&arr[i]);
	}
	sort(arr,arr+n);
	scanf("%d",&m);
	for(i=0;i<m;i++){
		scanf("%d",&k);
		temp=lower_search(k);
		if(temp == -1){
			printf("0 ");
		}
		else{
			printf("%d",upper_search(k)-temp+1);
		}
	}
	
	return 0;
}
