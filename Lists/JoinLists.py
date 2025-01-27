# Join Two Lists.
# One of the easiest ways are by using the + operator.
# Join two list :
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3) # ['a', 'b', 'c', 1, 2, 3].

# Append list2 into list1 :
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
for x in list2:
  list1.append(x)
print(list1) # ['a', 'b', 'c', 1, 2, 3].

# Or you can use the extend() method, where the purpose is to add elements from one list to another list.
# Use the extend() method to add list2 at the end of list1 :
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1) # ['a', 'b', 'c', 1, 2, 3].