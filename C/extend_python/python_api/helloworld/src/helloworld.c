#define PY_SSIZE_T_CLEAN
#include <Python.h>

// Function definition:
static PyObject *hello(PyObject *self, PyObject *args)
{
    printf("Hello from C\n");
    return Py_None;
}

// struct used to describe a method of an extension type:
static PyMethodDef module_methods[] = {
    {"hello", hello, METH_NOARGS, "Prints Hello World"},
    {NULL, NULL, 0, NULL}}; // signal the end of the method definitions

// The PyModuleDef is the module definition struct:
static struct PyModuleDef helloworld =
    {
        PyModuleDef_HEAD_INIT,
        "helloworld", /* name of module */
        "",           /* module documentation, may be NULL */
        -1,           /* size of per-interpreter state of the module, or -1 if the module keeps state in global variables. */
        module_methods};

// The module initialization function:
PyMODINIT_FUNC PyInit_helloworld(void)
{
    return PyModule_Create(&helloworld);
}