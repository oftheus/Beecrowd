#include <stdio.h>
#include <math.h>
int main(){
    int raio,conta;
    double pi = 3.14159;
    scanf("%d",&raio);
    double formula = (4/3.0)*pi*(pow(raio,3));
    printf("VOLUME = %.3lf\n",formula);
    return 0;
}