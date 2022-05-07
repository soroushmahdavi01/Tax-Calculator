#Tip Calculator

tip = input("Enter Tip Percentage: ") 
tip = float(tip) / 100 

price = input("Enter Price: ")

tip_not_rounded = float(price) * tip
#I didnt want it to continue off if it divided by 3
tip_total = round(tip_not_rounded, 2)

not_rounded_total = float(price) + float(tip_total)

total = round (not_rounded_total, 2)



print("Based on a " + str(round(tip, 4)) + "% tip with a price of $" + str(price) + " the tip comes down to $" + str(tip_total) + ", for a total of $" + str(total))
#Need to get rid of it calling it 0.121
