# python_practice41.py  --  Nov 18, 2026 (Wednesday, week 3 of the new routine: 4 new problems a week)
# Problem: Evaluate Reverse Polish Notation, LeetCode 150 (new problem; a STACK of numbers; an operator
#          takes the top two off and pushes the result back; taught from the idea up, then written by me)
# Results: morning Accepted 55/55, 91 ms (beats 100.00%), memory 10.7 MB (beats 94.71%).
#          evening redo from a blank editor: completed, Accepted 55/55 (time and memory not in the screenshot).
#          The repeat of Valid Parentheses planned for today was moved to Saturday's check (his choice).

# ---------------------------------------------------------------
# The six questions
#   1. Name:    Evaluate Reverse Polish Notation
#   2. Does:    evaluates a postfix expression: every operator works on the TWO values (numbers or results)
#               just BEFORE it
#   3. Input:   a list of strings, each a number ("2", "-11") or an operator "+", "-", "*", "/"
#   4. Output:  one integer, e.g. ["2","1","+","3","*"] -> 9 ((2 + 1) * 3);
#               ["4","13","5","/","+"] -> 6 (4 + 13 / 5, division truncates toward zero)
#   5. Steps every time: say it in one sentence; name input and output with a tiny example;
#      ask "what do I need to remember?"; pick the tool; stage comments, then code;
#      trace a tricky input; say time and space; derive the "because" from the trace.
#   6. Algorithm (the five jobs):
#        1. PREPARE    -> stack = [] and operators = ["+", "-", "*", "/"]
#        2. GO THROUGH -> for token in tokens
#        3. DECIDE     -> if token in operators
#        4. UPDATE     -> b = stack.pop() (the newer one), then a = stack.pop() (the older one, the LEFT side)
#        5. UPDATE     -> result from a and b by the operator (if / elif); "/" is int(a / b);
#                         then stack.append(result)
#        6. UPDATE     -> else it is a number: stack.append(int(token)) (tokens are strings)
#        7. RETURN     -> return stack[-1] after the loop (the one number left)
#
# Key question: what must I remember? The numbers (and results) still waiting for an operator, the newest on
# top: a stack.
#   "postfix / an operator uses the two most recent values / its result is the newest value" -> a stack.
# Pattern: "the newest comes first, so a stack"; what changes is WHAT the newest thing is: an open bracket
#   (Valid Parentheses), a value with its smallest (Min Stack), a number waiting for an operator (this one).
# ---------------------------------------------------------------

from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ["+", "-", "/", "*"]
        for token in tokens:
            if token in operators:
                b = stack.pop()
                a = stack.pop()
                if token == "+":
                    result = a + b
                elif token == "-":
                    result = a - b
                elif token == "*":
                    result = a * b
                elif token == "/":
                    result = int(a / b)
                stack.append(result)
            else:
                stack.append(int(token))
        return stack[-1]


# Trace for ["2","1","+","3","*"]:
#   "2" number, push                                        stack: [2]
#   "1" number, push                                        stack: [2, 1]
#   "+" operator: b = 1, a = 2, 2 + 1 = 3, push             stack: [3]
#   "3" number, push                                        stack: [3, 3]
#   "*" operator: b = 3, a = 3, 3 * 3 = 9, push             stack: [9]
#   return stack[-1] -> 9
# His own test ["1","2","+","3","*","4","-"]: [1,2] -> [3] -> [3,3] -> [9] -> [9,4] -> "-": b = 4, a = 9,
#   a - b = 5 (not b - a) -> [5]; returns 5.
# Tricky case ["-7","2","/"]: stack [-7, 2]; b = 2, a = -7; int(-7 / 2) is int(-3.5) = -3 (truncates toward
#   zero); -7 // 2 would be -4 (rounds down), which is wrong here.
# Other checks: ["4","13","5","/","+"] -> 4 + int(13 / 5) = 4 + 2 = 6; one token ["3"] -> [3] -> 3.
#   After b and a are popped, the numbers live in the variables a and b; stack[-2] - stack[-1] would point
#   at whatever is left underneath.
#
# Slips fixed today:
#   1. Said it evaluates "integers based on the operands after it": an operator works on the two values just
#      BEFORE it.
#   2. Picked a stack with the reason: the operator needs the newest two (stack[-1], stack[-2]); the two are
#      taken off and the result goes back on.
#   3. Wrote what to do per token but not the stack states: an operator takes two off and puts one on.
#   4. Order matters for - and /: the older number (stack[-2]) is the LEFT side, so a - b, not b - a.
#   5. First draft: list as a variable name hides the built-in (use operators); = instead of == in if and
#      elif; b - a; the result was never pushed back; push int(token) is not Python (stack.append(...)); the
#      last else must belong to the outer if.
#   6. After the two pops, a and b are variables: stack[-2] - stack[-1] points at other numbers; and
#      stack.append(result) must sit inside the operator branch (a wrong indent made the else a syntax error).
#   7. Trace comments must describe the state AT that line (at b = stack.pop() the stack is still [1, 2]); after
#      b is popped, a is the new top.
#   8. Division: int(a / b) truncates toward zero (-7 / 2 gives -3); // rounds down (-4).
#   9. Time: each token is handled once and each pop, append and calculation is one step; space: the reason is
#      the stack (up to about half of the tokens wait on it), not "a single number as the output".
#   10. The "because" first described what the code does; a model was given; he says it in his own words.
#
# Complexity: time O(n): each token is handled once, and each pop, append and calculation takes one step.
#             space O(n): in the worst case (all numbers first, like ["1","2","3","4","5","+","+","+","+"])
#               about half of the tokens wait on the stack.
#
# I used X because Y (model given today; say it in my own words):
# "I used a stack because in Reverse Polish Notation an operator always applies to the two most recent
#  values just before it, and its result becomes the newest value for the next operator. A stack always gives
#  me the newest at the top (last in, first out), so each operator takes the top two off and puts the result
#  back. Each token is handled once, so time is O(n), and space is O(n) for the numbers waiting on the stack."
#
# Interview sentence (model):
# "I go through the tokens with a stack. A number is pushed; an operator pops the top two, the older one is the
#  left operand, applies the operator (int(a / b) for division, to truncate toward zero) and pushes the
#  result. At the end the stack holds the answer. Time is O(n) and space is O(n)."

if __name__ == "__main__":
    print(Solution().evalRPN(["2", "1", "+", "3", "*"]))                     # 9
    print(Solution().evalRPN(["4", "13", "5", "/", "+"]))                    # 6
    print(Solution().evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))   # 22
    print(Solution().evalRPN(["1", "2", "+", "3", "*", "4", "-"]))           # 5
    print(Solution().evalRPN(["-7", "2", "/"]))                              # -3
    print(Solution().evalRPN(["4", "1", "-"]))                               # 3
    print(Solution().evalRPN(["3"]))                                         # 3

# Next: Thu Nov 19: the next stack problem (Daily Temperatures, or Generate Parentheses), then the evening redo and
# quiz. Saturday check: repeat Valid Parentheses and Min Stack from a blank editor; say the becauses from memory.
