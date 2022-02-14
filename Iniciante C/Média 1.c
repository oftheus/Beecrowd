#include <stdio.h>
int main(){
    float A,B;
    scanf("%f", &A);
    scanf("%f", &B);
    float conta = (A*3.5 + B*7.5)/11;
    printf("MEDIA = %.5f\n", conta);

    return 0;
}