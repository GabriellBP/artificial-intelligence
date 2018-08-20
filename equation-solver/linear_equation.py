import re

    
def remove_spaces(string):
    string = string.replace(" ", '')
    return string


# receives 2x+5=4x and transforms into ['2','*','x','+','5','=','4','*','x']
def separate_variables(string):
    string = [i for i in re.split(r'([\d.]+|\W+)', string) if i]
    i = 0
    while i < len(string) - 1:
        if re.match(r'([a-zA-Z])', string[i + 1]) and not re.match(r'(\W+)', string[i]):
            string = string[:i + 1] + list("*") + string[i + 1:]
            i += 1
        i += 1
    string = ''.join(string)
    return string


def verify_op(regex, string, pos):
    for i in regex:
        # print(i, string[pos])
        if not re.match(i, string[pos]):
            return False
        pos += 1
    return True


# transforms 10*x+20*x+30*x to 10+20+30
def remove_var(string):
    # print(string)
    string = string.replace("*x", '')
    # print(string)
    return string


def remove_part(string, part):
    string = string.replace(part, '')
    return string


def resolve(string):
    # TODO
    print(string)


def parsing(eq):
    if "x" not in eq:
        return 0, eval(eq)
    eq = separate_variables(eq)
    regex_var = r"((?:\+|\-)?\d*(?:\*|\/)[a-zA-Z](?:(?:\/|\*)?\d+)*)"
    var_op = re.findall(regex_var, eq)
    var_op = ''.join(var_op)
    const_op = remove_part(eq, var_op)
    var_op = remove_var(var_op)
    var_value = eval(var_op)
    # regex_const = r"((?:\+|\-|\*|\/)?\d+)(?!(\d*)(\*|\/)[a-zA-Z])"
    # const_op = re.findall(regex_const, eq)
    if len(const_op) == 0:
        return var_value, 0
    # const_op = [i[0] for i in const_op]  # return a list of te first`s elements of list of tuple
    # const_op = ''.join(const_op)
    const_value = eval(const_op)
    return var_value, const_value


def solve_linear_equation(eq):
    eq = remove_spaces(eq)
    eq = eq.split('=')
    before_equals_eq = eq[0]
    after_equals_eq = eq[1]
    before_equals_var_value, before_equals_const_value = parsing(before_equals_eq)
    after_equals_var_value, after_equals_const_value = parsing(after_equals_eq)
    numerator = after_equals_const_value - before_equals_const_value
    denominator = before_equals_var_value - after_equals_var_value
    if denominator == 0:
        print("Erro: Coeficiente da variável é zero")
    else:
        result = numerator / denominator
        print("x =", result)


def main():
    equations = ["0 = 1 + 1x + 1x + 2", "1x = -1", "(1x+5)=-5", "((1+2)/2)*2+1x=1707", "((1+2)/2)*2+5*x/50=1707"]
    for eq in equations:
        solve_linear_equation(eq)
    # equation = input()
    # solve_linear_equation(equations)


if __name__ == '__main__':
    main()
