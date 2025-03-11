#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, string argv[])
{
    if (argc == 2)
    {
        // printf("correct %s\n", argv[1]);

        // check if entire argv[1] is digits
        int length = strlen(argv[1]);
        for (int j = 0; j < length; j++)
        {
            if (!isdigit(argv[1][j]))
            {
                printf("Usage: ./caesar key\n");
                return 1;
            }
        }

        // MAIN CODE
        int key = atoi(argv[1]);
        // printf("%i is now an integer \n", key);

        string input = get_string("plaintext: ");

        // ci = (pi + k) % 26
        // ciphertext_i = (plaintext_i + key) % remainder_when_divided_by_26

        int len = strlen(input);
        for (int i = 0; i < len; i++)
        {
            char x = input[i];
            // abc..
            if (islower(x))
            {
                x = (x - 'a' + key) % 26 + 'a';
            }
            // ABC...
            if (isupper(x))
            {
                x = (x - 'A' + key) % 26 + 'A';
            }
            // 123...
            if (isdigit(x))
            {
                x = (x - '0' + key) % 10 + '0';
            }

            input[i] = x;
        }

        printf("ciphertext: %s\n", input);
        return 0;
    }
    else
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
}
