#Learning Function with Outputs (return command)
def format_name(first, last):
  first = first.capitalize()
  last = last.capitalize()
  full = first + " " + last
  return full

full_name = format_name("shaypher", "ashe")
print(full_name)
