# https://leetcode.com/problems/water-bottles/discuss/3404506/Simple-Logic

# Tc: O(n) | Sc: O(1)

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        drink_bottle = 0
        
        while True:
        
            # check how many will remain if we sell the empty bottle
            remainingBottle = numBottles % numExchange
            # print(remainingBottle)

            # sell only those bottle that will yeild use one bottle
            sell_full_bottle = numBottles - remainingBottle
            # print(sell_full_bottle)

            # in the end if suppose we have some bottle left
            if sell_full_bottle == 0:
                drink_bottle += numBottles
                break

            # when we sell this is the number of bottle we did drink
            drink_bottle += sell_full_bottle

            # how many bottle did we get back after selling the empty ones
            extra_bottle_obtained = sell_full_bottle // numExchange
            # print(extra_bottle_obtained)

            # add them to the bottle we previously had
            numBottles = remainingBottle + extra_bottle_obtained
            # print(numBottles)
            
            # print("\n")
        
        # print(drink_bottle)
        return drink_bottle