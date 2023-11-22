#This was taught during DAY 2 of the 100 day coding challenge
#making a simple BMI calculator

weight = input()
height = input()

weight_in_kg = int(weight)
height_in_meters = float(height)

print(int(weight_in_kg / (height_in_meters ** 2)))

#wanting to print BMI as a whole number
