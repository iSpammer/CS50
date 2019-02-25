#include <stdio.h>

int main(){
    int cache[8];
    int hit = 0;
    int miss = 0;
    int tag;
    int addr;
    int i;

    FILE *f;

    f = fopen("lab2.txt", "r");

    while((fscanf(f, "%d", &addr))!=EOF){
        i = addr % 8;
        tag = addr >> 3;
        if(cache[i] == tag){
            hit ++;
        }
        else{
            miss++;
            cache[i] = tag;
        }
    }
    fclose(f);
    printf("%d", miss);
    printf("%d",hit);
}