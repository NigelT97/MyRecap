#include "main.h"

int grade_decider(int var_x)
{
    if (var_x < 50)
    {
        printf("%d  is a fail \n", var_x);
        return (0);
    }
    else if (var_x < 75)
    {
        printf("%d is an average pass \n", var_x);
        return (75);
    }
    else if (var_x < 90)
    {
        printf("%d \n is an excellent pass", var_x);
        return (90);
    }
    else
    {
        printf("A++ pass. Brilliant score \n");
        return (100);
    }
    
}
