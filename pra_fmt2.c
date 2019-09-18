#include <stdio.h>
#include <stdlib.h>

int what_can_i_do() {
    return puts("do nothing");
}

int getflag() {
    return puts("finally I get the flag");
}

int main(void) {
    int (*func)();
    func = &what_can_i_do;

    char buf[1024];
    printf("get something at %p ", &func);
    fflush(stdout);
    fgets(buf, 1024, stdin);
    printf(buf);
    (*func)();

    return 0;
}
