#include "lists.h"

/**
 * is_palindrome - Function that checks if a singly linked list is a palindrome
 * @head: Doubly pointer to linked list.
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome.
 */
int is_palindrome(listint_t **head)
{
	char buffer[100000];
	listint_t *h = *head;
	int count_1 = 0;
	int count_2 = 0;

	if (*head == NULL)
		return (1);
	while (h != NULL)
	{
		buffer[count_1] = h->n;
		count_1++;
		h = h->next;
	}

	count_1--;
	while (count_2 < count_1)
	{
		if (buffer[count_2] != buffer[count_1])
			return (0);

		count_2++;
		count_1--;
	}

	return (1);
}
