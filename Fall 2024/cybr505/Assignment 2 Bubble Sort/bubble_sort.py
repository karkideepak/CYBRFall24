"""
Bubble Sort
"""

# Using the function for this algorithim
def bubble_sort(unsorted_list):
    print('Input: ', unsorted_list)
    # Unsorted_list variable as the input
    indexing_length = len(unsorted_list) -1
    # Using indexing linked for the comparision
    # -1 because we cannot perfom comparision on the last element
    sorted = False
    # The sorted variable helps us to break the loop once all the elements are in order

    # Performing iteration with while loop
    while not sorted:
        # As long as the sorted is False, continue the loop
        sorted = True
        for i in range(0, indexing_length):
            if unsorted_list[i] > unsorted_list[i+1]:
                # Comparing the elements on left and right
                sorted = False
                # Flip the elements if they are in wrong order
                unsorted_list[i], unsorted_list[i+1] = unsorted_list[i+1], unsorted_list[i]

    # Return the new sorted list
    return unsorted_list

# Call the bubble sort function and pass the values
print('Output:',bubble_sort([2,4,5]))





