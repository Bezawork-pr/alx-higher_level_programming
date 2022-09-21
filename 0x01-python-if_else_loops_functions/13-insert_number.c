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
	listint_t *temp2;

	temp2 = malloc(sizeof(listint_t));
	new = malloc(sizeof(listint_t));
	temp2 = *head;
	while (temp2)
	{
		if ((number < ((temp2)->n)))
		{
			temp = temp2;
			temp2 = new;
			new->n = number;
			new->next = temp;
			free(temp2);
			return (new);
		}
		temp2 = temp2->next;
	}
	return (NULL);
}
