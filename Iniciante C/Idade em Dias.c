#include <stdio.h>
int main(){
    int idade,meses,dias;
    scanf("%d",&idade);
    int anos = idade/365;
    if (anos==0)
    {
        meses=idade/30;
    }
    if (anos!=0)
    {
        meses=(idade-anos*365)/30;
    }
    if (meses==0)
    {
       dias=idade;
    }
    if (meses!=0)
    {
        dias=(idade-anos*365-meses*30);
    }
    printf("%d ano(s)\n", anos);
    printf("%d mes(es)\n", meses);
    printf("%d dia(s)\n", dias);
    return 0;
}