#include "lists.h"
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *current;
	listint_t *aux;

	current = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (*head == NULL)
		*head = new;
	else
	{
		while (current->next != NULL)
		{
			if (current->next->n <= number)
				current = current->next;
			else
			{
				aux = current;
				current = current->next;
				new->next = current;
				aux->next = new;
				return(new);
			}
		}
	}
	return (new);
}
