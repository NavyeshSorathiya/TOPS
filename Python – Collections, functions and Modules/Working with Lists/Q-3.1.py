# Write a Python program to sort a list using both sort() and sorted().


# Sort list element using sort() function it is not return anything that is modifies the original list
my_list = [1,3,2,5,1,3,7,8,1,2,4,6,3,7,8]
print(my_list)

my_list.sort()
print(my_list)



# Sort list element using sorted() metho it is return a new sorted list
mylist = [1,3,8,5,1,6,4,2,3,1,5,6,7,5,1,3]
print(mylist)

sorted_list = sorted(mylist)
print(sorted_list)