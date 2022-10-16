# https://www.youtube.com/watch?v=Du881K7Jtk8&ab_channel=takeUforward

def NGE(array):
    n = len(array)
    stack = [] # monotonous stack
    nge = [-1] * n

    # consider and imaginary array, where the second half is a copy of first half
    for i in reversed(range(2 * n)):
        # if the top of stack is less than current element, then remove till you find the greater ele
        while stack and stack[-1] <= array[i % n]:
            stack.pop()

        # once we are inside the actual array
        if i < n:
            if stack:
                nge[i] = stack[-1] # next greater element is top of stack
            else:
                nge[i] = -1

        stack.append(array[i % n]) # append the element in stack because this could be the possible next greater element
    
    return nge



if __name__ == '__main__':
    ip = [2, 10 , 12, 1, 11]
    nextGreaterElement = NGE(ip)
    print(nextGreaterElement)