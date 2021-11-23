
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int main()
{
int a = -2;
int b = -6;
int c = ~(a | b);
int d = 4;
int e = ~(d | d);
int f = ~(d | a);
int h = ~(-5 | a);
    return 0;
}