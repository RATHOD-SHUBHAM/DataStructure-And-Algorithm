https://www.youtube.com/watch?v=pPiSMPWKZ3E&t=120s&ab_channel=OggiAI-ArtificialIntelligenceToday

* Note that upper_bound and bisect.bisect_right look for the rightmost insertion position, 
* while lower_bound and bisect.bisect_left look for the leftmost insertion position.

* Right most insertion point is = Insert after a idx . Insert at correct position
* Left Most Insertion point is = Insert after a idx . Insert at correct position

Basically,
* bisect_left find an insertion point for an item in sorted list. Insert to left of item.
* If there is a match, return a spot to the left of it.

* bisect_right find an insertion point for an item in sorted list. Insert to right of item.
* If there is a match, return a spot to the right of it.

It return the index to be inserted at if target is not found.
If target is found:
    * bisect_right : return the right index.
    * bisect_left : return the left index.

---

# 3 Parts of a Successful Binary Search

Binary Search is generally composed of 3 main sections:

    * Pre-processing - Sort if collection is unsorted.

    * Binary Search - Using a loop or recursion to divide search space in half after each comparison.

    * Post-processing - Determine viable candidates in the remaining space.
