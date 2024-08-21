class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        op = []

        for cur_num in range(1, n+1):
            op.append("Push")

            if cur_num != target[0]:
                op.append("Pop")
            else:
                target.pop(0)

                if len(target) == 0:
                    break
        
        return op
