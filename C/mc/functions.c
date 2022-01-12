#include <stdio.h>

int multiply(int a, int b)
{
    return a * b;
}

int return_a_function(int a)
{
    while (a <= 5)
    {
        printf("%d\n", a);
        ++a;
    }
    printf("inside return a func: %d", a);
    return multiply(a, a);
}

int recursion(int a)
{
    if (a == 10)
    {
        return a;
    }
    printf("going for the recursion, currently at %d\n", a);
    ++a;
    return recursion(a);
}

size_t fibonacci(size_t n)
{
    if (n < 3)
        return 1;
    else
        return fibonacci(n - 1) + fibonacci(n - 2);
}

/*
fibonacci again, but with a cache:
*/
size_t fibCacheRec(size_t n, size_t cache[n])
{
    if (!cache[n - 1])
    {
        cache[n - 1] = fibCacheRec(n - 1, cache) + fibCacheRec(n - 2, cache);
    }
    return cache[n - 1];
}

size_t fibCache(size_t n)
{
    if (n + 1 <= 3)
        return 1;
    /* setup VLA to cache values */
    size_t cache[n];
    /* VLA must be initialized by assignment */
    cache[0] = 1;
    cache[1] = 1;
    for (size_t i = 2; i < n; ++i)
        cache[i] = 0;
    /* call the recursive function */
    return fibCacheRec(n, cache);
}

int main()
{

    int x;

    x = multiply(2, 2);
    printf("x: %d\n", x);

    int y;
    y = return_a_function(2);
    printf("y: %d\n", y);

    recursion(5);
    size_t fib_result;
    fib_result = fibonacci(40); // use a cache for really big numbers
    printf("y: %d\n", fib_result);
    size_t fib_cache_result;
    fib_cache_result = fibCache(240);
    printf("y: %d\n", fib_cache_result);

    return 0;
}