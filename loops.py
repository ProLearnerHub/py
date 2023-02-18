# loops are used to iterate over a list of data.
# a list is a collection of items, for example, students in a class.
# using this example, we might have a looping function that calculates the fee balances for each student, or we want to collectively update some information about them
# there are multiple methods of writing loops, but the most efficient and also popular method uses the keyword "for", followed by the criteria, for example "in" "of" etc.
# the concept is to iterate over individuals "in" a list, or individuals "of" a list.

# syntax is like

# for item starts_at  1 ends_at 10
# do something 10 times

# Or
#while item doesn't_meet_condition
#do something and modify value of item

For example:

list =["item_one", "item_two", "item_three", "item_four"]
for item in list:
    print(item) #do something with this item, repeats 4 times

# or

for item in range (len(list)):
    print(item) # or whatever you want 4 times

#or
while item < 2:
    print(item)
    item = item - 1 # or whatever case you want as your modifier

