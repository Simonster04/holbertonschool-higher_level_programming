#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: head of a linked list
 *
 * Return: 0 if it is not a palindrome, 1 if it is
 */

int is_palindrome(listint_t **head)
{
	int i, cont = 0, med, aux[1024];

	if (!head)
	{
		return (0);
	}

	while (*head)
	{
		aux[cont] = (*head)->n;
		*head = (*head)->next;
		cont++;
	}
	med = cont / 2;
	for (i = 0; i < med; i++)
	{
		if (aux[i] != aux[cont - 1])
		{
			return (0);
		}
		cont--;
	}
	return (1);
}
