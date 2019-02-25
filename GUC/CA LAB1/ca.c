#include <stdio.h>
#define MACCHAR 1000

int main(){
    long cache[8];
    int miss = 0;
    int hit = 0;
    long i , v , addr;

    FILE *f;
    f = fopen("lab2.txt", "r");
    while((fscanf(f, "%ld", &addr))!=EOF){
        i = addr % 8;
        v = addr >> 3;
        if(cache[i] == v){
            hit ++;
        }
        else{
            miss++;
            cache[i] = v;
        }
    }
    fclose(f);
    printf("%d miss \n", miss);
    printf("%d hits \n", hit);
    // for(i = 0; i< sizeof(cache); i++)
    // {
    //     printf("%ld\n", cache[i]);
    // }
    return 0;
}