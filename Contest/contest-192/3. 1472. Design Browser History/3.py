# Time: O()     ms      %
# Memory: O()   MB      %
from typing import *


class BrowserHistory:

    def __init__(self, homepage: str):
        self.c = homepage
        self.history = [self.c]
        self.pointer = 0

    def visit(self, url: str) -> None:
        self.history = self.history[:self.pointer + 1]
        self.history.append(url)
        self.c = url
        self.pointer += 1

    def back(self, steps: int) -> str:
        if steps > self.pointer:
            self.pointer = 0
        else:
            self.pointer -= steps
        return self.history[self.pointer]

    def forward(self, steps: int) -> str:
        if steps > (len(self.history) - self.pointer - 1):
            self.pointer = len(self.history) - 1
        else:
            self.pointer += steps
        return self.history[self.pointer]

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
