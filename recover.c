#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

typedef uint8_t BYTE;
const int BLOCK_SIZE = 512;

int main(int argc, char *argv[])
{
    // Accept a single command-line argument
    if (argc != 2)
    {
        printf("Usage: ./recover FILE\n");
        return 1;
    }

    // Open the memory card
    FILE *card = fopen(argv[1], "r");
    if (card == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }

    // Create a buffer for a block of data
    BYTE buffer[BLOCK_SIZE];

    FILE *output = NULL;

    char filename[8];

    int img_counter = 0;

    // While there's still data left to read from the memory card
    while (fread(buffer, sizeof(BYTE), BLOCK_SIZE, card) == BLOCK_SIZE)
    {
        // Create JPEGs from the data
        if (buffer[0] == 0xff)
        {
            if (buffer[1] == 0xd8)
            {
                if (buffer[2] == 0xff)
                {
                    if ((buffer[3] & 0xf0) == 0xe0)
                    {
                        // if first image, create new file and write
                        if (img_counter == 0)
                        {
                            sprintf(filename, "%03i.jpg", img_counter);
                            output = fopen(filename, "w");
                            fwrite(buffer, sizeof(BYTE), BLOCK_SIZE, output);
                            img_counter++;
                        }
                        // if new image, close ouput and create new file and write
                        else if (img_counter > 0)
                        {
                            fclose(output);
                            sprintf(filename, "%03i.jpg", img_counter);
                            output = fopen(filename, "w");
                            fwrite(buffer, sizeof(BYTE), BLOCK_SIZE, output);
                            img_counter++;
                        }
                    }
                    else if (img_counter > 0)
                    {
                        fwrite(buffer, sizeof(BYTE), BLOCK_SIZE, output);
                    }
                }
                else if (img_counter > 0)
                {
                    fwrite(buffer, sizeof(BYTE), BLOCK_SIZE, output);
                }
            }
            else if (img_counter > 0)
            {
                fwrite(buffer, sizeof(BYTE), BLOCK_SIZE, output);
            }
        }
        /*
                if (img_counter > 100)
                {
                    return 1;
                }
        */
        else if (img_counter > 0)
        {
            fwrite(buffer, sizeof(BYTE), BLOCK_SIZE, output);
        }
    }

    // Close files
    fclose(card);
    fclose(output);
}
