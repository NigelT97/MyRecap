#include "maind.h"

struct p_data tabulate_info(char *argv_info)
{
    struct p_data info_tab;

    info_tab.name = argv_info[1];
    info_tab.age = (int)argv_info[2];
    info_tab.year_born = (int)argv_info[3];
    info_tab.nickname = argv_info[4];

    full_info(info_tab);

    return (info_tab);
}

void full_info(struct p_data info)
{
    int age;
    age = current_year(info.age, info.year_born);
    printf("So you are %d and you were born on %d.\nTherefore, this is %d when you have run the programme.\n", (info).age, (info).year_born, age);
    return;
}