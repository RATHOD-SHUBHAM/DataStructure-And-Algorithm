# Tc: O(1)
# Sc: O(n)

class FreqStack:
    '''
    * have 2 dictionary
        1. To store the frequency/count of the value.
        2. To store the value with same count together -> # bucket
    '''
    def __init__(self):
        self.freq_cnt = {}
        self.bucket = {}
        self.maxCount = 0 # to get the max freq at cur time
        

    def push(self, val: int) -> None:
        # check if the val is already present or is it being added for the first time
        val_cnt = self.freq_cnt.get(val , 0) + 1 # increment by one because we have seen the value again
        
        #update the frequency count of cur value to new count
        self.freq_cnt[val] = val_cnt
        
        if val_cnt > self.maxCount:
            # this means new bucket needs to be created with this freq
            self.maxCount += 1
            self.bucket[val_cnt] = []
        
        self.bucket[val_cnt].append(val)
        
        
    def pop(self) -> int:
        # pop out the element with max frequency
        popEle = self.bucket[self.maxCount].pop()
        #update the freq
        self.freq_cnt[popEle] -= 1
        # if the bucket for that count is empty
        if not self.bucket[self.maxCount]:
            self.maxCount -= 1
            
        return popEle


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()