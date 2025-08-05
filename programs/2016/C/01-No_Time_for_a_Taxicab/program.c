// LIBRARIES:
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>


int main() {

    // --- MAIN VARIABLES:
    static bool debug_mode = false;
    int i;

    // --- TEXT CONVERSION:
    // I convert the input file from raw text to usable list input.
    // This is mandatory for now, as I'm using an online IDE 
    // (which doesn't allow to upload files in a workspace)...

    char* rawInput = "L4, L3, R1, L4, R2, R2, L1, L2, R1, R1, L3, R5, L2, R5, L4, L3, R2, R2, L5, L1, R4, L1, R3, L3, R5, R2, L5, R2, R1, R1, L5, R1, L3, L2, L5, R4, R4, L2, L1, L1, R1, R1, L185, R4, L1, L1, R5, R1, L1, L3, L2, L1, R2, R2, R2, L1, L1, R4, R5, R53, L1, R1, R78, R3, R4, L1, R5, L1, L4, R3, R3, L3, L3, R191, R4, R1, L4, L1, R3, L1, L2, R3, R2, R4, R5, R5, L3, L5, R2, R3, L1, L1, L3, R1, R4, R1, R3, R4, R4, R4, R5, R2, L5, R1, R2, R5, L3, L4, R1, L5, R1, L4, L3, R5, R5, L3, L4, L4, R2, R2, L5, R3, R1, R2, R5, L5, L3, R4, L5, R5, L3, R1, L1, R4, R4, L3, R2, R5, R1, R2, L1, R4, R1, L3, L3, L5, R2, R5, L1, L4, R3, R3, L3, R2, L5, R1, R3, L3, R2, L1, R4, R3, L4, R5, L2, L2, R5, R1, R2, L4, L4, L5, R3, L4";
    size_t inputLength = strlen(rawInput);

    if(debug_mode) {
        printf("\nSize = %zu\n", inputLength);
        printf("\nInput:\n\"%s\"", rawInput);
    }

    // Transforming the raw input into proper data
    char* rawInputBuffer = malloc( sizeof(char) * (inputLength+1) );
    strcpy(rawInputBuffer, rawInput) ;
    
    char** input = malloc( sizeof(char*) * inputLength ) ;
    static int loopCounter = 0 ;
    
    
    // Tokenizing the input here:
    char *inputToken = strtok(rawInput, ", ");
    
    while( inputToken != NULL ) {
        input[loopCounter] = inputToken ;
        inputToken = strtok(NULL, ", ") ; // We keep tokenizing the same STRING, with the "NULL" variable.
        
        loopCounter++ ;
    }
    





    return 0;


}
