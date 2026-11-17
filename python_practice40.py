# python_practice40.py  --  Nov 17, 2026 (Tuesday, week 3 of the new routine: 4 new problems a week)
# Problem: Min Stack, LeetCode 155 (new problem; a CLASS holding a stack of pairs (value, smallest so far);
#          taught from the idea up, then written by me)
# Results: morning Accepted 43/43, 108 ms (beats 43.01%), memory 12.6 MB (beats 12.16%).
#          evening redo: completed, Accepted 43/43 (time and memory not in the screenshot).

# ---------------------------------------------------------------
# The six questions
#   1. Name:    Min Stack
#   2. Does:    builds a stack class with push, pop, top and getMin, where getMin returns the SMALLEST value
#               currently in the stack, and every operation must be O(1)
#   3. Input:   calls on the class: push(val) with a number, pop(), top(), getMin() with nothing
#   4. Output:  top() and getMin() return a number; push and pop return nothing,
#               e.g. push(-2), push(0), push(-3): getMin() -> -3; pop(); top() -> 0; getMin() -> -2
#   5. Steps every time: say it in one sentence; name input and output with a tiny example;
#      ask "what do I need to remember?"; pick the tool; stage comments, then code;
#      trace a tricky input; say time and space; derive the "because" from the trace.
#   6. Algorithm (the five jobs, inside a class):
#        1. PREPARE    -> __init__: self.stack = [] (each item is a pair [value, smallest so far])
#        2. DECIDE     -> push: if self.stack == []: smallest_so_far = val
#        3. DECIDE     -> else: smallest_so_far = min(val, self.stack[-1][1]) (the smaller of the new value
#                         and the smallest stored in the top pair)
#        4. UPDATE     -> after the if/else (so it runs in both cases): self.stack.append([val, smallest])
#        5. UPDATE     -> pop: self.stack.pop() (takes the top pair off)
#        6. RETURN     -> top: return self.stack[-1][0] (the value of the top pair)
#        7. RETURN     -> getMin: return self.stack[-1][1] (the smallest-so-far of the top pair)
#
# Key question: what must I remember? For every item, the value AND the smallest value at the moment it was
# pushed (so that after a pop the new smallest is already known): a stack of pairs.
#   "stack with a fast minimum / O(1) / pop must not search" -> store the smallest-so-far with each item.
# ---------------------------------------------------------------


class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if self.stack == []:
            smallest_so_far = val
        else:
            smallest_so_far = min(val, self.stack[-1][1])
        self.stack.append([val, smallest_so_far])

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][-1]


# Trace for push(1), push(2), push(0), getMin, pop, top, getMin (his own example, walked through aloud):
#   push(1): the stack is empty, smallest is 1                  stack: [1,1]
#   push(2): min(2, 1) is 1                                      stack: [1,1] [2,1]
#   push(0): min(0, 1) is 0                                      stack: [1,1] [2,1] [0,0]
#   getMin() -> 0 (second number of the top pair)
#   pop()    -> removes [0,0]                                    stack: [1,1] [2,1]
#   top()    -> 2 (first number of the top pair)
#   getMin() -> 1 (second number of the top pair [2,1]); nothing was searched, the 1 was already stored
# Reference trace for the tricky case, a repeated smallest value: push(2), push(0), push(3), push(0):
#   stack: [2,2] [0,0] [3,0] [0,0]; getMin 0; pop -> [2,2] [0,0] [3,0]; getMin 0; pop -> [2,2] [0,0];
#   getMin 0; pop -> [2,2]; getMin 2. Each push stores its own pair, so popping one 0 leaves the other 0.
# Index reminder: self.stack[-1] is the top pair; [0] is its value, [1] (or [-1]) is its smallest so far.
#
# Slips fixed today:
#   1. Said it asks for "a new min stack with operations": it is a stack with push, pop, top, plus getMin,
#      the smallest value in the stack, fast.
#   2. getMin as min(self.stack) looks at every value: O(n), not O(1); the answer must already be stored.
#   3. Suggested a dict (value -> smallest): a repeated value overwrites the older one and a dict has no
#      top; a stack needs order and repeats, so a list of pairs.
#   4. push: self.stack == [] needs self; compared (==) instead of assigning (=) the smallest; compared
#      with min(self.stack) instead of min(val, top's smallest); the append belongs AFTER the if/else.
#   5. Indexing: self.stack[-1][0] is the top's value, self.stack[-1][1] its smallest-so-far.
#   6. pop: self.stack.pop() takes no number inside; .pop() is called on the list.
#   7. Return, not Return (Python is case-sensitive); top returns int.
#   8. How to run a design problem: call the methods one at a time (obj.push(...)); the list of names in
#      the LeetCode example is a description, not Python.
#   9. Time: said O(n) twice; each operation is O(1): a fixed number of steps on the top, no loop (model given).
#   10. The "because": a model was given; he says it back in his own words (the smallest is stored in every
#       pair, and popping just uncovers the older one).
#
# Complexity: time O(1) per operation: push does one min of two numbers and an append, pop and the reads
#               touch only the top of the stack, and nothing loops, so the time does not grow with the
#               stack (min(self.stack) would be O(n)).
#             space O(n): one pair per pushed value (two numbers each), twice as many numbers as a plain
#               stack.
#
# I used X because Y (model given today; say it in my own words):
# "I used a stack of pairs (value, smallest so far) because getMin must be O(1), and after a pop the new
#  smallest has to be already known. Each pair remembers the smallest of everything from the bottom up to
#  itself. A stack only changes at the top, so removing the top just uncovers the previous pair's smallest,
#  with no search. Time is O(1) per operation and space is O(n)."
#
# Interview sentence (model):
# "I keep a stack where each item is a pair: the value and the smallest value so far. Push stores the
#  smaller of the new value and the previous smallest, pop removes the top, and getMin reads the second
#  number of the top pair, so every operation is O(1). Space is O(n) for the pairs."

if __name__ == "__main__":
    obj = MinStack()
    obj.push(-2)
    obj.push(0)
    obj.push(-3)
    print(obj.getMin())   # -3
    obj.pop()
    print(obj.top())      # 0
    print(obj.getMin())   # -2

    obj = MinStack()
    obj.push(1)
    obj.push(2)
    obj.push(0)
    print(obj.getMin())   # 0
    obj.pop()
    print(obj.top())      # 2
    print(obj.getMin())   # 1

    obj = MinStack()
    obj.push(2)
    obj.push(0)
    obj.push(3)
    obj.push(0)
    print(obj.getMin())   # 0
    obj.pop()
    print(obj.getMin())   # 0
    obj.pop()
    print(obj.getMin())   # 0
    obj.pop()
    print(obj.getMin())   # 2

# Next: Wed Nov 18: repeat Valid Parentheses from a blank editor in the morning, then the next stack problem
# (Daily Temperatures or Evaluate Reverse Polish Notation), then the evening redo and quiz.
