#! /usr/bin/env pyth

def takepivot(left, right):
    # avoid overflow if either has a value near the largest value
    return left + (right - left)/2

def partition(inlist, left, right):
    pivot = inlist[takepivot(left, right)]
    
    while left < right:
        while inlist[left]  < pivot: left += 1
        while inlist[right] > pivot: right -= 1
        if inlist[left] == inlist[right]: left += 1
        elif left < right:
            tmp = inlist[left]
            inlist[left] = inlist[right]
            inlist[right] = tmp
    return right

def quicksort(inlist, left, right):
    if left < right:
        x = partition(inlist, left, right)
        quicksort(inlist, left, x-1)
        quicksort(inlist, x+1, right)

def main():
    inlist1 = [3, 11, 9, 5, 7, 1, 15, 21, 17, 19]
    print "Inlist 1:"
    quicksort(inlist1, 0, 7)
    print inlist1
    inlist2 = [23, 29 ,25, 31, 27, 37, 33, 35, 41, 39]
    print "Inlist 2:"
    quicksort(inlist2, 0, len(inlist2)-1)
    print inlist2
    
    
    
if __name__ == "__main__":
    main()
