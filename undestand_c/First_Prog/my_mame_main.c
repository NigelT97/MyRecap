#include "main.h"

int main(void)
{
   char name[] = "Nigel Tangaona";
   char surname[] = "Masiyazi-Ngorima";
   int bod = 1997, age, comb;

   printf("My name is %s \nAnd my surname is %s.", name, surname);
   age = age_calc(bod);

   for (comb = 1; comb < 6; comb++)
   {
    age = age + comb;
    if (comb == 1)
    {
        printf("\nIn %d years I will be %d years.", comb, age);
    }
    else
    {
        printf("\nConservatively from the preivous year in %d years I will be %d years.", comb, age);
    }

    
   }

   return (0);
}