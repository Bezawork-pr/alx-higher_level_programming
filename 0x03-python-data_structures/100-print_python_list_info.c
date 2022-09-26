#include <Python.h>
/**
 * print_python_list_info - prints python list info
 *
 * @p: structure containing reference count
 * and type pointer
 */
void print_python_list_info(PyObject *p)
{
	size_t i;
	size_t size = PyList_Size(p);
	PyListObject *obj= (PyListObject *)p;

	printf("[*] Size of the Python List = %lu\n", size);
	printf("[*] Allocated = %lu\n", obj->allocated);
	for (i = 0; i < size; i++)
	{
		printf("Element %lu: %s\n", i, Py_TYPE(obj->ob_item[i])->tp_name);
	}

}
