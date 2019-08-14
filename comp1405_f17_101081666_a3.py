# ============================================================
#
# Student Name (as it appears on cuLearn): Long Nguyen
# Student ID (9 digits in angle brackets): <101081666>
# Course Code (for this current semester): COMP1405B
#
# ============================================================

from comp1405_f17_assistant_a3 import *

def decision_making_function(e):  # 'e' IS THE SHAPE ARGUMENT YOU MUST PASS TO YOUR PERMITTED FUNCTIONS

	condition_for_sending_down =  (painted_red(e) and is_shaped_like_a_circle(e)) or (painted_blue(e) and is_shaped_like_a_square(e))

	condition_for_sending_left = divides_evenly_by(e,3) and (painted_orange(e) or painted_black(e))

	condition_for_sending_right = (painted_orange(e) and is_shaped_like_a_square(e)) or (painted_black(e) and is_shaped_like_a_circle(e))
	
	return (condition_for_sending_down, condition_for_sending_left, condition_for_sending_right)

	
run_the_program(decision_making_function)
