#define PY_SSIZE_T_CLEAN
#include <Python.h>

// Function definition:
static PyObject *printer(PyObject *self, PyObject *args)
{
    printf("Hello from C\n");
    return Py_None;
}

// struct used to describe a method of an extension type:
static PyMethodDef module_methods[] = {
    {"printer", printer, METH_NOARGS, "Hello from C"},
    {NULL, NULL, 0, NULL}}; // signal the end of the method definitions

// The PyModuleDef is the module definition struct:
static struct PyModuleDef c_functions =
    {
        PyModuleDef_HEAD_INIT,
        "c_functions", // Module name
        "",            // Module documentation, may be an empty string
        -1,            /* size of per-interpreter state of the module, or -1 if the module keeps state in global variables. */
        module_methods};

// The module initialization function:
PyMODINIT_FUNC PyInit_c_functions(void)
{
    return PyModule_Create(&c_functions);
}