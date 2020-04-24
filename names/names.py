import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)


class BinarySearchTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Recursive insert implementation
    # does not return anything when executed
    def insert(self, value):
        # self.left and/or self.right need to be valid nodes i.e. need to exist
        # for us to call 'insert' on them
        if value < self.value:
            # check is self.left is a valid node
            if self.left:
                self.left.insert(value)
            # the left side is empty
            else:
                # we've found a valid parking spot
                self.left = BinarySearchTreeNode(value)
        else:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BinarySearchTreeNode(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # check if node contains value
        if self.value == target:
            return True
        elif self.value < target:
            if self.right:
                return self.right.contains(target)
            else:
                return False
        else:
            if self.left:
                return self.left.contains(target)
            else:
                return False


# create temp var
bst = BinarySearchTreeNode('')
# loop through names_1
for name_1 in names_1:
    # invoke insert function to create a Binary Search Tree of names_1
    bst.insert(name_1)
# loop through names_2
for name_2 in names_2:
    # compare names_1 with names_2
    if bst.contains(name_2):
        # append duplicates to duplicates arr
        duplicates.append(name_2)

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.


# hashtable
# set
