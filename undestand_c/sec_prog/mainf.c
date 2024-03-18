#include <stdio.h>

void print_loop(int *arrayl)
{
    int i, size_l;

    size_l = sizeof(arrayl);
    
    for (i = 0; i <= size_l; i++)
    {
        printf("%d  ", arrayl[i]);
    }

    return;
}

void printlist(int *array1, int *array2, int *array3)
{
    printf("List of generated numbers: \n");
    print_loop(array1);
    printf("\nThe ones that are  even:\n");
    print_loop(array2);
    printf("\nThe list of odd numbers:\n");
    print_loop(array3);
    return;
}

int main(void)
{
    int numbers[24], i, j, k;
    int numbj[24], numbk[24];

    for(i = 0; i < 25; i++)
    {
        numbers[i] = (i + 1) * (41 - i) - 20;
    }

    for(i = 0, j = 0, k = 0; i < 24; i++)
    {
        if (numbers[i] % 2 == 0)
        {
            numbj[j] = numbers[i];
            j++;
        }
        else
        {
            numbk[k] = numbers[k];
            k++;
        }
    } 
    printlist(numbers, numbj, numbk);

    return (0);

}

