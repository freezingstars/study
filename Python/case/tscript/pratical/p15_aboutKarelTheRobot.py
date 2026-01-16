"""
Karel the robot starts in the corner of an n by n square for some unknown number n. Karel responds to only four functions:

move() moves Karel one square forward if there is no wall in front of Karel and errors if there is.
turn_left() turns Karel 90 degrees to the left.
front_is_blocked() returns whether there is a wall in front of Karel.
front_is_clear() returns whether there is no wall in front of Karel.
Implement a main() function that will leave Karel stopped halfway in the middle of the bottom row. For example, if the square is 7 x 7 and Karel starts in position (1, 1), the bottom left, then Karel should end in position (1, 4) (three steps from either side on the bottom row). Karel can be facing in any direction at the end. If the bottom row length is even, Karel can stop in either position (1, n // 2) or (1, n // 2 + 1).

Important You can only write if or if/else statements and function calls in the body of main(). You may not write assignment statements, def statements, lambda expressions, or while/for statements.
"""

# from karel.stanfordkarel import *
# 
# def main():
#     to_middle()
#
# def to_middle():
#     if front_is_clear():
#        move()
#        if front_is_clear():
#          move()
#     if front_is_clear():
#        to_middle()
#     else:
#        turn_left()
#        turn_left()
#     move()