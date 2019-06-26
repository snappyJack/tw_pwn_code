#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void noShell(void) {
    system("QaQ");
}

int main(void) {
    setvbuf(stdout, 0LL, 2, 0LL);
    setvbuf(stdin, 0LL, 1, 0LL);
    char msg[128];

    puts("=====================");
    puts("=echo server v1.0=");
    puts("=====================");

    for (;;) {
        if (!strcmp(msg, "Exit")) {
            exit(0);
        }
        fgets(msg, 128, stdin);
        printf(msg);
    }
}
