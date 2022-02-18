#include <stdio.h>
#include <math.h>
int main(){
    double A,B,C,F1,F2,DELTA,d,x;
    scanf("%lf%lf%lf",&A,&B,&C);
    DELTA=pow(B,2)-(4*A*C);
    x=A*2;
    d=sqrt(DELTA);
    if (x==0 || DELTA<0){
        printf("Impossivel calcular\n");
    }
    else{
        F1=(-B + d) / (A*2);
        F2=(-B - d) / (A*2);
        printf("R1 = %.5lf\n",F1);
        printf("R2 = %.5lf\n",F2);
    }
    return 0;

}