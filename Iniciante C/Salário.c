#include <stdio.h>

int main(){
    int A;
    float B,C;

    scanf("%i", &A);
    scanf("%f", &B);
    scanf("%f", &C);

    float conta = B * C;

    printf("NUMBER = %i\n", A);
    printf("SALARY = U$ %.2f\n",conta);
    return 0;
}