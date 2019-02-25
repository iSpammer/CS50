#include <stdio.h>
#include <time.h>
#include <stdlib.h>

int main(){
    int t1 = clock();
    for (int i = 0; i<100000; i++);
    int t2 = clock();

    printf("%f\n", (float)t1/CLOCKS_PER_SEC);
    printf("%f\n", (float)t2/CLOCKS_PER_SEC);

    float t = (float)t2/CLOCKS_PER_SEC - (float)t1/CLOCKS_PER_SEC;

    printf("%f\n",t);
}