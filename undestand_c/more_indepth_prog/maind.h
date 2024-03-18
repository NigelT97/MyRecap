#ifndef MAIND_H
#define MAIND_H

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct p_data
{
    char *name;
    int age;
    int year_born;
    char *nickname;
} ;

void full_info(struct p_data info);
struct p_data tabulate_info(char *argv_info);
int current_year(int age, int year);

#endif