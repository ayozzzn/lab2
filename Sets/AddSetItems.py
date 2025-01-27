# Add Items.
# To add one item to a set use the add() method.
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset) # {'cherry', 'apple', 'orange', 'banana'}.

# Add Sets.
# To add items from another set into the current set, use the update() method.
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset) # {'banana', 'mango', 'apple', 'pineapple', 'papaya', 'cherry'}.

# Add Any Iterable.
# The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset) # {'apple', 'cherry', 'banana', 'kiwi', 'orange'}.