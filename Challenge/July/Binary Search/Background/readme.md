# What is Binary Search?
Binary Search is one of the most fundamental and useful algorithms in Computer Science. 
It describes the process of searching for a specific value in an `ordered collection`.

## Ordered Collection meaning Sorted List.

# Terminology used in Binary Search:

* Target - the value that you are searching for
* Index - the current location that you are searching
* Left, Right - the indices from which we use to maintain our search Space
* Mid - the index that we use to apply a condition to determine if we should search left or right

---

# How does it work?

In its simplest form, Binary Search operates on a `contiguous sequence` with a specified left and right index. This is called the `Search Space`. 

Binary Search maintains the left, right, and middle indicies of the search space and compares the search target or applies the search condition to the middle value of the collection; if the condition is unsatisfied or values unequal, the half in which the target cannot lie is eliminated and the search continues on the remaining half until it is successful. 

If the search ends with an empty half, the condition cannot be fulfilled and target is not found.

Binary Search can take many alternate forms and might not always be as straight forward as searching for a specific value. Sometimes you will have to apply a specific condition or rule to determine which side (left or right) to search next.