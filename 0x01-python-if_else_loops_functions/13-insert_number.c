#include "lists.h"
/**
 * insert_node_attheend - insert node at the end
 *
 * @head: head of linked
 *
 * @number: number to be put for new
 *
 * @count: check loop is not empty
 *
 * Return: new or NULL
 */
listint_t *insert_node_attheend(listint_t **head, int number, int count)
{
	listint_t *temp, *new;

	new = malloc(sizeof(listint_t));
	temp = *head;

	if (count > 1)
	{
		while (temp->next)
			temp = temp->next;
		temp->next = new;
		new->n = number;
		new->next = NULL;
		return (new);
	}
	free(new);
	return (NULL);

}
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
	int flag = 0, count = 0;

	new = malloc(sizeof(listint_t));
	current = *head, previous = *head;
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
			count++;
		previous = current;
		current = current->next;
	}
	return (insert_node_attheend(head, number, count));
}
