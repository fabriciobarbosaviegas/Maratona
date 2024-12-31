#include <stdio.h>
#include <stdlib.h>

struct treeNode
{
    int key;
    struct treeNode *left, *right;
};

struct treeNode* newNodeCreate(int value)
{
    struct treeNode* temp = (struct treeNode*)malloc(sizeof(struct treeNode));
    temp->key = value;
    temp->left = temp->right = NULL;
    return temp;
}

struct treeNode*
insertNode(struct treeNode* node, int value)
{
    if (node == NULL) {
        return newNodeCreate(value);
    }
    if (value < node->key) {
        node->left = insertNode(node->left, value);
    }
    else if (value > node->key) {
        node->right = insertNode(node->right, value);
    }
    return node;
}

int main(){
    int C, N, i;

    scanf("%d", &C);

    while(C--){
        scanf("%d", &N);
        int keys[N];

        for(i = 0; i < N; i++){
            scanf("%d", &keys[i]);
        }
        
        for (int i = 0; i < N; i++) {
            printf("%d ", keys[i]);
        }
        printf("\n");
    }

    return 0;
}