'''

Note: The important point to note here is that if we have pairs like (a, b) 
and (b, c), then we can swap characters at indices a and c. 
Although we don't have the pair (a, c),
we can still swap them by first swapping them with the character at index b.
Thus, because we can swap the characters at these indices any number of times, 
we can rearrange the characters a, b, and c into any order.


# Combining the reachable index

Because we can swap infinite times, so we can get any order.

see

target = [2, 1, 4, 5], allowedSwaps = [[0, 1], [2, 3]]

we can get:

[2, 1, 4, 5], [1, 2, 4, 5], [2, 1, 5, 4], [1, 2, 5, 4]

What if there are some connections in allowedSwaps?

see

target = [2, 1, 4, 5], allowedSwaps = [[0, 1], [1, 2]]

These indexes [0, 1] and [1, 2] are connected by index 1. In a word, [0, 1, 2] are connected, so we can basically change them in any order

we can get:

[2, 1, 4, 5], [1, 2, 4, 5], [4, 1, 2, 5], [2, 4, 1, 5]


'''