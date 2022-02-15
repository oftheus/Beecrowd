#include <stdio.h>
#include <math.h>
int main(){
   double A,B,C;
   double pi = 3.14159;
   scanf("%lf%lf%lf", &A,&B,&C);
   double atriangulo = (A*C)/2;
   double acirculo   = (pi*(pow(C,2)));
   double atrapezio  = ((A+B)*C)/2;
   double aquadrado  = pow(B,2);
   double aretangulo = (A*B);
   printf("TRIANGULO: %.3lf\n",atriangulo);
   printf("CIRCULO: %.3lf\n",acirculo);
   printf("TRAPEZIO: %.3lf\n",atrapezio);
   printf("QUADRADO: %.3lf\n",aquadrado);
   printf("RETANGULO: %.3lf\n",aretangulo);
   return 0;
}