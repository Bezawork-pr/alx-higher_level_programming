#include <stdlib.h>
#include <stdio.h>
#include "lists.h"
/**
 * whennull - adds when null
 *
 * @newhead: add list here
 *
 * @copyhead: copy of orginal head
 *
 * Return: pointer to head
 */
listint_t *whennull(listint_t **newhead, listint_t *copyhead)
{
	listint_t *new;

	new = malloc(sizeof(listint_t) * 100);
	if (new == NULL)
	{
		free(new);
		return (NULL);
	}
	*newhead = new;
	new->n = copyhead->n;
	new->next = NULL;
	return (*newhead);
}
/**
 * reverse - copy reversed list when not null
 *
 * @newhead : add new node here
 *
 * @copyhead: copy of orginal head
 *
 * Return: pointer to new head
 */
listint_t *reverse(listint_t **newhead, listint_t *copyhead)
{
	listint_t *new;
	listint_t *anothertemp;

	new = malloc(sizeof(listint_t) * 100);
	if (new == NULL)
	{
		free(new);
		return (NULL);
	}
	anothertemp = *newhead;
	*newhead = new;
	new->n = copyhead->n;
	new->next = anothertemp;
	return (*newhead);
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
	listint_t *temp;
	listint_t *copyhead;
	listint_t *anothercphead;

	copyhead = *head;
	anothercphead = *head;
	temp = malloc(sizeof(listint_t) * 100);
	temp = NULL;
	if (*head == NULL)
		return (1);
	temp = whennull(&temp, copyhead);
	while (anothercphead != NULL)
	{
		reverse(&temp, anothercphead);
		anothercphead = anothercphead->next;
	}
	while (*head)
	{
		if ((*head)->n != (temp->n))
		{
			free_listint(temp);
			return (0);
		}
		temp = temp->next;
		*head = (*head)->next;
	}
	free_listint(temp);

	return (1);
}
