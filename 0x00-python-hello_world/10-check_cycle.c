#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: linked list to check
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *aux1, *aux2;

	if (!list)
		return (0);

	aux1 = list;
	aux2 = list;

	while (aux1 && aux2 && aux1->next && aux2->next)
	{
		aux1 = aux1->next;
		aux2 = aux2->next->next;

		if (aux1 == aux2)
			return (1);
	}

	return (0);
}
