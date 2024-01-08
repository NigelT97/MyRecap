#include "main.h"

int random_maker(int i_var)
{
    int x, y, z;

    x = i_var;
    y = 100 - (x * 5);
    z = 1 + y;

    return (z);
}