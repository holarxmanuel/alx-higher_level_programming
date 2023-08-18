#include <Python.h>

void custom_print_python_list(PyObject *p);
void custom_print_python_bytes(PyObject *p);

/**
 * custom_print_python_list - Prints basic info about Python lists.
 * @p: A PyObject list object.
 */
void custom_print_python_list(PyObject *p)
{
	int size, alloc, idx;
	const char *type;
	PyListObject *list = (PyListObject *)p;
	PyVarObject *var = (PyVarObject *)p;

	size = var->ob_size;
	alloc = list->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);

	for (idx = 0; idx < size; idx++)
	{
		type = list->ob_item[idx]->ob_type->tp_name;
		printf("Element %d: %s\n", idx, type);
		if (strcmp(type, "bytes") == 0)
			custom_print_python_bytes(list->ob_item[idx]);
	}
}

/**
 * custom_print_python_bytes - Prints basic info about Python byte objects.
 * @p: A PyObject byte object.
 */
void custom_print_python_bytes(PyObject *p)
{
	unsigned char i, bytes_size;
	PyBytesObject *bytes = (PyBytesObject *)p;

	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
	printf("  trying string: %s\n", bytes->ob_sval);

	if (((PyVarObject *)p)->ob_size > 10)
		bytes_size = 10;
	else
		bytes_size = ((PyVarObject *)p)->ob_size + 1;

	printf("  first %d bytes: ", bytes_size);
	for (i = 0; i < bytes_size; i++)
	{
		printf("%02hhx", bytes->ob_sval[i]);
		if (i == (bytes_size - 1))
			printf("\n");
		else
			printf(" ");
	}
}
