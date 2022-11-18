#Add
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
'+' : add,
'-' : subtract,
'*' : multiply,
'/' : divide
 }

#Program starting point(first calculation)
first_number = int(input("What is your first number?: "))
for symbol in operations:
    print(symbol)

#Right symbol enterence filter
picked_operation_right = False
picked_operation = None
while not picked_operation_right:
    picked_operation = input("Pick your operation: ")
    if picked_operation == "+" or picked_operation == "-" or picked_operation == "*" or picked_operation == "/":
       picked_operation_right = True
    else:
        print("Wrong symbol")
        
#Second number        
second_number = int(input("What is your second number?: "))

# First Calculation algorythm
calculation_function = operations[picked_operation]
answer = calculation_function(first_number, second_number)
print(f"{first_number} {picked_operation} {second_number} = {answer}")

#Second calculation part 
stop_calculating = False
while not stop_calculating:
    continue_calculation = input("Do you wanna keep calculating? y or n: ")
    if continue_calculation == "y":
    #   picked_operation = str(input("Pick another operation: "))
      for symbol in operations:
        print(symbol)

      #Right symbol enterence filter
      picked_operation_right = False
      picked_operation = None
      while not picked_operation_right:
        picked_operation = str(input("Pick your operation: "))
        if picked_operation == "+" or picked_operation == "-" or picked_operation == "*" or picked_operation == "/":
           picked_operation_right = True
        else:
           print("Wrong symbol")

      #Third number input
      third_number = int(input("What's next number?: "))
      calculation_function = operations[picked_operation]
      second_answer = calculation_function(calculation_function(first_number, second_number), third_number)

      print(f"{answer} {picked_operation} {third_number} = {second_answer} ")
    if continue_calculation == "n":
        stop_calculating = True