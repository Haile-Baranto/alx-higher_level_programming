#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>

void print_python_bytes(PyObject *p)
{
        long int size;
        int count;
        char *trying_str = NULL;

        printf("[.] bytes object info\n");
        if (!PyBytes_Check(p))
        {
                printf("  [ERROR] Invalid Bytes Object\n");
                return;
        }

        PyBytes_AsStringAndSize(p, &trying_str, &size);

        printf("  size: %li\n", size);
        printf("  trying string: %s\n", trying_str);
        if (size < 10)
                printf("  first %li bytes:", size + 1);
        else
                printf("  first 10 bytes:");
        for (count = 0; count <= size && count < 10; count++)
                printf(" %02hhx", trying_str[count]);
        printf("\n");
}

void print_python_list(PyObject *p)
{
        long int size = PyList_Size(p);
        int count;
        PyListObject *list = (PyListObject *)p;
        const char *type;

        printf("[*] Python list info\n");
        printf("[*] Size of the Python List = %li\n", size);
        printf("[*] Allocated = %li\n", list->allocated);
        for (count = 0; count < size; count++)
        {
                type = (list->ob_item[count])->ob_type->tp_name;
                printf("Element %count: %s\n", count, type);
                if (!strcmp(type, "bytes"))
                        print_python_bytes(list->ob_item[count]);
        }
}