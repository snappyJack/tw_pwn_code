#include <stdio.h>
#include <stdlib.h>

char modifyme = 'x';

int main(void) {
    char buf[100];
    printf("try to modify the value\n");
    gets(buf);
    printf(buf);
    if (modifyme == 'O')
        printf("good\n");
    return 0;
}
