#include <stdio.h>
#include <stdlib.h>

/* Definition of singly linked list node */
typedef struct listint_s {
    int n;
    struct listint_s *next;
} listint_t;

/* Function to check if a singly linked list is a palindrome */
int is_palindrome(listint_t **head) {
    if (*head == NULL || (*head)->next == NULL)
        return 1;

    listint_t *sl = *head;
    listint_t *far = *head;
    listint_t *prev_sl = NULL;
    listint_t *half = NULL;
    int is_palindrome = 1;

    while (far != NULL && far->next != NULL) {
        far = far->next->next;
        prev_sl = sl;
        sl = sl->next;
    }

    /* Odd number of elements, skip the middle node */
    if (far != NULL) {
        sl = sl->next;
    }

    half = sl;
    prev_sl->next = NULL;

    /* Reverse the second half of the linked list */
    listint_t *crrt = half;
    listint_t *prev = NULL;
    listint_t *next = NULL;

    while (crrt != NULL) {
        next = crrt->next;
        crrt->next = prev;
        prev = crrt;
        crrt = next;
    }
    half = prev;

    /* Compare the first half and reversed second half */
    listint_t *tmp1 = *head;
    listint_t *tmp2 = half;

    while (tmp1 != NULL && tmp2 != NULL) {
        if (tmp1->n != tmp2->n) {
            is_palindrome = 0;
            break;
        }
        tmp1 = tmp1->next;
        tmp2 = tmp2->next;
    }

    /* Restore the linked list to its original state */
    crrt = half;
    prev = NULL;
    while (crrt != NULL) {
        next = crrt->next;
        crrt->next = prev;
        prev = crrt;
        crrt = next;
    }
    half = prev;
    prev_sl->next = half;

    return is_palindrome;
}

/* Example usage */
int main(void) {
    listint_t *head = NULL;
    
    /* Create a sample linked list (1 -> 2 -> 2 -> 1) */
    listint_t *node1 = malloc(sizeof(listint_t));
    listint_t *node2 = malloc(sizeof(listint_t));
    listint_t *node3 = malloc(sizeof(listint_t));
    listint_t *node4 = malloc(sizeof(listint_t));
    
    node1->n = 1; node1->next = node2;
    node2->n = 2; node2->next = node3;
    node3->n = 2; node3->next = node4;
    node4->n = 1; node4->next = NULL;
    
    head = node1;

    /* Call the is_palindrome function and print the result */
    int result = is_palindrome(&head);
    printf("Is the linked list a palindrome? %s\n", result ? "Yes" : "No");

    /* Free memory */
    while (head != NULL) {
        listint_t *temp = head;
        head = head->next;
        free(temp);
    }

    return 0;
}
