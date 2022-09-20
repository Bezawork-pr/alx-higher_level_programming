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
	listint_t *temp;
	listint_t *new;

	new = malloc(sizeof(listint_t));
	while (*head)
	{
		if ((number > ((*head)->n)))
			*head = (*head)->next;
		else
		{
			temp = *head;
			*head = new;
			new->n = number;
			new->next = temp;
			printf("%d", new->n);
			return (*head);
		}
	}
	return (NULL);
}
