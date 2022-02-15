#include <stdio.h>
#include <stdlib.h>
int main(){
    int a,b,c,conta,conta2;
    scanf ("%d%d%d", &a,&b,&c);
    conta = ((a+b)+abs(a-b))/2;
    conta2 = ((conta+c)+abs(conta-c))/2;
    printf("%d eh o maior\n",conta2);
    return 0;
}