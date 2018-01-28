"""
MergeSort
Python implementation of a MergeSort
by Dylan Hamer
"""

from Data import generateSample  # Generate large sample datasets on the fly for testing

arraySize = 10  # Size of sample array
arrayMax = 100  # Maximum random value permittable in array

"""Main mergesort function"""
def mergeSort(array):
    if len(array) == 1:  # If the array has been fully sorted,
        return(array)  # Return it so we don't get stuck in an infinite loop
    
    # First we need to split the array into two halves,
    arrayMiddle = int(round(len(array)/2))  # Middle index of array
    arrayLeft = array[:arrayMiddle]  # Left half of array
    arrayRight = array[arrayMiddle:]  # Right half of array

    arrayLeft = mergeSort(arrayLeft)  # We need to split the left half of the array again
    arrayRight = mergeSort(arrayRight)  # Same for the right

    return merge(arrayLeft, arrayRight)  # Merge the arrays

"""Merge two arrays"""
def merge(firstArray, secondArray):
    temporaryArray = []  # Temporary array to sort into
    while firstArray and secondArray:  # Loop until both arrays are empty
        if firstArray[0] > secondArray[0]:  # If the the first element of the first array is greater than the first element of the second array,
            temporaryArray.append(secondArray.pop(0))  # Add the first element of the second array to the end of the temporary array and remove it from the second array
        else:  # Otherwise, 
            temporaryArray.append(firstArray.pop(0))   # Do the same but for the second array
    while firstArray:  # Loop until first array is empty 
        temporaryArray.append(firstArray.pop(0))  # Add the first element of the first array to the end of the temporary array
    while secondArray:  # Loop until second array is empty
        temporaryArray.append(secondArray.pop(0))
    return temporaryArray

"""Main function"""
def main():
    sampleDataset = generateSample(size=arraySize, maximumValue=arrayMax)
    sortedDataset = mergeSort(sampleDataset)
    print("Original: {}".format(sampleDataset))
    print("Sorted: {}".format(sortedDataset))

if __name__ == "__main__":
    main()

