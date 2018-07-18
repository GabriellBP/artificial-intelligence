import re
def solve_linear_equation ( equ ):
    if(re.match(r"(\d+)x\+(\d+)=(\d+)", equ)):
        match = re.match(r"(\d+)x\+(\d+)=(\d+)", equ)
        m, c, y = match.groups()
        m, c, y = float(m), float(c), float(y) # Convert from strings to numbers
        x = (y-c)/m
        print("x = %.2f" % x)
    else:
        print("falou")

def remove_spaces(string):
    string = string.replace(" ", '')
    return string


# receives 2x+5=4x and transforms into ['2','*','x','+','5','=','4','*','x']
def separate_variables(string):
    string = [i for i in re.split(r'([\d.]+|\W+)', string) if i]
    i = 0
    while i < len(string) - 1:
        if re.match(r'([a-zA-Z])', string[i + 1]):
            string = string[:i + 1] + list("*") + string[i + 1:]
            i += 1
        i += 1
    return string


def parsing(string):
    tokens = separate_variables(string)
    for i in range(0, len(tokens)):
        print(tokens[i])


eq = "2x + 5 - 3x * 4 + 5 = 3 * 2 - 3x + 4 "
eq = remove_spaces(eq)
eq = eq.split('=')
before_equals_eq = eq[0]
after_equals_eq = eq[1]
parsing(before_equals_eq)


solve_linear_equation("2x+4=-12")