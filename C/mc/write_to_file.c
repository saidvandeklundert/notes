#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[argc + 1])
{
    FILE *logfile = fopen("mylog.txt", "a");
    if (!logfile)
    {
        perror("fopen failed");
        return EXIT_FAILURE;
    }
    fputs("feeling fine today\n", logfile);
    return EXIT_SUCCESS;
}