#include "lists.h"

/**
 *check_cycle - valide if the list have a cicle
 *@list: Linked list.
 *Return: Always 0 or 1.
 */
int check_cycle(listint_t *list)
{
	listint_t *tortuga = NULL;
	listint_t *liebre = NULL;

	if (list == NULL || list->next == NULL)
		return (0);
	tortuga = list->next;
	liebre = list->next->next;

	while (liebre != NULL && tortuga != NULL && liebre->next != NULL)
	{
		if (tortuga == liebre)
			return (1);
		tortuga = tortuga->next;
		liebre = liebre->next->next;
	}
	return (0);
}
