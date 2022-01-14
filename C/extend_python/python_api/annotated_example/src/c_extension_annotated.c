#define PY_SSIZE_T_CLEAN
#include <Python.h>

// Multiplier function:
int multiplier(int a, int b)
{
    return a * b;
}

//  contains the information Python needs to treat a pointer to an object as an object
static PyObject *c_multiplier(PyObject *self, PyObject *args)
{
    // Declare variables:
    int a;
    int b;
    int ret;
    // Receive arguments from the Python runtime:
    if (!PyArg_ParseTuple(args, "ii", &a, &b))
    {
        return NULL;
    }
    // run the multiplier function:
    ret = multiplier(a, b);
    // Build a value that we can return to the Python runtime:
    return Py_BuildValue("i", ret);
}

// struct with an array of methods:
static PyMethodDef module_methods[] = {
    // Here we define the methods we want to expose to Python:
    {"multiplier", c_multiplier, METH_VARARGS, "Multiply two numbers."},
    {NULL, NULL, 0, NULL}}; // signal the end of the method definitions

// Define the module struct:
static struct PyModuleDef c_extension =
    {
        PyModuleDef_HEAD_INIT,
        "c_extension", // the name of the module in Python
        "",            // The docstring in Python
        -1,            /* size of per-interpreter state of the module, or -1 if the module keeps state in global variables. */
        module_methods};

// Define the module initialization function:
PyMODINIT_FUNC PyInit_c_extension(void)
{
    return PyModule_Create(&c_extension);
}
/*
    Note that the 'c_extension' name. It appears three times:
    - PyModuleDef
    - PyModuleDef_HEAD_INIT
    - as part of the PyMODINIT_FUNC 'PyInit_c_extension'

    This has to match. You will not see a compiler error or warning if this does not match.

*/
