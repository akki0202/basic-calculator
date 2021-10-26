#Calculator
import art
def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}
def calc(num1,num2):
  num1 = float(input("What's the first number?: "))
  for symbol in operations:
    print(symbol)

  #Here we select "+"
  operation_symbol = input("Pick an operation: ") 
  num2 = float(input("What's the next number?: "))
  calculation_function = operations[operation_symbol]
  first_answer = calculation_function(num1, num2)

  print(f"{num1} {operation_symbol} {num2} = {first_answer}")
  ans=input(f"Type y to continue calculating with {first_answer} else type n: ")
  return first_answer
ans = "y" 
print(art.logo)
num1 = float(input("What's the first number?: "))
for symbol in operations:
  print(symbol)

#Here we select "+"
operation_symbol = input("Pick an operation: ") 
num2 = float(input("What's the next number?: "))
calculation_function = operations[operation_symbol]
first_answer = calculation_function(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {first_answer}")
ans=input(f"Type y to continue calculating with {first_answer} else type n: ")
while ans == "y":
  a= first_answer
  num1 = a
  for symbol in operations:
    print(symbol)

  #Here we select "+"
  operation_symbol = input("Pick an operation: ") 
  num2 = float(input("What's the next number?: "))
  calculation_function = operations[operation_symbol]
  first_answer = calculation_function(num1, num2)

  print(f"{num1} {operation_symbol} {num2} = {first_answer}")
  ans=input(f"Type y to continue calculating with {first_answer} else type n: ")
if ans == "n":
  calc(num1,num2)  


  
  