'''
-------------------------------------------------------------------------------
Name:		oz_to_ml.py
Purpose:	A recipe website lists all fluid amounts in ounces, however, your kitchen 
is only equipped with measuring cups in millilitres(ml). The website also list recipes 
based on serving 4 people. Write a program that will get the amount of a fluid 
in a recipe in ounces as well as the number of servings that you want cook for. 
Considering the number of servings, the program will output the proper amount 
in millilitres.

Author:	Fabroa.E

Created:	date in 03/12/2020
------------------------------------------------------------------------------
'''

print("****** Welcome to the Oz to ml Converter *****")

# get ounces and servings
ounces = float(input("Enter the amount of fluid in ounces: "))
servings = int(input("Enter the number of people to serve: "))


# compute millilitres
ml = (ounces * 29.5735) * servings/4

# output millilitres
print("\nYou will need", ml, "ml")
