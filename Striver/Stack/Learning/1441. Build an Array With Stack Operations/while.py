class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        op = []

        cur_num = 0

        while len(target) > 0:
            cur_num += 1

            op.append("Push")

            if cur_num != target[0]:
                op.append("Pop")
            else:
                target.pop(0)
        
        return op
            

