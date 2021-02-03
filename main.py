#Calculator

from art import logo

import sys

#add
def add(n1, n2):
  return n1 + n2

#subtract
def subtract(n1, n2):
  return n1 - n2

#multiply
def multiply(n1, n2):
  return n1 * n2

#divide
def divide(n1, n2):
  return n1 / n2

operations = {
  "+" :  add,
  "-" :  subtract,
  "*" :  multiply,
  "/" :  divide,
}

def calc ():
  print(logo)

  num1 = float(input("What's the first number: "))

  for symbol in operations:
    print(symbol)

  is_continue = True

  while is_continue:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number: "))
    cal_func = operations[operation_symbol] 
    answer = cal_func(num1,num2)

    print(f"{num1} {operation_symbol} {num2} = {answer}")
    
    choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start new calculation or 'e' to exit. : ")
    if choice == 'y':
      num1 = answer
      
    elif choice == 'n':
      is_continue = False
      calc()
    else:
      sys.exit()

calc()