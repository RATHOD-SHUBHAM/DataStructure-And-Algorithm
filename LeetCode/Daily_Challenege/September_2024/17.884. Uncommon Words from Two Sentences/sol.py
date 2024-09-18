class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        list_s1 = s1.split(' ')
        list_s2 = s2.split(' ')

        counter = collections.defaultdict(int)

        op = []

        for ch in list_s1:
            counter[ch] += 1
        
        for ch in list_s2:
            counter[ch] += 1
        
        
        for ch, count in counter.items():
            if count <= 1:
                op.append(ch)
        
        return op