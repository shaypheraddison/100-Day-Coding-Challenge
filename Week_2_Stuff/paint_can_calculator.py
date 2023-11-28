#This will take the area of a wall, divide it by the coverage of the paint can and determine how many cans of paint is needed for a specific area.
def paint_calc(height, width, cover):
  cans_math = int(height * width) / coverage
  number_of_cans = round(cans_math + 0.5)
  print(f"You'll need {number_of_cans} cans of paint.")

#Lines 8-10 were code given by the lesson
test_h = int(input()) # Height of wall (m)
test_w = int(input()) # Width of wall (m)
coverage = 5

paint_calc(height=test_h, width=test_w, cover=coverage)
