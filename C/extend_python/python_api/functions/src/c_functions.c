#define PY_SSIZE_T_CLEAN
#include <Python.h>

// Example C function from the Python documentation:
static PyObject *
spam_system(PyObject *self, PyObject *args)
{
    const char *command;
    int sts;

    if (!PyArg_ParseTuple(args, "s", &command))
        return NULL;
    sts = system(command);
    return PyLong_FromLong(sts);
}

// Return a greating string:
static PyObject *greeter(PyObject *self, PyObject *args)
{
    char *name;
    char greeting[255] = "Hello ";
    if (!PyArg_ParseTuple(args, "s", &name))
    {
        return NULL;
    }
    strcat(greeting, name);
    return Py_BuildValue("s", greeting);
}

// Return the square value for a number:
static PyObject *square(PyObject *self, PyObject *args)
{
    int n;

    if (!PyArg_ParseTuple(args, "i", &n))
    {
        return NULL;
    }

    return Py_BuildValue("i", c_square(n));
}

// return the cube value for a number:
int c_square(int n)
{
    return n * n;
}

// Print a message to the console using C:
static PyObject *printer(PyObject *self, PyObject *args)
{
    printf("Hello from C\n");
    return Py_None;
}

// struct used to describe a method of an extension type:
static PyMethodDef module_methods[] = {
    {"printer", printer, METH_NOARGS, "Hello from C"},
    // The C function from the Python documentation.
    // Note that it will be available as 'system()' in Python, not 'spamsystem'.
    {"system", spam_system, METH_VARARGS, "Execute a shell command."},
    {"greeter", greeter, METH_VARARGS, "Return a greating to a person."},
    {"square", square, METH_VARARGS, "Return the cube value for a number."},
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