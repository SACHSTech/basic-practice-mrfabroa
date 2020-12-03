'''
-------------------------------------------------------------------------------
Name:		cake_jog.py
Purpose:	A piece of cake contains about 225 calories . Jogging one 1 km uses about 100 calories. 
Write a program cake_jog.py that ask how many pieces of cake you have eaten and tells you 
how far you must jog to burn up the calories.

Author:	Fabroa.E

Created:	date in 03/12/2020
------------------------------------------------------------------------------
'''

# Welcome message and get number of pieces of cake
print("******* Welcome to the Cake Burner App ******")
pieces = int(input("Enter the number of pieces of cake: "))

# compute distance
calories = pieces * 225
distance = calories/100

# show result
print("You need to jog " +str(distance) +"km to burn off " + str(calories) + " calories from eating " + str(pieces) +  " piece(s) of cake.")


