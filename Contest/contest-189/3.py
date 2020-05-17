# Time: O()     ms      %
# Memory: O()   MB      %
from typing import *


class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]):
        n = len(favoriteCompanies)
        lovers = {}
        for i, people in enumerate(favoriteCompanies):
            for j, company in enumerate(people):
                if company in lovers:
                    lovers[company].append(i)
                else:
                    lovers[company] = [i]
        table = [[1] * n for _ in range(n)]
        for i in range(n):
            table[i][i] = 0
        for company, lover in lovers.items():
            for i in range(n):
                if i not in lover:
                    for j in lover:
                        table[j][i] = 0

        ans = []
        for i, people in enumerate(table):
            if not sum(people):
                ans.append(i)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.peopleIndexes([["leetcode", "google", "facebook"], ["google", "microsoft"], ["google", "facebook"]]))
