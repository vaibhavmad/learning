# only practising what I am not aware of in section 1, 1 is sets, 2 is list join
# sets are a collection like lists and tuples
# key diff is that they do not contain order and do not hold duplicate values

# [] are used for lists, () for tuples and {} are used for sets, however, if we use empty {} we end up getting a dict, for an empty set, due to the similarity in the brackets, we use set()

set_1 = {1, 2, 5, 6, 9, 10}
set_2 = {1, 2, 3, 4, 5, 6}

# adding to a set
set_1.add(15)
print(set_1)
# {1, 2, 5, 6, 9, 10, 15}
# since sets can not hold duplicate values, if we do
set_1.add(1)
print(set_1)
# we get
# {1, 2, 5, 6, 9, 10, 15} > 1 existed already, so no new 1 value added to this set

# removing from a set
set_1.remove(15)
print(set_1)
# {1, 2, 5, 6, 9, 10}

# sets operations:
# find items which are in set 1 and not in set 2
print(set_1.difference(set_2))
# now, in set one and set 2 we have 1, 2, 5 & 6 as common, hence, this gets removed from set 1 and we get:
# {9, 10}
# we can do the same for set 2
print(set_2.difference(set_1))
# {3, 4} > 3 & 4 are in set 2, but not in set 1, other common numbers 1, 2, 5, 6 have been removed from the response


# we can also find uncommon by comparing 2 sets, basically, the values that exist in either of the sets but not in both
print(set_1.symmetric_difference(set_2))
# {3, 4, 9, 10} > we see, 1, 2, 5 & 6 are common, rest are not, that's what got printed here

# we can also check what value exists in both sets:
print(set_1.intersection(set_2))
# {1, 2, 5, 6}


# moving on to list join
my_friends = ['bob', 'anne', 'sam']
# now, we can convert this into a string by using join
# we do
print(", ".join(my_friends))
# we get ", " comma space separated list items as one string: bob, anne, sam