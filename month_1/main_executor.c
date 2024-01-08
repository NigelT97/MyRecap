#include "main.h"
#include <stdio.h>

int main(void)
{
    int values[10], i, result;

    for (i = 0; i < 10; i++)
    {
        values[i] = random_maker(i);
        result = grade_decider(values[i]);
        printf("%d = max", result);
    }

    return 0;
}