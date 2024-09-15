#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define MOD 998244353

typedef struct {
    int top;
    int capacity;
    char *array;
} Stack;

void initStack(Stack *stack, int capacity) {
    stack->array = malloc(capacity * sizeof(char));
    stack->top = -1;
    stack->capacity = capacity;
}

int isFull(Stack *stack) {
    return stack->top == stack->capacity - 1;
}

int isEmpty(Stack *stack) {
    return stack->top == -1;
}

void push(Stack *stack, char item) {
    if (isFull(stack)) {
        stack->capacity *= 2;
        stack->array = realloc(stack->array, stack->capacity * sizeof(char));
    }
    stack->array[++stack->top] = item;
}

char pop(Stack *stack) {
    if (isEmpty(stack)) {
        fprintf(stderr, "Stack underflow\n");
        exit(EXIT_FAILURE);
    }
    return stack->array[stack->top--];
}

int isValid(int N, char *S) {
    if (N % 2 != 0) {
        return 0;
    }

    Stack stack;
    initStack(&stack, N / 2);

    for (int i = 0; i < N; i++) {
        if (S[i] == '(') {
            push(&stack, S[i]);
        } else {
            if (isEmpty(&stack)) {
                return 0;
            }
            pop(&stack);
        }
    }

    return isEmpty(&stack);
}

int countSub(char **parentheses_list, int size, char *substring) {
    int count = 0;
    for (int i = 0; i < size; i++) {
        count += strstr(parentheses_list[i], substring) - parentheses_list[i];
    }
    return count;
}

int *geraParentese(int n) {
    int *result = malloc((n * (n + 1) / 2) * sizeof(int));
    int index = 0;

    void rastreio(char *s, int left, int right) {
        if (strlen(s) == n) {
            if (left == right) {
                result[index++] = strdup(s);
            }
            return;
        }
        if (left < n / 2) {
            rastreio(strcat(s, "(", n + 1), left + 1, right);
        }
        if (right < left) {
            rastreio(strcat(s, ")", n + 1), left, right + 1);
        }
    }

    rastreio("", 0, 0);
    return result;
}

int main() {
    int N;
    scanf("%d", &N);

    char S[100001];
    scanf("%s", S);

    int *parenteses_list = geraParentese(N);
    int size = (N * (N + 1) / 2);
    int total = countSub(parenteses_list, size, S);
    printf("%d\n", total % MOD);

    return 0;
}