# Time: O()     ms      %
# Memory: O()   MB      %
from typing import *


class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        count = 0
        for i, v in enumerate(startTime):
            if v <= queryTime <= endTime[i]:
                count += 1
        return count
