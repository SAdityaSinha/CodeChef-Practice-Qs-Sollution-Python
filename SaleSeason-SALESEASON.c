#include <stdio.h>


int discoutn(int x){
    if(x<=100){
        return 0;
    }if(x>100 && x<=1000){
        return 25;
    }if(x>1000 && x<=5000){
        return 100;
    }if(x>5000){
        return 500;
    }
}



int main(){
	// your code goes here
    int x;
    int t;
    scanf("%d",&t);
    for(int i=0; i<t;i++){
        scanf("%d",&x);
        int disc = discoutn(x);
        printf("%d\n",x-disc);

    }

	return 0;
}
