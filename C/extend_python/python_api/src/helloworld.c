#define PY_SSIZE_T_CLEAN
#include <Python.h>

// Function: hello from C
static PyObject *hello(PyObject *self, PyObject *args)
{
    printf("Hello from C\n");
    return Py_None;
}

// A C function that we will be exporting:
int square(int n)
{

    return n + n;
}

// The PyObject:
//
//  All object types are extensions of this type.
//  This is a type which contains the information Python needs to treat a pointer to an object as an object.
static PyObject *square_name_in_python(PyObject *self, PyObject *args)
{
    int n;
    if (!PyArg_ParseTuple(args, "i", &n))
        return NULL;
    return Py_BuildValue("i", square(n));
}

// struct used to describe a method of an extension type:
static PyMethodDef module_methods[] = {
    {"hello", hello, METH_NOARGS, "Prints Hello World"},
    {"square_name_in_python", (PyCFunction)square_name_in_python, METH_VARARGS, "multiply n by n"},
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