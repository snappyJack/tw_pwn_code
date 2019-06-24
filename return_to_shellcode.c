#include <stdio.h>
#include <stdlib.h>

char buf2[100];

int main(void){
    setvbuf(stdout, 0LL, 2, 0LL);
    setvbuf(stdin, 0LL, 1, 0LL);

    char buf[100];
    puts("this is a test");
    gets(buf);
    strncpy(buf2, buf, 100);
    printf("byebye");
    return 0;
}
