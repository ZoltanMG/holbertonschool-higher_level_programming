#include "lists.h"

/**
 * is_palindrome - Function that checks if a singly linked list is a palindrome
 * @head: Doubly pointer to linked list.
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome.
 */
int is_palindrome(listint_t **head)
{
	listint_t *h = *head;
	listint_t *aux = *head;
	int count = 0, count_2 = 0, count_3 = 0;

	if (*head == NULL)
		return (1);
	while (h->next)
	{
		count++;
		h = h->next;
	}

	h = *head;
	while (count_2 < count)
	{
		while (count_3 != count)
		{
			aux = aux->next;
			count_3++;
		}
		if (aux->n != h->n)
			return (0);
		count--;
		count_2++;
		count_3 = 0;
		aux = *head;
		h = h->next;
	}
	return (1);
}
