#include <stdio.h>

// I'm assuming each print output except 'CodeTest'
// is in it's own line

#define PRINTNEWLINE
void codetest(void) {
    for (int i = 1; i<=100; i++) {

        if (i%3 == 0) printf("Code");            
        if (i%5 == 0) printf("Test");
        if (i%3 !=0 && i%5 !=0)
            printf("%d", i);

        
        #ifdef PRINTNEWLINE
        printf("\n");   
        #endif                 
    }
}

int main(void) {
    codetest();
    return 0;
}
