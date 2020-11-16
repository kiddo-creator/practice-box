#include <stdio.h>
#include <stdlib.h>

typedef struct treeNode{
	char data;
	struct treeNode *left;
	struct treeNode *right;
	int isThreadRight; // ¿À¸¥ÂÊ  
}treeNode; 

treeNode* makeRootNode(char data, treeNode* leftnode, treeNode* rightnode,int isThreadRight){
	treeNode* root=(treeNode *)malloc(sizeof(treeNode));
	root->data=data;
	root->left=leftnode;
	root->right=rightnode;
	root->isThreadRight=isThreadRight;
	return root;
}

treeNode* findThreadSuccessor(treeNode* p)
{
	treeNode *q=p->right;
	if(q==NULL) return q;
	if(p->isThreadRight==1) return q;
	while(q->left !=NULL) q=q->left;
	return q;
}

void inorder(treeNode* root){
	treeNode* q=root;
	while(q->left) q=q->left;
	do{
		printf("%c",q->data);
		q=findThreadSuccessor(q);
	}while(q);
}

int main(){
	treeNode* n7=makeRootNode('D',NULL,NULL,0);
	treeNode* n6=makeRootNode('C',NULL,NULL,1);
	treeNode* n5=makeRootNode('B',NULL,NULL,1);
	treeNode* n4=makeRootNode('A',NULL,NULL,1);
	treeNode* n3=makeRootNode('/',n6,n7,0);
	treeNode* n2=makeRootNode('*',n4,n5,0);
	treeNode* n1=makeRootNode('-',n2,n3,0);
	
	n4->right=n2;
	n5->right=n1;
	n6->right=n3;
	printf("\n inorder : ");
	inorder(n1);

}
