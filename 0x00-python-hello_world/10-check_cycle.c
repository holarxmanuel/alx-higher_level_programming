#include "lists.h"

/**
 * check_cycle - check for loop in LL
 * @list: head of linked list
 *
 * Description - check for loops in LL
 * Return: 1 if cycled, 0 if not
 */

int check_cycle(listint_t *list)
{
	listint_t *stat, *act;

	if (!list)
	{
		return (0);
	}
	stat = list;
	act = list->next;
	while (act && stat && act->next)
	{
		if (stat == act)
		{
			return (1);
		}
		stat = stat->next;
		act = act->next->next;
	}
	return (0);
}
