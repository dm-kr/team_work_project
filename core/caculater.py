def cacul():
    print ("oper: +,-,*,/")

    number = float(input("Ввод числа 1:  "))

    oper = input("выбери че надо:  ")

    number_two = float(input("Ввод числа 2: ")) 

    if oper == "+":
        result = number + number_two
    elif oper == "-":
        result = number - number_two
    elif oper == "*":
        result = number * number_two
    elif oper == "/":
        result = number / number_two
    else:
        print("не то")
        return
    
    see_result(result, oper, number, number_two)

def see_result(result, oper, number, number_two):
    print(f"{number} {oper} {number_two} = {result}")


cacul()

