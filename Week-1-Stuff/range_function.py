#Using for loops to assist with range function

#The lesson here is to take the input and get the sum only even numbers of the range of the input
target = int(input()) # Enter a number between 0 and 1000

new_target = target + 1
for number in range(0, new_target, 2):
  total += number
print(total)
