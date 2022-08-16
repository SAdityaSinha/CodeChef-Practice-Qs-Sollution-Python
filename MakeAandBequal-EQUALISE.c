#include <stdio.h>
// has two number A , B 
// choose any one a , b and *2
// 
void test(int s , int b){
    do{
        s = s * 2;
        if(s==b){
            printf("YES\n");
            break;
        }if(s>b){
            printf("NO\n");
            break;
        }
    }while(1==1);
    
}


int main(void) {
	// your code goes here
	int t,a,b;
	scanf("%d",&t);
	for(int i = 0; i<t ; i++){
	    scanf("%d %d",&a,&b);
	    if(a==b){
	        printf("YES\n");
	    }if(a>b){
	        test(b,a);
	    }if(a<b){
	        test(a,b);
	    }
	}
	return 0;
}

