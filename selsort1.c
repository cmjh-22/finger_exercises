/* The selection sort algorithm sorts an array by repeatedly finding the minimum element
 (considering ascending order) from unsorted part and putting it at the beginning.
 The algorithm maintains two subarrays in a given array.
The subarray which is already sorted.
Remaining subarray which is unsorted */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

int to_sort[10] = {4711, 8, 2, 33, 5, 23, 42, 78, 123, 2398};

void pretty_printer(int *to_print);

int main(int argc, char **argv)
{
    int asc = 0;

    if (argc != 2)
    {
        printf("Usage: ./selsort [asc|dsc]\n");
        return 1;
    }
    // TODO asc, dsc
    if (strcmp(argv[1], "asc") == 0)
    {
        asc = 1;
    }
    else if (strcmp(argv[1], "dsc") == 0)
    {
        asc = 0;
    }
     else
    {
        printf("Usage: ./selSort [asc|dsc] to_sort\n");
        return 1;
    }
    //helpers
    int limit = sizeof(to_sort)/sizeof(to_sort[0]);
    int max;
    int maxIndex;
    //why this way? :) because it will look through the array from the end to the beginning??
    for (int i = limit - 1; i > 0; i--)
    {
        //TODO
        //find the maximum element in the array
        maxIndex = i;
        //check if I have to sort asc or desc
        for (int j = 0; j < limit; j++){
            if(asc){ // anything that is NOT zero is true
                   //asc is true then:
                if (to_sort[j]>to_sort[maxIndex]){
                    maxIndex = j;
                }

                int temp = to_sort[j];
                to_sort[j] = to_sort[maxIndex];
                to_sort[maxIndex] = temp;

            }
            else{
            //asc is NOT true then we sort descending order
                if (to_sort[j]< to_sort[maxIndex]){
                    maxIndex = j;
                }
                int temp = to_sort[j];
                to_sort[j] = to_sort[maxIndex];
                to_sort[maxIndex] = temp;
          }
        }
    }

    pretty_printer(to_sort);
    return 0;
}

void pretty_printer(int *to_print){
    printf("[");
    for (int i = 0, j = sizeof(to_sort)/sizeof(to_sort[0]); i < j; i++)
    {
        if (i == j - 1)
        {
            printf("%i", to_print[i]);
            break;
        }
        printf("%i, ", to_print[i]);
    }
    printf("]\n");
}
