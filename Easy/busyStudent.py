class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        return sum([(queryTime >= startTime[i] and queryTime <= endTime[i]) for i in range(len(startTime)) ])
