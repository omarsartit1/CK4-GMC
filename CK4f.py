def calculator():    
    while True : 
        try:   
            num1= float(input("enter your number :"))
            operator = input("enter operation type :")
            num2= float(input("enter your number :"))
            
            if   operator == "+":
                result = num1 + num2
                return result
            elif operator == "-":
                result = num1 - num2
                return result
            elif operator == "*":
                result = num1 * num2
                return result
            elif operator == "/":
                if num2 == 0 :
                    print("Error, division by 0 is impossible")
                else :
                    result = num1 / num2
                    return result
            else :
                    print("error, please enter a valid operation, try again")
        except ValueError : 
            print("error, please enter a numeric value")
            
result = calculator()
print("the result is", result)    


calculator ()