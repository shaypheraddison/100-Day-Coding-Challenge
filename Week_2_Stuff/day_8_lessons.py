#Creating a simple function
def greet():
  print("Hello.")
  print("How are you?")
  print("Isn't it nice out toady?")

greet()

#Creating a fuunction with input inside the parenthsis
def greet_with_name(name):   #name = PARAMETER
  print(f"Hello {name}.")
  print(f"How are you {name}?")
  print("Isn't it nice out toady?")

greet_with_name("Jeff")  #"Jeff" = ARGUMENT

#Creating a function with multiple arguments
def greet_with(name, location):
  print(f"Hello {name}!")
  print(f"How is it in {location}?")

greet_with(location=Texas, name=Lee)
