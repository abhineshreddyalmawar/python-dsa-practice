# python_practice42.py  --  Nov 19, 2026 (Thursday, week 3 of the new routine: 4 new problems a week)
# Problem: Daily Temperatures, LeetCode 739 (new problem; a STACK of DAY NUMBERS still waiting for a warmer
#          day; taught from the idea up, then written by me)
# Results: morning Accepted 49/49, 84 ms (beats 82.07%), memory 11.1 MB (beats 78.41%).
#          evening redo: SKIPPED today (no time); do it tomorrow morning from a blank editor.

# ---------------------------------------------------------------
# The six questions
#   1. Name:    Daily Temperatures
#   2. Does:    for every day, counts how many days you must wait after it for a WARMER temperature
#               (0 if there is none)
#   3. Input:   a list of numbers, the temperature of each day
#   4. Output:  a list of the same length, e.g. [73,74,75,71,69,72,76,73] -> [1,1,4,2,1,1,0,0]
#   5. Steps every time: say it in one sentence; name input and output with a tiny example;
#      ask "what do I need to remember?"; pick the tool; stage comments, then code;
#      trace a tricky input; say time and space; derive the "because" from the trace.
#   6. Algorithm (the five jobs):
#        1. PREPARE    -> answer = [0] * len(temperatures) (zeros: days with no warmer day stay 0),
#                         stack = [] (the day NUMBERS still waiting for a warmer day)
#        2. GO THROUGH -> for day in range(len(temperatures))
#        3. DECIDE     -> while stack != [] and temperatures[day] > temperatures[stack[-1]]
#                         (the stack is checked for empty FIRST; the newest waiting day is the coldest)
#        4. UPDATE     -> a = stack.pop() (the waiting day answered now); result = day - a;
#                         answer[a] = result (the answer belongs to the day that WAITED)
#        5. UPDATE     -> after the while: stack.append(day) (today joins the waiting days)
#        6. RETURN     -> return answer, after the loop
#
# Key question: what must I remember? The days that have not yet found a warmer day, the newest on top,
# and, for each, where to write its answer: a stack of day numbers (from a day number I get both its
# temperature, temperatures[day], and its wait, today - day).
#   "how many days until a warmer one / next greater" -> a stack of positions.
# Pattern: "the newest comes first, so a stack"; here the newest thing is a day still waiting.
# ---------------------------------------------------------------

from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []
        for day in range(len(temperatures)):
            while stack != [] and temperatures[day] > temperatures[stack[-1]]:
                a = stack.pop()
                result = day - a
                answer[a] = result
            stack.append(day)
        return answer


# Trace for [30,38,30,36,35,40,28]:
#   day 0 (30): stack empty, push                         stack [0]        answer [0,0,0,0,0,0,0]
#   day 1 (38): 38 > 30, pop day 0, answer[0] = 1; push   stack [1]        answer [1,0,0,0,0,0,0]
#   day 2 (30): 30 > 38 no; push                          stack [1,2]
#   day 3 (36): 36 > 30, pop day 2, answer[2] = 1; 36 > 38 no; push
#                                                         stack [1,3]      answer [1,0,1,0,0,0,0]
#   day 4 (35): 35 > 36 no; push                          stack [1,3,4]
#   day 5 (40): pop 4 (answer[4] = 1), pop 3 (answer[3] = 2), pop 1 (answer[1] = 4); push
#                                                         stack [5]        answer [1,4,1,2,1,0,0]
#   day 6 (28): 28 > 40 no; push                          stack [5,6]
#   return [1,4,1,2,1,0,0]   (days 5 and 6 never found a warmer day, so they stay 0)
# Worked by hand first on [73,74,75,71,69,72,76,73] with a "waiting list": day 5 (72) answers days 4 and 3 and
# stops at day 2 (75); day 6 (76) answers days 5 and 2.
# Why we can stop at the first waiting day that is not colder: the waiting days go from warmest at the bottom
# to coldest on top, so if today is not warmer than the top, it is not warmer than any day below it.
#
# Slips fixed today:
#   1. The direct method (for each day, look forward) is O(n squared): 4 + 3 + 2 + 1 = 10 looks for 5 days.
#   2. The "waiting list" idea was not clear at first; walked through day by day: a day answers the waiting
#      days that are colder, newest first.
#   3. Day 5: the answer for day 4 is 5 - 4 (the waiting day itself); day 2 (75) is warmer than 72 so it
#      stays waiting; the day that joins at the end is today.
#   4. Day 7: day 2 had already left at day 6; the waiting list was [6], then [6, 7].
#   5. The stack holds DAY NUMBERS, not temperatures: from a day I get its temperature and its wait.
#   6. The result was calculated but never saved; the position slip again (position vs value, like
#      counts[right]): answer[day], answer[day - 1], answer[day - a] are wrong; the answer belongs to the
#      waiting day: answer[a] = result. The editor still had the old line until the output was compared.
#   7. Hand-trace comments: for day 3 the popped day is 2; answer is the WHOLE list from the start; the stack
#      after day 3 is [1, 3].
#   8. Oral explanation: compare with the waiting day on TOP (not "the previous day"), store at answer[a],
#      the while can repeat, and today joins the stack after the while.
#   9. The "because": the days beneath the top are WARMER (not colder), which is why we can stop.
#
# Complexity: time O(n): each day is pushed once and popped at most once, so the while inside the for does at
#               most n pops in total (about 2n steps).
#             space O(n): the stack can hold every day (a list that only goes down) and the answer list has n
#               numbers.
#
# I used X because Y (his own words, with one word fixed):
# "I used a stack of day numbers because the newest waiting day is the coldest, so it is the first to be
#  answered when a warmer day arrives. The days below it are warmer, so the first one that is not colder
#  lets me stop. Each day is pushed once and popped at most once, so time is O(n), and space is O(n) for
#  the stack and the answer list."
#
# Interview sentence:
# "I keep a stack of the days still waiting for a warmer temperature. Each new day pops every colder waiting
#  day and records how long it waited, then joins the stack. Each day is pushed and popped at most once, so
#  time is O(n); space is O(n)."

if __name__ == "__main__":
    print(Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))   # [1, 1, 4, 2, 1, 1, 0, 0]
    print(Solution().dailyTemperatures([30, 38, 30, 36, 35, 40, 28]))       # [1, 4, 1, 2, 1, 0, 0]
    print(Solution().dailyTemperatures([22, 21, 20]))                       # [0, 0, 0]
    print(Solution().dailyTemperatures([30, 40, 50, 60]))                   # [1, 1, 1, 0]
    print(Solution().dailyTemperatures([30]))                               # [0]
    print(Solution().dailyTemperatures([]))                                 # []

# Next: Fri Nov 20: redo Daily Temperatures from a blank editor in the morning, then the Saturday-check
# preparation (Valid Parentheses and Min Stack repeats, becauses from memory). Chapter 9 and 10 recalls owed.
