# Assignment 1
'''
1.	List Manipulation:
'''
# Create a list of numbers from 1 to 10.

create_list = [1,2,3,4,5,6,7,8,9,10]
print("Original:", create_list)
#Append the number 11 to the list.
create_list.append(11)
#Insert the number 0 at the beginning of the list.
create_list.insert(0,0)
# Remove the number 5 from the list.
create_list.remove(5)
#Sort the list in descending order.
#default is reverse=false
create_list.sort(reverse=True)
#Print the final list.
print("Descending:", create_list)
print('* * '*20)

'''
2.	Range and Loops:
'''
even_num=[]
#between 1 and 20, inclusive
for i in range(21):
    #Use an if statement
    if i %2 ==0:
        even_num.append(i)
#print the even numbers
print("Even numbers:", even_num)
print('* * '*20)