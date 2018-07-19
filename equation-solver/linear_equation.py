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


def verify_op(regexs, string, pos):
    for i in regexs:
        print(i, string[pos])
        if not re.match(i, string[pos]):
            return False
        pos += 1
    return True


def testing(eq = "10*x+10+20*x+10*20+x/10+20*x-20"):
    print("equacao: ",eq)
    regex_var = r"((?:\+|\-)?\d*(?:\*|\/)[a-zA-Z])"
    var_op = re.findall(regex_var, eq)
    var_op = ''.join(var_op)
    print("operacoes das variaveis: ",var_op)
    regex_const = r"((?:\+|\-|\*|\/)?\d+)(?!(\d*)(\*|\/)[a-zA-Z])"
    const_op = re.findall(regex_const, eq)
    const_op = [i[0] for i in const_op] #return a list of te first`s elements of list of tuple
    const_op = ''.join(const_op)
    print("operacoes das constantes: ",const_op)


eq = "2x + 5 - 3x * 4 + 5 = 3 * 2 - 3x + 4 "
eq = remove_spaces(eq)
eq = eq.split('=')
before_equals_eq = eq[0]
after_equals_eq = eq[1]
testing()



