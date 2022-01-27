#include <stdio.h>
// https://www.onlinegdb.com/online_c_compiler
void talk(void)
{
    puts("talktalktalk\n");
}

int multiplier(int a, int b)
{
    return a * b;
}

struct f
{
    void (*talk)();
    int (*multiplier)(int a, int b);
};
struct f func_struct;

int main()
{

    func_struct.talk = &talk;
    func_struct.talk();

    func_struct.multiplier = &multiplier;
    int a, b, c;
    a = 2;
    b = 2;
    c = func_struct.multiplier(a, b);
    printf("multiplier result: %d\n",
           a);
    printf("finished\n");

    return (0);
}