class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        n = len(mountain)

        peaks = []

        for i in range(1, n-1):
            if mountain[i-1] < mountain[i] and mountain[i+1] < mountain[i]:
                peaks.append(i)
        
        return peaks