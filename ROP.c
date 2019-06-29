#include <stdio.h>
#include <stdlib.h>

char *shell = "/bin/sh";

int main(void)
{
setvbuf(stdout,0LL,2,0LL);
setvbuf(stdin,0LL,1,0LL);

char buf[100];

printf("what do you plan to do?")

gets(buf);
}
