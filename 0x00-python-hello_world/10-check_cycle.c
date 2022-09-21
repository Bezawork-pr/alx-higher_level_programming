#include "lists.h"
/**
 * check_cycle - checks if there is cycle
 *
 * @list: takes head of linked list
 *
 * Return: 1 if there is cycle 0 if there is no cycle
 */
int check_cycle(listint_t *list)
{
	int flag = 0;
	int copy;
	int count = 0;

	if (list)
		copy = list->n;
	while (list)
	{
		if ((list->n == copy) && (flag == 0))
			flag = 1;
		else if ((list->n == copy) && (flag == 1))
			return (1);
		count++;
		if (count == 1000)
			return (1);
		list = list->next;
	}
	return (0);
}
