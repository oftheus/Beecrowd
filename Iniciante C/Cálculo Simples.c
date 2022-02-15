#include <stdio.h>
int main(){
    int a,b,c,d;
    double w,z,conta;
    scanf("%d%d%lf",&a,&b,&w);
    scanf("%d%d%lf",&c,&d,&z);
    conta = (b*w)+(d*z);
    printf("VALOR A PAGAR: R$ %.2lf\n",conta);
    return 0;
}