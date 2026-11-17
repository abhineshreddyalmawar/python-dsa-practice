# python_practice39.py  --  Nov 16, 2026 (Monday, week 3 of the new routine: 4 new problems a week)
# Problem: Valid Parentheses, LeetCode 20 (new problem; a STACK: a list with .append and .pop, plus a dict of
#          pairs; taught from the idea up, then written by me)
# Results: morning Accepted 42/42, 28 ms (beats 59.84%), memory 7.7 MB (beats 99.61%).
#          evening redo from a blank editor: completed (result figures not recorded).

# ---------------------------------------------------------------
# The six questions
#   1. Name:    Valid Parentheses
#   2. Does:    checks that every opening bracket is closed by the SAME type of bracket, and in the
#               CORRECT order (the newest open bracket must be closed first)
#   3. Input:   a string s made only of ( ) { } [ ]
#   4. Output:  a boolean: True or False, e.g. "()[]{}" -> True, "{[]}" -> True, "(]" -> False,
#               "([)]" -> False
#   5. Steps every time: say it in one sentence; name input and output with a tiny example;
#      ask "what do I need to remember?"; pick the tool; stage comments, then code;
#      trace a tricky input; say time and space; derive the "because" from the trace.
#   6. Algorithm (the five jobs):
#        1. PREPARE    -> pairs = {opening: closing} (a dict), stack = [] (a list)
#        2. GO THROUGH -> for char in s
#        3. DECIDE     -> if char in pairs: it is an OPENING bracket (in checks the keys only)
#        4. UPDATE     -> stack.append(char): the newest open bracket goes on top
#        5. DECIDE     -> else (a closing bracket): if stack == [] or pairs[stack[-1]] != char: return False
#                         (nothing is open, or the top needs a different closing bracket)
#        6. UPDATE     -> stack.pop(): the top matched, take it off
#        7. RETURN     -> after the loop: return True only if stack == [] (nothing left open)
#
# Key question: what must I remember? Every open bracket still waiting to be closed, IN THE ORDER they
# came, with the newest on top: a list used as a stack. And, for each closing bracket, which opening
# bracket it needs: a dict.
#   "brackets / newest opened must be closed first / matching pairs" -> a stack (last in, first out)
#   plus a dict of pairs.
# ---------------------------------------------------------------


class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {"(": ")", "{": "}", "[": "]"}
        stack = []
        for char in s:
            if char in pairs:
                stack.append(char)
            else:
                if stack == [] or pairs[stack[-1]] != char:
                    return False
                stack.pop()
        if stack == []:
            return True
        return False


# Trace for "([{}])" (valid):
#   (  opening, append          stack: (
#   [  opening, append          stack: ( [
#   {  opening, append          stack: ( [ {
#   }  closing: top { needs }, equal -> no return, pop      stack: ( [
#   ]  closing: top [ needs ], equal -> no return, pop      stack: (
#   )  closing: top ( needs ), equal -> no return, pop      stack: empty
#   after the loop the stack is empty -> True
# Trace for "([)]" (invalid):
#   (  append   stack: (
#   [  append   stack: ( [
#   )  closing: top is [, pairs["["] is ], not ) -> return False (wrong order: [ had to be closed first)
# Other edge cases:
#   ")"   closing bracket on an EMPTY stack: stack == [] is checked first (or stops there), so stack[-1] is
#         never read -> False
#   "(("  nothing is popped, the stack still holds ( ( after the loop -> False
#   "()(" the stack is empty after "()", but the last ( stays open -> False (the final check must run
#         AFTER the loop; inside the loop it would return True too early)
#   ""    the loop never runs, the stack is empty -> True
#
# Slips fixed today:
#   1. Said the input is "a stack": the input is a STRING; the stack is the tool.
#   2. "([)]": every bracket has a partner of the right type, but the order is wrong: the newest open
#      bracket must be closed first.
#   3. Picked a set: a set has no order and loses repeats ("((" is one item); the notebook is a list used
#      as a stack (.append puts on top, .pop takes the top, stack[-1] looks at the top).
#   4. What to remember: ALL the open brackets in order, not only the latest one (after a pop, the next
#      newest is needed).
#   5. Dict direction {opening: closing} works: `char in pairs` checks only the KEYS, so a closing bracket is
#      not "in pairs" and goes to the else; pairs[top] gives the closing bracket the top needs.
#   6. The closing-bracket check ran for every character (missing else); then added the else.
#   7. No check for an empty stack before stack[-1]; the empty check must come FIRST in the `or`.
#   8. Syntax: stack(.pop()) should be stack.pop(); missing colons; missing the final return False.
#   9. Indentation: stack.pop() sat after return False (never ran); the final `if stack == []` sat inside
#      the for (it returned True too early for "()("); both moved.
#   10. Thought pairs[top] != char is True on a match: it is False on a match (they are equal), so the
#      return False is skipped and the code pops; return False happens only for a real problem.
#   11. Trace of the valid string said "returns False and pops" at a match: no return on a match.
#   12. Space is O(n), not O(1): the worst case ("(((((") keeps every character on the stack.
#   13. The "because" first described what the code does; a model was given and he said it back in his own
#      words (newest closes first; the dict tells which partner is needed).
#
# Complexity: time O(n): the loop touches each character once, and append, pop and the dict lookup each take
#               one step.
#             space O(n): in the worst case (all opening brackets) every character stays on the stack; the
#               dict has 3 entries, a fixed size.
#
# I used X because Y:
# "I used a stack (a list with .append and .pop) because the newest open bracket must be closed first, and
#  a stack always gives me the newest one at the top. I used a dict because when a closing bracket arrives
#  it tells me which opening bracket the top must be, so I can check the type in one step. Time is O(n)
#  and space is O(n)."
#
# Interview sentence:
# "I go through the string with a stack. An opening bracket goes on the stack; a closing bracket must match
#  the top, so if the stack is empty or the top is a different type I return False, otherwise I pop. At the
#  end the stack must be empty. Time is O(n) and space is O(n)."

if __name__ == "__main__":
    print(Solution().isValid("()"))          # True
    print(Solution().isValid("()[]{}"))      # True
    print(Solution().isValid("{[]}"))        # True
    print(Solution().isValid("([{}])"))      # True
    print(Solution().isValid("(]"))          # False
    print(Solution().isValid("([)]"))        # False
    print(Solution().isValid(")"))           # False
    print(Solution().isValid("(("))          # False
    print(Solution().isValid("()("))         # False
    print(Solution().isValid(""))            # True

# Next: Tue Nov 17: the next stack problem (Min Stack or Daily Temperatures), then the evening redo and quiz.
