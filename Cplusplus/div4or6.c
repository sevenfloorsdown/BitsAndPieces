// Assumptions:
//  * always y >= x 
//  * garbage collection is outside of function
//  * UINT_MAX is defined or limits.h is included
//  * UINT_MAX is used as a marker as end of array
//  * DIV4MASK is defined as 0x3
unsigned int* div4or6( unsigned int x, unsigned int y) {
    unsigned int w, z, j, i = 0;
    unsigned int *set;
    
    set = new unsigned int [y-x];
    while (i < y-x) set[i++] = UINT_MAX;
    
    if (x%2 == 1) x++; // no odd numbers for us
    i = 0;
    while (x < y) {
       
        // divisibility by 4
        if ((x & DIV4MASK) == 0 ) { 
            set[i++] = x;
        // this 'else' is to avoid duplicates  
        } else { 
            // divisibility by 6
            w = x;
            // add all the hexits and see if that's divisible by 3
            // since all the numbers we're checking now are all even anyway
            do {
                z = j = 0;
                while (j < 16) {
                    z += (w >> j) & 0xF;
                    j += 4;
                }
                w = z;
                // if more than 1 hexit, do it again
                // FYI, I don't like recursing 
          } while (w > 0xF);  
           
          if (z == 0 || z == 3 || z == 6 || z == 9 || z == 0xC || z == 0xF) {
             set[i++] = x;           
          }    
        }
        // everything will be even numbers at this point
        x += 2;   
    } 	
   return set;
}
