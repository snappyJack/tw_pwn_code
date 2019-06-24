#include <stdio.h>
#include <stdlib.h>

void foo(int a, int b) {
    char buf[40];
    gets(buf);
}
void Neveruse() {
    system("sh");
}

int main(){
    setvbuf(stdout, 0LL, 2, 0LL);
    setvbuf(stdin, 0LL, 2, 0LL);
    puts("this is a test");
    foo(1, 2);
}
