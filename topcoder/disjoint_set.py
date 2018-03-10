
numbers = [[1], [2], [3], [4], [5]]

def find(x):
    # this will return the position of parent which contains x
    index = 0
    for parent in numbers:
        if parent.__contains__(x):
            return index
        index = index + 1

    print("parent not found")

def union(x, y):
    # this will merge parent x and y
    from copy import deepcopy
    parents = deepcopy(numbers)

    new_numbers = []
    x_pos = find(x)
    y_pos = find(y)

    x_set = deepcopy(parents[x_pos])
    y_set = deepcopy(parents[y_pos])

    parents.remove(x_set)
    parents.remove(y_set)

    for element in y_set:
        x_set.append(element)

    new_numbers.append(x_set)
    print(new_numbers)

    for parent in parents:
        new_numbers.append(parent)

    return new_numbers

uni = union(1, 2)
print(uni)
uni_2 = union(3, 4)
print(uni_2)
