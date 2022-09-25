#include "lists.h"
/**
 * counter - counts how many nodes in a list
 *
 * @head: head of linked list
 *
 * Return: number of nodes
 */
int counter(listint_t **head)
{
	int i = 0;

	while (*head)
	{
		i++;
		*head = (*head)->next;
	}
	return (i - 1);
}
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
	int i = 0, n = 0, listsize = counter(head);
	int arrayforint[listsize];

	while (temp)
	{
		arrayforint[i] = temp->n;
		i++;
		temp = temp->next;
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
