"""
Bubble Sort Algorithm for Sorting Book Prices
"""

# Define the bubble sort function
def bubble_sort(book_prices):
    print('Input (Book Prices):', book_prices)
    # book_prices is the list of book prices that needs to be sorted
    indexing_length = len(book_prices) - 1
    # Length minus 1 because comparisons stop before the last element

    sorted = False
    # sorted is used to break the loop once the list is fully sorted

    # Perform sorting using a while loop
    while not sorted:
        # Continue looping as long as the list is not fully sorted
        sorted = True
        for i in range(0, indexing_length):
            if book_prices[i] > book_prices[i + 1]:
                # Compare adjacent elements in the list
                sorted = False
                # Swap if the current price is greater than the next price
                book_prices[i], book_prices[i + 1] = book_prices[i + 1], book_prices[i]

    # Return the sorted list of book prices
    return book_prices

# Call the bubble_sort function with a list of book prices
book_prices = [50.15, 12.49, 66.09, 7.00, 90.99]
sorted_prices = bubble_sort(book_prices)

# Adding $ symbol in the output
print('Output (Sorted Book Prices):', ['${:.2f}'.format(price) for price in sorted_prices])
