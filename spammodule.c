#include <Python.h>

static PyObject * spam_system(PyObject *self, PyObject *args) {
    const char *command;
    
    if (!PyArg_ParseTuple(args, "s", &command)) {
        return NULL;
    }
    int sts = system(command);
    return Py_BuildValue("i", sts);
}

static PyMethodDef spam_methods[] = {
    {"system", spam_system, METH_VARARGS, "Execute a shell command."},
    {NULL, NULL, 0, NULL} /* sentinel */
};

PyMODINIT_FUNC initspam(void) {
    PyImport_AddModule("spam");
    Py_InitModule("spam", spam_methods);
}
