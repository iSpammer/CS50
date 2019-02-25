#include <stdio.h>
#include <stdlib.h>
#include <cs50.h>

int main(int argc, char *argv[])
{

    if (argc != 2)
    {
        fprintf(stderr, "usage ./recover car.raw\n");
        return 1;
    }
    //open the card file
    char *infile = argv[1];
    FILE *outptr = fopen(infile, "r");
    if (outptr == NULL)
    {
        fprintf(stderr, "Forensic image cannot be opened for reading\n");
        return 2;
    }

    //read 512 byte
    unsigned char buffer [512];
    bool jpgFound = false;
    int i = 0; //jpeg counter
    FILE *img;
    // loop till you reach eof
    while (fread(buffer, 1, 512, outptr) != 0x00)
    {
        //check jpeg header pattern
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            //if we didnt found the 1st jpeg
            if (!jpgFound)
            {
                //change first jpg boolean to true
                jpgFound = true;
                //write the bytes of new jpg in new file
                char filename[8];
                //open/create the file
                sprintf(filename, "%03i.jpg", i++);
                img = fopen(filename, "w");
                if (img == NULL)
                {
                    return 3;

                }
                //write data to the new file
                fwrite(buffer, 1, 512, img);
            }
            else
            {
                //close prev file
                fclose(img);
                //write data to new file
                //open/ create new file
                char filename[8];
                sprintf(filename, "%03i.jpg", i++);
                img = fopen(filename, "w");
                if (img == NULL)
                    return 3;
                //write data to a new file
                fwrite(buffer, 1, 512, img);
            }
        }
        else
        {
            //if we found the 1sst jpg
            if (jpgFound)
            {
                //continue to write bytes
                fwrite(buffer, 1, 512, img);
            }
        }
    }
    //close all files and free the memory
    fclose(outptr);
    fclose(img);
    return 0;
}

