#include "lists.h"
/**
 * insert_node- inserts node
 *
 * @head: head of linked list
 *
 * @number: number to inset
 *
 * Return: address or NULL on failure
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *next, *new, *current, *previous;
	int flag = 0;

	new = malloc(sizeof(listint_t));
	current = *head;
	previous = *head;
	if (*head == NULL)
	{
		*head = new;
		new->n = number;
		new->next = NULL;
		return (new);
	}
	while (current)
	{
		if (number > (*head)->n)
			flag = 1;
		if ((number < ((*head)->n)) && (flag == 0))
		{
			next = *head;
			*head = new;
			new->n = number;
			new->next = next;
			return (new);
		}
		else if ((number < ((current)->n)) && (flag != 0))
		{
			next = current;
			previous->next = new;
			new->n = number;
			new->next = next;
			return (new);
		}
		else
			previous = current;
		previous = current;
		current = current->next;
	}
	free(new);
	return (NULL);
}
