// DESIGNED FOR C23.
// @celeste_vandamme (github)

/// --- LIBRARIES
#include <stdio.h>
#include <stdlib.h>


/// --- STRUCTURES
typedef struct Instruction {
    char direction;      // L or R
    unsigned short int degree;    // Amount of rotation/click in said direction
} Instruction;


/// --- FUNCTIONS PROTOTYPES
int int_wrapper(const int value, const int min, const int max) ;
void password_0x434C49434B(int *password, const int dial_pos, const Instruction line_instruction) ;

/// --- MAIN
int main(void)
{
    // --- 1. Major variables
    const bool debug_mode = false ;
    constexpr int initial_dial_pos = 50 ;
    const char file_directory[100] = "input.txt" ;
    const int line_max_size = 100 ;

    // --- 2. Variables
    int final_password = 0 ;
    int final_password_0x434C49434B = 0 ;
    int dial_pos = initial_dial_pos ;

    int i = 0;
    Instruction line_instruction ;

    FILE *input_file = NULL ;
    char line_input[line_max_size] ;


    // --- 2. Process
    input_file = fopen(file_directory, "r" );

    if (input_file == NULL)
    {
        printf(">> File not found/an error happened.\n"
               "Please make sure the file_directory variable is set correctly.\n\n"
               "Directory: '%s'\n", file_directory ) ;

        return EXIT_FAILURE ;
    }

    else
    {
        /// --- 2.a. Reading the input.txt data
        while ( fgets(line_input, line_max_size, input_file) != NULL )
        {

            if (debug_mode) {
                printf("\n>>> %s", line_input ) ;
            }

            // Direction: 'L' or 'R'
            line_instruction.direction = line_input[0] ;

            // Degree of rotation?
            line_instruction.degree = 0 ;

            for (i=1; line_input[i] != '\n'; i++)
            {
                // Make space for the new value -&- Convert '4' to 4 (char > int)
                line_instruction.degree = (line_instruction.degree * 10) + (line_input[i] - '0') ;
            }

            if (debug_mode)
            {
                printf("direction = '%c' / value = '%i'\n", line_instruction.direction, line_instruction.degree) ;
            }

            /// 2. d. "Real" password with the method: "0x434C49434B"
            password_0x434C49434B(
                    &final_password_0x434C49434B,
                    dial_pos,
                    line_instruction
                    ) ;

            if (debug_mode)
            {
                printf("Password v2 end: %i\n", final_password_0x434C49434B ) ;
            }

            /// --- 2.b. Applying the instruction
            // Applying the degree to the dial...
            dial_pos += (1 - 2 * (line_instruction.direction == 'L') ) * line_instruction.degree ;

            if (debug_mode)
            {
                printf("Dial unwrap = %i\n", dial_pos) ;
            }

            // Then restraining the value between [0;99].
            dial_pos = int_wrapper(dial_pos, 0, 99) ;

            if (debug_mode)
            {
                printf("dial = %i\n", dial_pos ) ;
            }

            /// 2. c. "Real" password here!
            /// When the dial is = 0°.
            if ( dial_pos == 0 )
            {
                final_password++ ;
            }

            if ( debug_mode )
            {
                printf("final_password = %i\n", final_password ) ;
            }

        }

    }

    // --- 3. Result display
    printf("Dial position as told on the instruction:\n"
           "DIAL = %i\n\n", dial_pos) ;

    printf("Secret password:\n> '%i'\n\n", final_password);

    printf("Secret password (method '0x434C49434B'):\n> '%i'\n\n", final_password_0x434C49434B);

    // --- 4. End of program
    return 0;
}

/// --- FUNCTIONS

int int_wrapper(const int value, const int min, const int max)
{
    const int range = max - min + 1;
    return ((((value - min) % range) + range) % range) + min ;
}

void password_0x434C49434B(int *password, int dial_pos, const Instruction line_instruction)
{
    //
    const bool wasAtZero = (dial_pos == 0) ;

    // Applying the instruction but not wrapping it directly.
    dial_pos += (1 - 2 * (line_instruction.direction == 'L') ) * line_instruction.degree ;


    // We add ONE CLICK, then we check whether we still go above 100? (+1 click each time)
    if (dial_pos <= 0 )
    {
        if ( !wasAtZero )
        {
            *password += 1 ;
        }

        dial_pos = abs(dial_pos) ;
    }

    *password += dial_pos / 100 ;
}
