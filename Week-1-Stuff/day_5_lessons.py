# Using ONLY FOR LOOPS to solve getting the avg height(in cm), total number of students in the input created list and to sum up the total height from the list

student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

sum_height = 0
for height in student_heights:
  sum_height += height

total_students = 0
for total in student_heights:
  total_students += 1

avg_height = int(round(sum_height / total_students))
  
print(f"total height = {sum_height}")
print(f"number of students = {total_students}")
print(f"average height = {avg_height}")

#Using ONLY FOR LOOPS to solve locating the highest number in a input list 

student_scores = input().split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
  
highest_score = 0
for score in student_scores:
  if score > highest_score:
    highest_score = score
print(f"The highest score in the class is: {highest_score}")
