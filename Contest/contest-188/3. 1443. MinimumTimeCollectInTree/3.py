# Time: O()     1228ms      16.86%
# Memory: O()   74MB      %
from typing import *


class Tree:
    def __init__(self, name, val):
        self.val = val
        self.name = name
        self.children = []
        self.time = 0
        self.apple_below = []


class Solution:
    def construct_tree(self, es, root, hasApple):
        t = Tree(root, hasApple[root])
        if root in es.keys():
            t.children = [self.construct_tree(es, i, hasApple) for i in es[root]]
        return t

    def apple(self, t: Tree):
        for i, c in enumerate(t.children):
            if self.apple(c):
                t.apple_below.append(i)
        if t.apple_below or t.val:
            return 1
        return 0

    def tt(self, t: Tree):
        for i in t.apple_below:
            t.time += 2 + self.tt(t.children[i])
        return t.time


    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        edges = sorted(edges)
        e_d = {}
        for e in edges:
            if e[0] in e_d.keys():
                e_d[e[0]].append(e[1])
            else:
                e_d[e[0]] = [e[1]]
        t = self.construct_tree(e_d, 0, hasApple)
        self.apple(t)
        ttt = self.tt(t)
        print(ttt)
        return ttt

if __name__ == '__main__':
    s = Solution()
    s.minTime(7,  [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], [0,0,1,0,1,1,0])

