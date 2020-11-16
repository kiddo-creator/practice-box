#include<stdio.h>
#include<string.h>

int main(){
    int queue[1],front, rear;
    char cmd[5];
    front,rear = 0;
    int N,i,num;
    
    scanf("%d",&N);
    for(i=0; i<N;i++){
        scanf("%s",&cmd);
        if(strcmp(cmd, "p") == 0){
            scanf("%d",&num);
            queue[rear] = num;
            rear++;
        }
        else if(strcmp(cmd, "o") == 0){
            if(queue[front] == 0){
                printf("%d\n",-1);
            }
            else{
            printf("%d\n",queue[front]);
            front++;
            }
        }
        else if(strcmp(cmd, "f")== 0){
            if(front - rear == 0){
                printf("%d\n",-1);
            }
            else{
            printf("%d\n",queue[front]);
            }
        }
        else if(strcmp(cmd, "b") == 0){
            if(front - rear == 0){
                printf("%d\n",-1);
            }
            else{
                printf("%d\n",queue[rear-1]);
            }
        }
        else if(strcmp(cmd, "s") == 0){
            printf("%d\n",rear-front);
        }
        else if(strcmp(cmd, "e") == 0){
            if(rear - front == 0){
                printf("%d\n",1);
            }
            else{
                printf("%d\n",0);
            }
        }
    }
}
