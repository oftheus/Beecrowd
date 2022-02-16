#include <stdio.h>
int main(){
    int x,y;
    scanf("%d",&x);
    scanf("%d",&y);
    double z = (x*y);
    double h = z/12;
    printf("%.3lf",h);
    return 0;
}