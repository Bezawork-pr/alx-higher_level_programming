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
	listint_t *next;
	listint_t *new;
	listint_t *current;
	listint_t *previous;

	new = malloc(sizeof(listint_t));
	current = *head;
	while (current)
	{
		if ((number < ((current)->n)))
		{
			next = current;
			previous->next = new;
			new->n = number;
			new->next = next;
			return (new);
		}
		previous = current;
		current = current->next;
	}
	free(new);
	return (NULL);
}
