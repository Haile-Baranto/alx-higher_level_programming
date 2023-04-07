#include <Python.h>

void print_python_string(PyObject *p)
{
    const char *str;
    Py_ssize_t len;

    if (!PyUnicode_Check(p)) {
        printf("  [ERROR] Invalid String Object\n");
        PyErr_Print();
        return;
    }

    str = PyUnicode_AsUTF8AndSize(p, &len);
    printf("  %s\n", str);
}
