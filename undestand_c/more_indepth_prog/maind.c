#include "maind.h"

int main(int argc, char *argv[])
{
    struct p_data personal_info;

    if (argc != 5)
    {
        printf("Please enter like:\n main_program Name Age Year_born Nickname\n");
        return (0);
    }

    printf("Hie %s\n", argv[1]);

    personal_info = tabulate_info(*argv);

    printf("So your choosed nickname is %s\n", personal_info.nickname);


    return (0);

}