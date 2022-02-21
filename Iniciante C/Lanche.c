#include <stdio.h>
int main(){
    float x,q;
    float c;
    scanf("%f%f",&x,&q);
    if (x==1)
        x=4.00;
    else if (x==2)
        x=4.50;
    else if (x==3)
        x=5.00;
    else if (x==4)
        x=2.00;
    else if (x>4)
        x=1.50;
    c = x * q;
    printf("Total: R$ %.2f\n",c);
    return 0;
}