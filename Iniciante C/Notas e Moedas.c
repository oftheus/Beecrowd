#include <stdio.h>
int main(){
    double x;
    scanf("%lf",&x);
    int q = x/100;
    int c = (x-(q*100))/50;
    int v= (x-(c*50)-(q*100))/20;
    int d=(x-(v*20)-(c*50)-(q*100))/10;
    int f=(x-(d*10)-(v*20)-(c*50)-(q*100))/5;
    int g=(x-(f*5)-(d*10)-(v*20)-(c*50)-(q*100))/2;
    int u=(x-(g*2)-(f*5)-(d*10)-(v*20)-(c*50)-(q*100))/1;

    int a=(x-(u)-(g*2)-(f*5)-(d*10)-(v*20)-(c*50)-(q*100))/(0.5);
    int b=(x-(a*0.5)-(u)-(g*2)-(f*5)-(d*10)-(v*20)-(c*50)-(q*100))/(0.25);
    int e=(x-(b*0.25)-(a*0.5)-(u)-(g*2)-(f*5)-(d*10)-(v*20)-(c*50)-(q*100))/(0.10);
    int h=(x-(e*0.10)-(b*0.25)-(a*0.5)-(u)-(g*2)-(f*5)-(d*10)-(v*20)-(c*50)-(q*100))/0.05;
    float l=(x-(h*0.05)-(e*0.10)-(b*0.25)-(a*0.50)-(u)-(g*2.00)-(f*5.00)-(d*10.00)-(v*20.00)-(c*50.00)-(q*100.00))/0.01;

    printf("NOTAS:\n");
    printf("%d nota(s) de R$ 100.00\n",q);
    printf("%d nota(s) de R$ 50.00\n",c);
    printf("%d nota(s) de R$ 20.00\n",v);
    printf("%d nota(s) de R$ 10.00\n",d);
    printf("%d nota(s) de R$ 5.00\n",f);
    printf("%d nota(s) de R$ 2.00\n",g);
    printf("MOEDAS:\n");
    printf("%d nota(s) de R$ 1.00\n",u);
    printf("%d nota(s) de R$ 0.50\n",a);
    printf("%d nota(s) de R$ 0.25\n",b);
    printf("%d nota(s) de R$ 0.10\n",e);
    printf("%d nota(s) de R$ 0.05\n",h);
    printf("%.0f nota(s) de R$ 0.01\n",l);
   
    return 0;
}