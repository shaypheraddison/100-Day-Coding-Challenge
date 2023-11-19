#This was taught during DAY 2 of the 100 day coding challenge
#Making a calculator to see how many weeks you have left until you reach 90 years old
age = input()
age_in_weeks = int(age) * 52
weeks_at_90 = 90 * 52
total_weeks_left = weeks_at_90 - int(age_in_weeks)



print(f"You have {total_weeks_left} weeks left.")