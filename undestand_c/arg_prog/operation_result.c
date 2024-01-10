#include "mainf.h"

int operation_result(int x, int y, char *oper)
{
    int result;

    if (strcmp(oper, "+") == 0)
    {
        result = x + y;
    }
    else if (strcmp(oper, "-") == 0)
    {
        result = x - y;
    }
    else if (strcmp(oper, "*") == 0)
    {
        result = x * y;
    }
    else
    {
        result = x / y;
    }

    return (result);
}