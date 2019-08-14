# ============================================================
#
# Student Name (as it appears on cuLearn): Long Nguyen
# Student ID (9 digits in angle brackets): <101081666>
# Course Code (for this current semester): COMP1405B
#
# ============================================================

from comp1405_f17_assistant_a4 import *

hat = ask_question("Does your character wear a hat?").upper()
if hat == "YES" :
	hair = ask_question("Does your character have hair?").upper()
	if hair == "YES" :
		glasses = ask_question("Does your character wear glasses?").upper()
		if glasses == "YES" :
			pipe = ask_question("Does your character have a pipe?").upper()
			if pipe == "YES" :
				make_a_guess("Reed")
			else : 
				make_a_guess("Kendall")
		else:
			make_a_guess("Taylor")
	else:
		tattoo = ask_question("Does your character have a tattoo?").upper()
		if tattoo == "YES" :
			pipe = ask_question("Does your character have a pipe?").upper()
			if pipe == "YES" :
				glasses = ask_question("Does your character wear glasses?").upper()
				if glasses == "YES" :
					moustache = ask_question("Does your character have a moustache?").upper()
					if moustache == "YES" :
						make_a_guess("Landry")
					else : 
						make_a_guess("Bobbie")
				else : 
					eyepatch = ask_question("Does your character wear an eyepatch?").upper()
					if eyepatch == "YES" :
						make_a_guess("Ash")
					else: 
						make_a_guess("Dylan")
			else:
				earring = ask_question("Does your character have an earring?").upper()
				if earring == "YES":
					make_a_guess("Campbell")
				else:
					make_a_guess("Aiden")
		else:
			bowtie = ask_question("Does your character wear a bowtie?").upper()
			if bowtie == "YES":
				make_a_guess("Skylar")
			else:
				make_a_guess("Jayden")
else:
	glasses = ask_question("Does your character wear glasses?").upper()
	if glasses == "YES":
		pipe = ask_question("Does your character have a pipe?").upper()
		if pipe == "YES":
			make_a_guess("Eddie")
		else:
			make_a_guess("Frances")
	else:
		tattoo = ask_question("Does your character have a tattoo?").upper()
		if tattoo == "YES" :
			make_a_guess("Gray")
		else:
			moustache = ask_question("Does your character have a moustache?").upper()
			if moustache == "YES":
				make_a_guess("Adrian")
			else:
				make_a_guess("Jordan")


					
				
						
	
