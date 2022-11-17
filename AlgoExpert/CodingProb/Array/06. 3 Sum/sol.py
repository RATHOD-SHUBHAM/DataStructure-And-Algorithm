'''
a + b + c = target

if my sum > target -- reduce the sum
if my sum < target -- increse the sum

'''

# tc: O(n^2) | O(n)
def threeNumberSum(array, targetSum):
    array.sort()
    res = []
    n = len(array)

    for i in range(n):
        a = array[i]
        
        left = i + 1
        right = n - 1

        while left < right:
            b = array[left]
            c = array[right]

            curSum = a + b + c

            if targetSum == curSum:
                res.append([a,b,c])
                left += 1
                right -= 1
            
            elif targetSum < curSum:
                right -= 1
            else:
                left += 1

    return res
