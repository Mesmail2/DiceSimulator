#My name's Mohamed and this will be my implementation of a dice roller 
#for fun using the random module 

import random


user_input = "r"

while user_input == "r":

	dice = random.randint(1,6)

	if dice == 1:
		print("[-----]")
		print("[     ]")
		print("[  0  ]")
		print("[     ]")
		print("[-----]")
        if dice == 2:
		print("[-----]")
		print("[ 0   ]")
		print("[     ]")
		print("[   0 ]")
		print("[-----]")
	if dice == 3:
		print("[-----]")
		print("[     ]")
		print("[0 0 0]")
		print("[     ]")
		print("[-----]")
	if dice == 4:
		print("[-----]")
		print("[0   0]")
		print("[     ]")
		print("[0   0]")
		print("[-----]")
	if dice == 5:
		print("[-----]")
		print("[0   0]")
		print("[  0  ]")
		print("[0   0]")
		print("[-----]")
	if dice == 6:
		print("[-----]")
		print("[0 0 0]")
		print("[     ]")
		print("[0 0 0]")
		print("[-----]")
	user_input = input("Enter r to roll again and x to exit: ")
	print("\n")
