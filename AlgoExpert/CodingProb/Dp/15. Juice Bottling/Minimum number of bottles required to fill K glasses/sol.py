from math import ceil
class Solution:
    def getMinBottle(self, N , K , arr):
        # sort the arr based on minimum volume
        arr.sort()

        # get the top K volume - getting the top k value makes sure that we have minimum volume
        min_volume = 0
        for i in range(K):
            min_volume += arr[i]

        total_no_of_bottle = ceil(min_volume / 100)

        return total_no_of_bottle



if __name__ == '__main__':
    N = 4 
    K = 3 
    arr = [200, 150, 140, 300]

    obj = Solution()
    print(obj.getMinBottle(N, K , arr))