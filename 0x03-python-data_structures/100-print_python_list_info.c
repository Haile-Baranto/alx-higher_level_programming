#include <object.h>
#include <Python.h>
#include <listobject.h>

void print_python_list_info(PyObject *p)
{
        long int size = PyList_Size(p);
        PyListObject *obj = (PyListObject *)p;
	 int count;

        printf("[*] Size of the Python List = %li\n", size);
        printf("[*] Allocated = %li\n", obj->allocated);
        for (count = 0; count < size; count++)
                printf("Element %count: %s\n", count, Py_TYPE(obj->ob_item[count])->tp_name);

