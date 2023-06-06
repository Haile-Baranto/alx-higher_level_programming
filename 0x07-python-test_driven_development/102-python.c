#include "Python.h"

/*
 * print_python_string - Prints information about Python strings.
 * @str_obj: A PyObject string object.
 */
void print_python_string(PyObject *str_obj)
{
    long int str_length;

    fflush(stdout);

    /* Print section header */
    printf("[.] string object info\n");

    /* Check if the object is a valid string */
    if (strcmp(str_obj->ob_type->tp_name, "str") != 0)
    {
        /* Print error message for invalid string object */
        printf("  [ERROR] Invalid String Object\n");
        return;
    }

    /* Get the length of the string */
    str_length = ((PyASCIIObject *)(str_obj))->length;

    /* Check if the string is in compact ASCII format */
    if (PyUnicode_IS_COMPACT_ASCII(str_obj))
    {
        /* String is in compact ASCII format */
        printf("  type: compact ascii\n");
    }
    else
    {
        /* String is in compact unicode format */
        printf("  type: compact unicode object\n");
    }

    /* Print the length of the string */
    printf("  length: %ld\n", str_length);

    /* Print the value of the string */
    printf("  value: %ls\n", PyUnicode_AsWideCharString(str_obj, &str_length));
}