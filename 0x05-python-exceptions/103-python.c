#include <Python.h>
#include <stdio.h>

/**
 * print_python_list - Print information about a Python list object.
 * @p: Pointer to the Python list object.
 */
void print_python_list(PyObject *p)
{
	if (PyList_Check(p))
	{
		printf("[*] Python list info\n");
		printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
		printf("[*] Size = %ld\n", PyList_Size(p));
		for (Py_ssize_t i = 0; i < PyList_Size(p); i++)
		{
			printf("Element %ld: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
		}
	}
	else
	{
		fprintf(stderr, "[ERROR] Invalid List Object\n");
		return;
	}
}

/**
 * print_python_bytes - Print information about a Python bytes object.
 * @p: Pointer to the Python bytes object.
 */
void print_python_bytes(PyObject *p)
{
	if (PyBytes_Check(p))
	{
		printf("[.] bytes object info\n");
		printf("  size: %ld\n", PyBytes_Size(p));
		printf("  trying string: %s\n", PyBytes_AsString(p));
	}
	else
	{
		fprintf(stderr, "[ERROR] Invalid Bytes Object\n");
		return;
	}
}

/**
 * print_python_float - Print information about a Python float object.
 * @p: Pointer to the Python float object.
 */
void print_python_float(PyObject *p)
{
	if (PyFloat_Check(p))
	{
		printf("[.] float object info\n");
		printf("  value: %f\n", PyFloat_AsDouble(p));
	}
	else
	{
		fprintf(stderr, "[ERROR] Invalid Float Object\n");
		return;
	}
}
