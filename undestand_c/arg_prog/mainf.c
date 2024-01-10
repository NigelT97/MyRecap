#include "mainf.h"

int main(int argc, char **argv)
{
    int result, x, y;
    char *a, *b;

    if (argc == 9)
    {
        argv[2] = "*";
        argv[3] = argv[8];
    }
    else if (argc != 4)
    {
        printf("Error! Make sure its 2 numbers and an operator in-between.\nExample: 5 + 6\n");
        printf("%d is the count\n", argc);
        return (0);
    }
    
    a = argv[1];
    b = argv[3];
    x = atoi(a);
    y = atoi(b);

    result = operation_result(x, y, argv[2]);

    printf("\n%d %s %d = %d\n", x, argv[2], y, result);

    return (0);
}