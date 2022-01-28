#define PY_SSIZE_T_CLEAN
#include <Python.h>
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

int run_struct_methods(int a, int b)
{

    func_struct.talk = &talk;
    func_struct.talk();

    func_struct.multiplier = &multiplier;
    int c;
    c = func_struct.multiplier(a, b);
    printf("multiplier result: %d\n",
           a);
    printf("finished\n");

    return (0);
}
static PyObject *func_that_runs_int_python(PyObject *self, PyObject *args)
{
    int a;
    int b;
    int ret;
    if (!PyArg_ParseTuple(args, "ii", &a, &b))
    {
        return NULL;
    }
    ret = run_struct_methods(a, b);
    return Py_BuildValue("i", ret);
}

// multiplier

static PyObject *c_multiplier(PyObject *self, PyObject *args)
{
    int a;
    int b;
    int ret;
    if (!PyArg_ParseTuple(args, "ii", &a, &b))
    {
        return NULL;
    }
    ret = multiplier(a, b);
    return Py_BuildValue("i", ret);
}

static PyMethodDef module_methods[] = {
    {"multiplier", c_multiplier, METH_VARARGS, "Multiply two numbers."},
    {"run_struct_methods", func_that_runs_int_python, METH_VARARGS, "Crazy stuff."},
    {NULL, NULL, 0, NULL}};

static struct PyModuleDef samples =
    {
        PyModuleDef_HEAD_INIT,
        "samples",
        "",
        -1,
        module_methods};

PyMODINIT_FUNC PyInit_samples(void)
{
    return PyModule_Create(&samples);
}
