// Implements a dictionary's functionality

#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#include "dictionary.h"

// Represents number of children for each node in a trie
#define N 27

// Represents a node in a trie
typedef struct node
{
    bool is_word;
    struct node *children[N];
}
node;

//prototypes
void unloadH(node *ptr);
unsigned int sizeH(node *ptr);
node *getNode(void);

// Represents a trie
node *root;


//helper methods
node *getNode(void)
{
    node *ptr = NULL;
    ptr = calloc(1, sizeof(node));

    if (ptr)
    {
        int i;

        ptr->is_word = false;

        for (i = 0; i < N; i++)
            ptr->children[i] = NULL;
    }

    return ptr;
}

// Loads dictionary into memory, returning true if successful else false
bool load(const char *dictionary)
{
    // Initialize trie
    root = getNode();

    // Open dictionary
    FILE *file = fopen(dictionary, "r");
    if (file == NULL)
    {
        unload();
        return false;
    }
    //word counter;
    int count = 0;
    // Buffer for a word
    char word[LENGTH + 1];
    // Insert chars into trie
    for (char c = fgetc(file); c != EOF; c = fgetc(file))
    {
        c = tolower(c);

        node *ptr = root;

        if(ptr == NULL) printf("SEG FAULT COMING!\n");

        if (c == '\n' && ptr!=root)
        {
            count++;
            ptr->is_word = true;
            ptr = root;
        }
        else{
            if(!isalpha(c))
            {
                continue;
            }
            int m = c - 'a';
            node* current = ptr->children[m];
            if (current == NULL)
            {
                ptr->children[m] = getNode();
                ptr = ptr->children[m];
            }
            else
            {
                ptr = current;
            }
        }
    }

    printf("COUNTER IN LOAD %i\n" , count);
    // Close dictionary
    fclose(file);

    // Indicate success
    return true;
}

// Returns number of words in dictionary if loaded else 0 if not yet loaded
unsigned int size(void)
{
    node *ptr = root;
    unsigned int count = sizeH(ptr);
    printf("COUNTER IN SIZE %d\n" , count);
    return 0;
}

unsigned int sizeH(node *ptrr){
    node *ptr = root;
    if(ptr==NULL){
        printf("NULL ptr\n");
        return 99999;
    }
    if(ptr->is_word)
    {
        return 1;
    }
    else
    {
        for(int x = 0; x < N; x++){
            return 0 + sizeH(ptr->children[x]);

        }
    }
    return 0;
}

// Returns true if word is in dictionary else false
bool check(const char *word)
{
    node *ptr = root;
    for(int i = 0; i < strlen(word); i++)
    {
        if(!isalpha(word[i]))
            {
                continue;
            }
        char c = tolower(word[i]);
        int m = c - 'a';
        if(ptr->children[m]==NULL){
            return false;
        }
        else{
            ptr = ptr->children[m];
        }
    }
    if(ptr->is_word == true)
    {
        return true;
    }
    else
    {
        return false;
    }
}

// Unloads dictionary from memory, returning true if successful else false
void unloadH(node* ptr)
{
    for (int i = 0; i < 27; i++)
    {
        if(ptr->children[i] != NULL)
        {
            unloadH(ptr->children[i]);
        }
    }
    free(ptr);
}

bool unload(void)
{
    if(root != NULL)
    {
        unloadH(root);
        return true;
    }
    else
    {
        return false;
    }
}


