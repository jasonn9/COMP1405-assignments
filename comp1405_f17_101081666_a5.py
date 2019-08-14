# ============================================================
#
# Student Name (as it appears on cuLearn): Long Nguyen
# Student ID (9 digits in angle brackets): <101081666>
# Course Code (for this current semester): COMP1405B
#
# ============================================================

from comp1405_f17_assistant_a5 import *

for i in range(13):
	move_down()

for i in range (40):
	move_right()
	
num = True
while num == True:
	move_down()
	if what_number_am_i_standing_on() == 5:
		num = False
		break

while what_number_am_i_standing_on() != 4:
	move_left()

num = True
while num == True:
	move_down()
	if am_i_standing_on(5):
		num = False

for i in range(14):
	move_right()

while not am_i_standing_on(5):
	move_down()

num = True
while num == True:
	move_left()
	if am_i_standing_on(4):
		num = False
		break

num = True 
while num == True:
	move_down()
	if what_number_am_i_standing_on() == 5:
		num = False
	




