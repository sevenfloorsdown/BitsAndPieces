#include <iostream>
using namespace std;

const int INPUT_SIZE = 10;

int takepivot(int p, int r) {
    return p + (r-p)/2; 
}

// partition and swapping
int partition(int* input, int p, int r) {
    int x = takepivot(p, r);
    int pivot = input[x];
    
    while (p < r) {
        while (input[p] < pivot) p++;
        while (input[r] > pivot) r--;
        
        if (input[p] == input[r]) p++;
        else if (p < r) {
            // this is also the case where input[p] > input[r]
            int tmp = input[p];
            input[p] = input[r];
            input[r] = tmp;
        }
    }
    return r;
}

// recursive quicksort
void quicksort(int *input, int p, int r) {
    if (p < r) {
        int j = partition(input, p, r);
        quicksort(input, p,   j-1);
        quicksort(input, j+1, r);
    }
}


void print(int *input) {
    for (int i = 0; i < INPUT_SIZE; i++) cout << input[i] << " ";
    cout << endl;
}


int main() {
    int input[INPUT_SIZE] = { 3, 11, 9, 5, 7, 1, 15, 21, 17, 19};
    cout << "Input: ";
    print(input);
    quicksort(input, 0, 9);
    cout << "Output: ";
    print(input);
    
    int input2[INPUT_SIZE] = { 23, 29 ,25, 31, 27, 37, 33, 35, 41, 39};
    cout << "Input: ";
    print(input2);
    quicksort(input2, 0, 9);
    cout << "Output: ";
    print(input2);
       
    return 0;
}
