# python_practice43.py  --  Nov 23, 2026 (Monday, week 4 of the new routine: 4 new problems a week)
# Problem: Car Fleet, LeetCode 853 (new problem; sort the cars front to back, then a STACK of arrival hours
#          of the fleets so far; taught from the idea up, then written by me)
# Results: morning Accepted 25/25, 68 ms (beats 70.63%), memory 20.3 MB (beats 99.42%).
#          evening redo from a blank editor: Accepted 25/25, 67 ms (beats 70.65%), memory 20.2 MB (beats 99.42%).

# ---------------------------------------------------------------
# The six questions
#   1. Name:    Car Fleet
#   2. Does:    counts how many FLEETS (groups of cars) arrive at the destination; a car can never pass the
#               car ahead, so a faster car that catches up slows down and joins the fleet ahead
#   3. Input:   an integer target, a list position (where each car starts), a list speed (how fast each goes)
#   4. Output:  one integer, the number of fleets, e.g. target = 10, position = [4,1,0,7], speed = [2,2,1,1]
#               -> 3
#   5. Steps every time: say it in one sentence; name input and output with a tiny example;
#      ask "what do I need to remember?"; pick the tool; stage comments, then code;
#      trace a tricky input; say time and space; derive the "because" from the trace.
#   6. Algorithm (the five jobs):
#        1. PREPARE    -> cars = sorted(zip(position, speed), reverse=True)  (front car first),
#                         stack = [] (the arrival hours of the fleets so far, newest on top)
#        2. GO THROUGH -> for pos, spd in cars
#        3. UPDATE     -> hours = (target - pos) / spd
#        4. DECIDE     -> if stack == [] or hours > stack[-1]: it cannot catch the fleet ahead
#        5. UPDATE     -> stack.append(hours): a NEW fleet (otherwise it joins the fleet ahead: do nothing)
#        6. RETURN     -> return len(stack), after the loop
#
# Key question: what must I remember? The arrival hours of the fleets formed so far; the next car is only
# compared with the NEWEST one (the fleet directly ahead): a stack.
#   "cars can't pass / fleets / catches up and slows down" -> sort by position, then a stack of hours.
# Pattern: "the newest comes first, so a stack"; here the newest thing is the fleet directly ahead.
# ---------------------------------------------------------------

from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        stack = []
        for pos, spd in cars:
            hours = (target - pos) / spd
            if stack == [] or hours > stack[-1]:
                stack.append(hours)
        return len(stack)


# Trace for target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3] (his own trace, finished aloud):
#   sorted front to back: (10,2), (8,4), (5,1), (3,3), (0,1)
#   (10,2): hours = (12 - 10) / 2 = 1; stack empty, append                       stack [1]
#   (8,4):  hours = (12 - 8) / 4 = 1;  1 > 1 is False, joins the fleet ahead      stack [1]
#   (5,1):  hours = (12 - 5) / 1 = 7;  7 > 1, cannot catch it, new fleet, append  stack [1, 7]
#   (3,3):  hours = (12 - 3) / 3 = 3;  compare with the TOP (7): 3 > 7 is False,
#           it joins the 7 fleet, nothing appended                                 stack [1, 7]
#   (0,1):  hours = (12 - 0) / 1 = 12; 12 > 7, new fleet, append                  stack [1, 7, 12]
#   return len(stack) = 3
# Example 2 (target = 10, position = [4,1,0,7], speed = [2,2,1,1]): sorted (7,1), (4,2), (1,2), (0,1); hours
#   3, 3, 4.5, 10; stack [3] -> [3] (3 > 3 is False, joins) -> [3, 4.5] -> [3, 4.5, 10]; answer 3.
# Why compare only with the top: cars cannot pass, so a car is stuck behind the NEAREST fleet; if it cannot
#   catch that one it cannot catch any fleet further ahead. Equal hours = it reaches the finish together
#   with the fleet ahead, so it is the same fleet (> and not >=).
#
# Slips fixed today:
#   1. The problem COUNTS fleets (the number), not "the fleet of cars".
#   2. Misread a speed in a small variation (speed 1 instead of 2); the back car needing MORE hours than the
#      car ahead never catches up (two fleets).
#   3. Compared the 10-hour car with "both" earlier fleets: only with the newest (the top of the stack).
#   4. First code: for pair in cars with the full lists position and speed still in the formula; it must
#      be for pos, spd in cars and (target - pos) / spd (position vs value, again); = instead of ==; missing
#      colon on the if.
#   5. Trace: hours for (8,4) are (12 - 8) / 4 = 1 (not 4); the stack after (5,1) is [1, 7] (the 1 stays at
#      the bottom); for (3,3) compared "is it a new number" instead of with stack[-1] (7): 3 > 7 is False, so
#      it joins and the stack stays [1, 7]; the 3 never goes on the stack.
#   6. Complexity: first said both O(n); the sorted() costs O(n log n), and the stack can hold n numbers.
#   7. Loop names position, speed hide the two input lists (works because cars was built before the loop);
#      pos, spd is clearer.
#
# Complexity: time O(n log n): sorting the cars costs O(n log n) and the loop after it is O(n) (each car
#               handled once; compare, divide and append are one step each).
#             space O(n): the stack holds one number per fleet, up to n when every car is its own fleet
#               (each car needs more hours than the one ahead), and cars holds n pairs.
#
# I used X because Y (his own words, with cars and fleet fixed):
# "I used a stack of arrival hours after sorting the cars front to back because a car is only compared with
#  the most recent fleet, the top of the stack, not with the older ones: the newest fleet is the one directly
#  ahead of the next car."
# Model with the sort reason: "...because cars can't pass each other, so each car only depends on the fleet
#  directly ahead of it. That fleet is the newest on the stack, so I compare only with the top. Time is
#  O(n log n) for the sort and space is O(n) for the stack."
#
# Interview sentence (model):
# "I sort the cars by position from the front, work out each car's arrival hours, and keep a stack of the
#  fleets' hours. A car that needs more hours than the top cannot catch that fleet, so it starts a new one;
#  otherwise it joins it. The answer is the size of the stack. Time is O(n log n), space is O(n)."

if __name__ == "__main__":
    print(Solution().carFleet(10, [1, 4], [3, 2]))                    # 1
    print(Solution().carFleet(10, [4, 1, 0, 7], [2, 2, 1, 1]))        # 3
    print(Solution().carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3])) # 3
    print(Solution().carFleet(10, [3], [3]))                          # 1
    print(Solution().carFleet(100, [0, 2, 4], [4, 2, 1]))             # 1
    print(Solution().carFleet(10, [0, 4, 2], [2, 1, 3]))              # 1

# Next: Tue Nov 24: the next stack problem (Largest Rectangle in Histogram is the hard one; or Generate
# Parentheses), the evening redo, and the 1-hour AWS Cloud Practitioner session (exam Sat Dec 5, 9:30).
