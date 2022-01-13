#define PY_SSIZE_T_CLEAN
#include <Python.h>

// Multiplier function:
int multiplier(int a, int b)
{
    return a * b;
}

static PyObject *_multiplier(PyObject *self, PyObject *args)
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
    {"multiplier", _multiplier, METH_VARARGS, "Multiply two numbers."},
    {NULL, NULL, 0, NULL}}; // signal the end of the method definitions

// Define the module struct:
static struct PyModuleDef c_functions =
    {
        PyModuleDef_HEAD_INIT,
        "c_extension", // the name of the module in Python
        "",            // The docstring in Python
        -1,            /* size of per-interpreter state of the module, or -1 if the module keeps state in global variables. */
        module_methods};

// Define the module initialization function:
PyMODINIT_FUNC PyInit_c_functions(void)
{
    return PyModule_Create(&c_functions);
}
