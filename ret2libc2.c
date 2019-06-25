#include <stdio.h>
#include <stdlib.h>
#include <time.h>

char buf2[100];

void secure(void) {
    int secretcode, input;
    srand(time(NULL));

    secretcode = rand();
    scanf("%d", &input);
    if (input == secretcode)
        system("shell?");
}

int main(void) {
    setvbuf(stdout, 0LL, 2, 0LL);
    setvbuf(stdin, 0LL, 1, 0LL);

    char buf1[100];
    puts("this is a test");
    gets(buf1);
    return 0;
}
