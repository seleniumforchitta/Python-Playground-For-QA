"""You have two lists, both of them contain digits.
The first list is [1, 3, 4, 5, 7, 0, 3, 2, 7, 2],
the second one is [9, 2, 3, 4, 8].
You should create a method which returns a collection with digits,
which exist in two lists. This collection must contain unique values."""
def common_member(a, b):
    first_set = set(a)
    second_set = set(b)

    if (first_set & second_set):
        common_set =  first_set & second_set
        return set(common_set)
    else:
        print("There is no common element found.")


a = [1, 3, 4, 5, 7, 0, 3, 2, 7, 2]
b = [9, 2, 3, 4, 8]
print(common_member(a,b))