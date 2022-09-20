# https://www.youtube.com/watch?v=ey82ZWRAqkM&ab_channel=AlgorithmsCasts
# Tc: O(nlogn)
# Sc: O(n)

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        # meeting will take place in the unused room -- lowest numbered room first
        unused_room = [i for i in range(n)] #There are n rooms numbered from 0 to n - 1
        # print(unused_room)
        heapq.heapify(unused_room)
        
        # keep track of meetings and room
        meeting_room = [] #(endTime, room) : Endtime: when the meeting will be over; and the room that will get free
        
        # keep track of the room that held the most meetings
        room_usage = [0 for _ in range(n)]
        # print(room_usage)
        
        # Meetings that have an earlier original start time should be given the room.
        # sort the meeting based on start time
        for st, et in sorted(meetings):
            #st: start time; et: end time;
            
            # check if the previous meeting end before start of current meeting
            # if so take the room of previous meeting
            
            # if the end time of previous meeting is smaller than current start time --> use the previous room
            while meeting_room and meeting_room[0][0] <= st:
                endTime , room = heapq.heappop(meeting_room)
                
                # add the room to unused room list
                heapq.heappush(unused_room, room)
                
            # if there are unused room available
            if unused_room:
                # get the room
                room = heapq.heappop(unused_room)
                # use it for current meeting
                heapq.heappush(meeting_room, (et, room))
                
                # since the room was held for meeting, increase usage count
                room_usage[room] += 1
                
            # if there are no rooms available
            else:
                # get the room whose meeting will end soon
                endTime, room = heapq.heappop(meeting_room)
                # calculate the current meeting duration
                current_meeting_duration = et - st
                # calculate the delay
                st = endTime
                et = endTime + current_meeting_duration
                
                # now assign the meeting room
                heapq.heappush(meeting_room, (et, room))
                
                 # since the room was held for meeting, increase usage count
                room_usage[room] += 1
                
        # once all the meetings are over -  check the room with max usage
        # print(room_usage)
        max_usage = 0
        
        for i in range(n):
            if room_usage[max_usage] < room_usage[i]:
                max_usage = i
                
        return max_usage
                