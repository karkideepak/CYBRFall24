'''
3.	While Loop with Condition:
o	Write a Python program that uses a while loop to sum the numbers from 1 to 100. The loop should stop when the sum exceeds 500, and the program should print the sum at that point.

'''
#Initialize variables
number = 1
sum_track = 0
#using while loop
while sum_track + number <= 500:
    #sum_track = sum_track + number
    sum_track += number
    number += 1
#print the sum
print("The sum of numbers from 1 to 100 that does not exeed 500 is: ",sum_track)
print('* * '*20)



'''
4.	Nested Loops and Matrix Printing:
After printing the matrix, use a for loop to sum all the elements in the matrix and print the result.

'''
# Create a 3x3 matrix (a list of lists) containing integers from 1 to 9
total_sum = 0
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]
# printing matrix directly
print(matrix)
# nested for loop
# traversing the list
for row in matrix:
    for element in row:
        print(element, end=' ') #seperate by space
    # print new line after each row
    print()

for row in matrix:
    for element in row:
        total_sum += element
print("Total sum is: ", total_sum)
print('* * '*20)