import re

    
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
    string = ''.join(string)
    return string


def verify_op(regex, string, pos):
    for i in regex:
        print(i, string[pos])
        if not re.match(i, string[pos]):
            return False
        pos += 1
    return True


# transforms 10*x+20*x+30*x to 10+20+30
def remove_var(string):
    print(string)
    string = string.replace("*x", '')
    print(string)
    return string


def resolve(string):
    # TODO
    print(string)


def parsing(eq):
    eq = separate_variables(eq)
    regex_var = r"((?:\+|\-)?\d*(?:\*|\/)[a-zA-Z])"
    var_op = re.findall(regex_var, eq)
    var_op = ''.join(var_op)
    var_op = remove_var(var_op)
    var_value = eval(var_op)
    regex_const = r"((?:\+|\-|\*|\/)?\d+)(?!(\d*)(\*|\/)[a-zA-Z])"
    const_op = re.findall(regex_const, eq)
    const_op = [i[0] for i in const_op]  # return a list of te first`s elements of list of tuple
    const_op = ''.join(const_op)
    const_value = eval(const_op)
    return var_value, const_value


def solve_linear_equation(eq):
    eq = remove_spaces(eq)
    eq = eq.split('=')
    before_equals_eq = eq[0]
    after_equals_eq = eq[1]
    before_equals_var_value, before_equals_const_value = parsing(before_equals_eq)
    after_equals_var_value, after_equals_const_value = parsing(after_equals_eq)
    parsing(before_equals_eq)
    result = (after_equals_const_value - before_equals_const_value) / (before_equals_var_value - after_equals_var_value)
    print("x =", result)


def main():
    equation = "2x + 5 - 3x + 4 * 5 = 3 * 2 - 3x + 4"
    solve_linear_equation(equation)


if __name__ == '__main__':
    main()
