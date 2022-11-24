##calculator##
while True:
    #enter 
    num_1 = input("enter frist number: ")
    num_2 = input("enter second number: ")
    operator = input("enter you operator (+,-,*,/): ") 
    # number verification 
    valid_num = None
    num_1_float = 0
    num_2_float = 0
    try:
        num_1_float = float(num_1)
        num_2_float = float(num_2)
        valid_num = True
        
    except: 
        valid_num = None

    if valid_num is None:
        print("Number is not valid")
        continue 
    
    #operator verification 

    operator_true = "+-*/"

    if operator not in operator_true:
        print("Operators is not valid")
        continue 
    if len(operator) > 1:
        print("Only one operator")
        continue 
    

    #calculation
    print("calculating...")
    if operator == "+":
        print(num_1_float + num_2_float)
    elif operator == "-":
        print(num_1_float - num_2_float)
    elif operator == "*":
        print(num_1_float * num_2_float)
    elif operator == "/":
        print(num_1_float / num_2_float)
    

    #out 
    out = input("wanna go out ? [s]")
    out = out.lower().startswith("s")

    if out is True:
        break

