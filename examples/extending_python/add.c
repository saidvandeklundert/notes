void add_one(int* x){
    *x += 1;
}
// gcc -c -fpic add.c
// gcc -shared -o libadd1.so add.o