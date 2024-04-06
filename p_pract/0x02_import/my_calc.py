#!/usr/bin/python3

if __name__ == "__main__":
    
    import sys
    import fun_calc

    if len(sys.argv) != 4:
        print("Usage: ./my_calc.py <a> <operator> <b>\n")
    else:
        r_value = 0
        a_value = int(sys.argv[1])
        b_value = int(sys.argv[3])
        if sys.argv[2] == "+":
            result = fun_calc.add(a_value, b_value)
        elif sys.argv[2] == "-":
            result = fun_calc.sub(a_value, b_value)
        elif sys.argv[2] == "*":
            result = fun_calc.mul(a_value, b_value)
        elif sys.argv[2] == "/":
            result = fun_calc.div(a_value, b_value)
        else:
            print("Unknown operator. Available operators: +, -, * and /\n")
            r_value = 1
        if r_value != 1:
            print(f"{a_value} {sys.argv[2]} {b_value} = {result}")