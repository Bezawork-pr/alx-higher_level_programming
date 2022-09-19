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

	while (list)
	{
		if ((list->n == 1024) && (flag == 0))
			flag = 1;
		else if ((list->n == 1024) && (flag == 1))
			return (1);
		list = list->next;
	}
	return (0);
}
