'''

# todo:  Brute Force Approach

from typing import List

# todo : sliding window concept
class Solution():
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        total_sum = 0
        if len(nums) < 2:
            return False
        for start in range(len(nums)):
            # print(start)
            i = start + k - 1
            # print("i is : ",i)
            if i<len(nums):
                i = i+1
                sum_no = 0
                for j in range(start,i):
                    print("j is : ",j)
                    print("start j is: ",start)
                    print("i j is : ",i)
                    sum_no = sum_no + nums[j]
                    print("sum_no is: ",sum_no)
                    print("\n\n")
                    total_sum = max(total_sum , sum_no)
                    print("sum is : ",total_sum)
                    avg = total_sum/k
                    print(avg)
        return avg





def main():
    nums = [1,12,-5,-6,50,3]
    k = 4
    s = Solution()
    my_func = s.findMaxAverage(nums,k)
    print("The Final result is : ",my_func)


if __name__ == '__main__':
    main()


'''

# todo : Approach

from typing import List


class Solution():
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        x = 0
        total_sum = sum(nums[:k])
        max_sum = total_sum

        for i in range(k,len(nums)):
            total_sum = total_sum + nums[i] - nums[x]
            max_sum = max(max_sum,total_sum)
            x += 1
        return(max_sum/float(k))





def main():
    nums = [1,12,-5,-6,50,3]
    k = 4
    s = Solution()
    my_func = s.findMaxAverage(nums,k)
    print("The Final result is : ",my_func)


if __name__ == '__main__':
    main()

