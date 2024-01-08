#include <stdio.h>

int main()
{
    int x, y, b, Nums[3], i;

    x = 7;
    y = x + 18;
    b = x + y;

    Nums[0] = x;
    Nums[1] = y;
    Nums[2] = b;

    for (i = 0; i < 3; i++)
    {
        if (Nums[i] % 2 == 0)
        {
            printf("%d is a even number \n", Nums[i]);
        }
        else
        {
            printf("%d is an odd number \n", Nums[i]);
        }
    }

    return 0;
}