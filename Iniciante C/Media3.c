#include <stdio.h>
int main(){
    float n1,n2,n3,n4,media,q,m;
    scanf("%f%f%f%f",&n1,&n2,&n3,&n4);
    media = (n1*2+n2*3+n3*4+n4*1)/10.0;
    
    if (media>=7.0)
        {
            printf("Media: %.1f\n",media);
            printf("Aluno aprovado.\n");
        }
    
    else if(media<5)
        {
            printf("Media: %.1f\n",media);
            printf("Aluno reprovado.\n");
        }

    else if(media>=5.0 && media<=6.9)
        {
        scanf("%f",&q);
        m = ((q+media)/2.0);
        printf("Media: %.1f\n",media);
        printf("Aluno em exame.\n");
        printf("Nota do exame: %.1f\n",q);
        if (m>=5.0)
            {
                printf("Aluno aprovado.\n");
            }

        else
            {
                printf("Aluno reprovado.\n");
            }

        printf("Media final: %.1f\n",m);
        }

    return 0;
}