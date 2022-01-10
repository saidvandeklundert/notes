#include <Python.h>

// the function:
int square(int n)
{

    return n * n;
}

// The PyObject:
static PyObject *square_func(PyObject *self, PyObject *args)
{
    int n;
    if (!PyArg_ParseTuple(args, "i", &n))
        return NULL;
    return Py_BuildValue("i", square(n));
}

static PyMethodDef module_methods[] = {
    {"square_func", (PyCFunction)square_func, METH_VARARGS, "multiply n by n"},
    {NULL, NULL, 0, NULL}};

static struct PyModuleDef helloworld =
    {
        PyModuleDef_HEAD_INIT,
        "helloworld", /* name of module */
        "",           /* module documentation, may be NULL */
        -1,           /* size of per-interpreter state of the module, or -1 if the module keeps state in global variables. */
        module_methods};

PyMODINIT_FUNC PyInit_cModPyDem(void)
{
    return PyModule_Create(&helloworld);
}