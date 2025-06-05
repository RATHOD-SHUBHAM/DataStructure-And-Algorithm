# Subsequence vs. Subset

## Subsequence
### Definition:
A subsequence is a sequence derived from another sequence by deleting zero or more elements, without changing the order of the remaining elements.

### Key Point:
The elements must appear in the same order as in the original sequence, but they do not have to be contiguous.

### Example:
Original: [A, B, C, D]
Valid subsequences:

[A, C, D] (removed B)

[B, D] (removed A and C)

[A, B, C, D] (itself)

[A, D] (removed B and C)

[ ] (empty subsequence) # very important 

# ----------------------------------------------------------------------------------------------------- #

## Subset
### Definition:
A subset is any combination of elements from a set (or array), regardless of their order or positions.

### Key Point:
Order doesn’t matter. A subset can have elements in any order, and you simply select any group of elements (including none or all).

### Example:
Original set: {A, B, C, D}
Valid subsets:

{A, B}

{B, D}

{A, C, D}

{D, B, A} (order doesn’t matter in sets)

{} (empty set)

## Quick Table
Property	            Subsequence	                        Subset
Order	                Preserved	                        Irrelevant
Must be contiguous?	    No	                                No
Possible Duplicates?	Yes (if original has duplicates)	Yes
Empty allowed?	        Yes	                                Yes

## Key Difference
Subsequence: Order is preserved; elements are chosen by skipping some (can’t rearrange).

Subset: Order is irrelevant; just any selection of elements.

## Interview Tip:
If the question asks about sequence or order, think “subsequence”.
If it’s just “pick any group”, think “subset”.

# ----------------------------------------------------------------------------------------------------- #

# The difference between a substring and a subsequence lies in order and continuity:

# 🔹 Substring
A substring is a contiguous (continuous) part of a string.

All characters in a substring appear in the same order and are adjacent in the original string.

Example:
For the string "abcde":

Valid substrings: "ab", "bcd", "abcde", "c"

Invalid substring: "ace" (not contiguous)

# 🔹 Subsequence
A subsequence is a sequence that appears in the same relative order, but not necessarily contiguous.

You can skip characters, but you cannot change the order.

Example:
For the string "abcde":

Valid subsequences: "ace", "bd", "abc", "e"

Invalid subsequence: "aec" (characters out of order)

# ----------------------------------------------------------------------------------------------------- #
