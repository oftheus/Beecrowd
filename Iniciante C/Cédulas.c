#include <stdio.h>
int main(){
    int x;
    scanf("%d",&x);
    int q = x/100;
    int c = (x-(q*100))/50;
    int v= (x-(c*50)-(q*100))/20;
    int d=(x-(v*20)-(c*50)-(q*100))/10;
    int f=(x-(d*10)-(v*20)-(c*50)-(q*100))/5;
    int g=(x-(f*5)-(d*10)-(v*20)-(c*50)-(q*100))/2;
    int u=(x-(g*2)-(f*5)-(d*10)-(v*20)-(c*50)-(q*100))/1;
    printf("%d\n", x);
    printf("%d nota(s) de R$ 100,00\n",q);
    printf("%d nota(s) de R$ 50,00\n",c);
    printf("%d nota(s) de R$ 20,00\n",v);
    printf("%d nota(s) de R$ 10,00\n",d);
    printf("%d nota(s) de R$ 5,00\n",f);
    printf("%d nota(s) de R$ 2,00\n",g);
    printf("%d nota(s) de R$ 1,00\n",u);
    return 0;
}