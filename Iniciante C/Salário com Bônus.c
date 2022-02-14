#include <stdio.h>
int main(){
    char nome;
    float A,B;
    scanf("%s", &nome);
    scanf("%f", &A);
    scanf("%f", &B);
    float conta = (15*B)/100 + A;
    printf("TOTAL = R$ %.2f\n", conta);
    return 0;  

}