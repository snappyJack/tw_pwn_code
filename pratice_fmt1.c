#include <stdio.h>
#include <stdlib.h>

char flag[100];

int main(void) {
    char I[100];
    char MADE[100];
    char A[100];
    char STUPID[100];
    char MISTAKE[100];
    FILE *fp = fopen("/home/morty/flag", "r");
    fscanf(fp, "%s", flag);
    printf("flag is %p .\n", flag);
    fflush(stdout);
    read(0, STUPID, 100);
    char *QQ = alloca(100);
    printf(STUPID);
    fclose(fp);
    return 0;
}
