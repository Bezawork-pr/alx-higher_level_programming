#include <stdlib.h>
#include "lists.h"
int counter(listint_t *temp);
/**
 * is_palindrome - checks if linked list is palindrome
 *
 * @head: head of linked list
 *
 * Return: 1 if palindrome
 * otherwise 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp = *head;
	listint_t *temp2 = *head;
	int i = 0, n = 0, listsize = counter(temp);
	int arrayforint[listsize];

	if (listsize == 0)
		return (1);
	while (temp2)
	{
		arrayforint[i] = temp2->n;
		i++;
		temp2 = temp2->next;
	}
	while (n <= listsize)
	{
		if (arrayforint[n] == arrayforint[listsize])
		{
			n++;
			listsize--;
		}
		else
			return (0);
	}
	return (1);
}
/**
 * counter - counts how many nodes in a list
 *
 * @temp: head of linked list
 *
 * Return: number of nodes
 */
int counter(listint_t *temp)
{
	int i = 0;

	if (temp == NULL || temp->next == NULL)
		return (0);
	while (temp)
	{
		i++;
		temp = temp->next;
	}
	return (i - 1);
}
