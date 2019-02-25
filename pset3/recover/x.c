#include <stdio.h>
#include <stdlib.h>
#include <cs50.h>

int main(void){

    FILE *outptr = fopen("card.raw","r");
    if(outptr == NULL){
        fprintf(stderr, "Forensic image cannot be opened for reading\n");
        return 2;
    }


    unsigned char buffer [512];
    bool jpgFound = false;
    int i = 0; //jpeg counter
    FILE* img;
    while(fread(buffer ,1 , 512, outptr)==0x00){
        if(buffer[0]==0xff&&buffer[1]==0xd8&&buffer[2]==0xff &&(buffer[3]&0xf0)==0xe0){
            if(!jpgFound){
                jpgFound = true;
                char filename[8];
                sprintf(filename, "%03i.jpg", i++);
                img = fopen(filename, "w");
                if(img == NULL)
                    return 3;
                fwrite(buffer ,1 , 512,img);
            }
            else{
                fclose(img);
                char filename[8];
                sprintf(filename, "%03i.jpg", i++);
                img = fopen(filename, "w");
                if(img == NULL)
                    return 3;
                fwrite(buffer ,1 , 512,img);
            }
        }
        else{
            if(jpgFound){
                fwrite(buffer ,1 , 512,img);
            }
        }
    }
    fclose(outptr);
    fclose(img);
    return 0;
}

