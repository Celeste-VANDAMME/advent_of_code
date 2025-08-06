// LIBRARIES:
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <time.h>
#include <math.h>


// STRUCTURES:
// todo: describe here
typedef struct Instruction {
    char direction ; // "L" or "R"
    unsigned int distance ;
    
} Instruction ;


// todo: describe here
typedef struct Position {
    int x  ;
    int y  ;
    char facingDirection ; // 'N', 'E', 'S', 'W'
    
} Position ;


/* FUNC: setDefaultPos
// TODO : complete the description here
A kind of constructor, in a sense. :)
*/
Position setDefaultPos( ) {
    
    // Initialization:
    Position pos ;
    
    // Values:
    pos.x                   = 0 ;
    pos.y                   = 0 ;
    pos.facingDirection     = 'N' ;
    
    return pos ;
}



/* FUNC: tokenCounter
// TODO : complete the description here

*/
int tokenCounter(const char* stringInput) {

    char scrutinizedLetter = stringInput[0];
    int tokenCounter = 1; // We suppose the input has at least one element
    int i = 0;

    while(scrutinizedLetter != '\0') {

        scrutinizedLetter = stringInput[i];

        if(scrutinizedLetter == ',') {
            tokenCounter++;
        }

        // End of loop
        i++;
    }

    return tokenCounter;
}



int main() {

    // --- MAIN VARIABLES:
    static bool debug_mode = true;
    int i;
    
    int tokenAmount = 0 ;
    unsigned int inputTokenLength ;
    unsigned int tokenDistanceCalculation ;
    
    
    // RNG
    srand(time(NULL));
    int randomValue ;


    /* --- TEXT CONVERSION:
    I convert the input file from raw text to usable list input.
    This is mandatory for now, as I'm using an online IDE
    (which doesn't allow to upload files in a workspace)...
    LINK:
    https://www.online-cpp.com/
    */

    char* rawInput = "L4, L3, R1, L4, R2, R2, L1, L2, R1, R1, L3, R5, L2, R5, L4, L3, R2, R2, L5, L1, R4, L1, R3, L3, R5, R2, L5, R2, R1, R1, L5, R1, L3, L2, L5, R4, R4, L2, L1, L1, R1, R1, L185, R4, L1, L1, R5, R1, L1, L3, L2, L1, R2, R2, R2, L1, L1, R4, R5, R53, L1, R1, R78, R3, R4, L1, R5, L1, L4, R3, R3, L3, L3, R191, R4, R1, L4, L1, R3, L1, L2, R3, R2, R4, R5, R5, L3, L5, R2, R3, L1, L1, L3, R1, R4, R1, R3, R4, R4, R4, R5, R2, L5, R1, R2, R5, L3, L4, R1, L5, R1, L4, L3, R5, R5, L3, L4, L4, R2, R2, L5, R3, R1, R2, R5, L5, L3, R4, L5, R5, L3, R1, L1, R4, R4, L3, R2, R5, R1, R2, L1, R4, R1, L3, L3, L5, R2, R5, L1, L4, R3, R3, L3, R2, L5, R1, R3, L3, R2, L1, R4, R3, L4, R5, L2, L2, R5, R1, R2, L4, L4, L5, R3, L4";
    size_t inputLength = strlen(rawInput);

    if(debug_mode) {
        printf("\nSize = %zu\n", inputLength);
        printf("\nInput:\n\"%s\"", rawInput);
    }

    // Transforming the raw input into proper data
    char* rawInputBuffer = malloc(sizeof(char) * (inputLength+1));
    strcpy(rawInputBuffer, rawInput);
    
    // Getting the amount of space we need in the input array:
    tokenAmount = tokenCounter( rawInputBuffer ) ;
    if( debug_mode ) { printf("\ntokenAmount = %d\n", tokenAmount ) ; }
    
    
    // Then, setting up the space for it:
    Instruction* input = malloc(sizeof(Instruction*) * tokenAmount);


    static int loopCounter = 0;


    // Tokenizing the input here:
    char *inputToken = strtok(rawInputBuffer, ", ");

    while(inputToken != NULL) {
        
        // 0. Analyzing the inputToken:
        inputTokenLength = strlen(inputToken);
        
        // 1. Direction
        input[loopCounter].direction = inputToken[0] ;
        
        // 2. Distance
        tokenDistanceCalculation = 0;
        
        for(i=1; i<inputTokenLength; i++){
            tokenDistanceCalculation = tokenDistanceCalculation*10 + (inputToken[i] - '0')  ;
        }
        input[loopCounter].distance = tokenDistanceCalculation;
        
        // 3. Getting ready for next loop
        inputToken = strtok(NULL, ", "); // We keep tokenizing the same STRING, with the "NULL" variable.
        loopCounter++;
    }

    // Displaying the result of a random variable:
    if(debug_mode){
        randomValue = rand() % (loopCounter+1) ;
        
        printf( "\n\n*- %dst input:\n", randomValue+1);
        printf( "   direction = %c\n", input[randomValue].direction ) ;
        printf( "   distance = %u\n\n", input[randomValue].distance ) ;
    }
    
    
    
    /* --- DATA INTERPRETATION:
    We set our default position to North (N), and read the input step by step
    while turning Left (L) or Right (R) and going forward to a set distance.
    
    Then, it's only a matter of calculing the taxicab distance while being by
    default on (0,0)... thus adding the two x+y coordinates.
    */
    
    Position gridPosition = setDefaultPos() ;
    const int orderLength = loopCounter ;
    
    // Direction:
    int directionMapping[256] = {O} ; // We set a table large enough that contains all ASCII usual letters.
    directionMapping['N'] = 1 ;
    directionMapping['E'] = 2 ;
    directionMapping['S'] = 3 ;
    directionMapping['W'] = 4 ;
    
    
    
    for(i=0; i<orderLength; i++){
        // 1. Pole facing update
        
        
        // 2. Distance calculation
    }
    
    // 3. Overall distance calculation (from the default position)
    

    return 0;


}
