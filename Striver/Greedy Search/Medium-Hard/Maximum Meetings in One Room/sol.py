# Tc: O(NlogN)
# Sc: O(N)

from typing import List


class Solution:
    def maxMeetings(self, N : int, S : List[int], F : List[int]) -> List[int]:
        # code here
        arr = []
        for i in range(N):
            val = [S[i], F[i], i+1]
            arr.append(val)

        """Sort as per End time.
        The faster the meeting gets over, the room can be used for another meeting, 
        hence increasing the max number of meeting
        """
        arr.sort(key = lambda x: x[1])

        
        # Initialize the end time of the previous meeting to the end time of the first meeting
        prev_meeting_end_time = arr[0][1]
        
        count = 1
        indexes = [arr[0][2]]  # Store the index of the first meeting
        
        for i in range(1, N):
            start_time, end_time, idx = arr[i]
            
            if prev_meeting_end_time >= start_time:
                continue
            
            prev_meeting_end_time = end_time
            count += 1
            indexes.append(idx)
        
        # Sort the indexes of the meetings that can be attended
        return sorted(indexes)


if __name__ == "__main__":
    N = 5
    S = [1, 3, 0, 5, 8, 5]
    F = [2, 4, 6, 7, 9, 9]
    sol = Solution()
    sol.maxMeetings(N, S, F)
    # Expected output: [1, 2, 4, 5]

    # 12 6 16 12 6 9 16 6 17 5
    # 17 13 16 18 17 10 18 12 18 11
    N = 10
    S = [12, 6, 16, 12, 6, 9, 16, 6, 17, 5]
    F = [17, 13, 16, 18, 17, 10, 18, 12, 18, 11]
    sol = Solution()
    sol.maxMeetings(N, S, F)
    # Expected output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]