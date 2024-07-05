# Template I

## Distinguishing Syntax:

        * Initial Condition: 
            left = 0, right = length-1
        * Condition : 
            left <= right
        * Searching Left: 
            right = mid-1
        * Searching Right: 
            left = mid+1
        * Termination: 
            left > right

- No post-processing required because at each step, you are checking to see if the element has been found. If you reach the end, then you know the element is not found

# Template II

## Distinguishing Syntax:

        * Initial Condition: 
            left = 0, right = length - 1
        * Condition : 
            left < right
        * Searching Left: 
            right = mid
        * Searching Right: 
            left = mid+1
        * Termination: 
            left == right

- Post-processing required. Loop/Recursion ends when you have 1 element left. Need to assess if the remaining element meets the condition.
