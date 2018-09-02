import re
import sys


def remove_var(string):
    string = string.replace("*x", '')
    return string


def remove_part(string, part, count=-1):
    string = string.replace(part, '', count)
    return string


def remove_spaces(string):
    string = string.replace(" ", '')
    return string


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


def error(description=-1):
    message = "Something is wrong! Error undefined."
    if description == 1:
        message = "Some operation is generating a non-linear equation"
    print("ERROR!\n" + message)
    sys.exit(message)


def make_distributive(eq, operation, parenthesis):
    # regex_var = r"((?:\+|\-)?\d*)(?=\*[a-zA-Z])"
    value = eq
    eq_var = False
    if "*x" in value:
        value = remove_var(value)
        eq_var = True
    parenthesis_parts = parenthesis.split("+")
    if len(parenthesis_parts) > 1:
        if eq_var:
            error(1)  # generating a non-linear equation
        parenthesis_parts[0] = remove_var(parenthesis_parts[0])
        if operation == "*":
            first = float(value) * float(parenthesis_parts[0])
            second = float(value) * float(parenthesis_parts[1])
        else:
            first = float(value) / float(parenthesis_parts[0])
            second = float(value) / float(parenthesis_parts[1])

        result = str(int(first)) + "*x" + str(int(second))
    else:
        parenthesis_parts = parenthesis_parts[0]
        if "*x" in parenthesis_parts:
            if eq_var:
                error(1)  # generating a non-linear equation
            parenthesis_parts = remove_var(parenthesis_parts)
            if operation == "*":
                aux = float(value) * float(parenthesis_parts)
            else:
                aux = float(value) / float(parenthesis_parts)
            result = str(int(aux)) + "*x"
        else:
            if operation == "*":
                aux = float(value) * float(parenthesis_parts)
            else:
                aux = float(value) / float(parenthesis_parts)
            if eq_var:
                result = str(int(aux)) + "*x"
            else:
                result = str(int(aux))
    return result


def simplify_expression(expression):
    regex_var = r"((?:(?:\+|\-)?\d*(?:\*|\/))+[a-zA-Z](?:(?:\/|\*)?\d+)*)"
    equation1 = expression.group(1)
    operation = expression.group(2)
    equation2 = expression.group(3)

    if "(" in equation1:
        const = equation1
        var = re.findall(regex_var, equation1)
        for i in var:
            const = remove_part(const, i)
        if const != '':
            const = eval(const)
            const = str(const)
        if len(var) != 0:
            var = ''.join(var)
            var = remove_var(var)
            var = eval(var)
            var = str(var)
            var = var + "*x"
        if len(var) != 0 and len(const) != 0:
            equation1 = var + "+" + const
        elif len(var) != 0:
            equation1 = var
        elif len(const) != 0:
            equation1 = const
        var = re.findall(regex_var, equation2)
        if len(var) != 0:
            temp = ''.join(var)
            temp = remove_var(temp)
            temp = eval(temp)
            temp = str(temp)
            temp = temp + "*x"
        else:
            temp = eval(equation2)
            temp = str(temp)
        equation2 = temp
        equation = make_distributive(equation2, operation, equation1)
    else:
        const = equation2
        var = re.findall(regex_var, equation2)
        for i in var:
            const = remove_part(const, i)
        if len(const) != 0:
            const = eval(const)
            const = str(const)
        if len(var) != 0:
            var = ''.join(var)
            var = remove_var(var)
            var = eval(var)
            var = str(var)
            var = var + "*x"
        if len(var) != 0 and len(const) != 0:
            equation2 = var + "+" + const
        elif len(var) != 0:
            equation2 = var
        elif len(const) != 0:
            equation2 = const
        var = re.findall(regex_var, equation1)
        if len(var) != 0:
            temp = ''.join(var)
            temp = remove_var(temp)
            temp = eval(temp)
            temp = str(temp)
            temp = temp + "*x"
        else:
            temp = eval(equation1)
            temp = str(temp)
        equation1 = temp
        equation = make_distributive(equation1, operation, equation2)

    return equation


def solve_parentheses(eq):
    regex_right_parentheses = r"(\-?(?:\d*\*[a-zA-Z](?:(?:\/|\*(?:\-)?)?\d+)*)*(?:(?:\*|\/(?:\-)?)?\d+)*)(\*|\/)(\((" \
                              r"?:(?:\+|\-)?\d*\*[a-zA-Z](?:(?:\/|\*(?:\-)?)?\d+)*)*(?:(?:\+|\-|\*|\/)?\d+)*\))"
    regex_left_parentheses = r"\(((?:(?:\+|\-)?\d*\*[a-zA-Z](?:(?:(?:\*|\/)(?:\-)?)?\d+)*)*(?:(" \
                             "?:\+|\-|\*|\/)?\d+)*)\)(\*|\/)((?:(?:(?:\-)?\d)*\*[a-zA-Z](?:(?:(?:\*|\/)(" \
                             "?:\-)?)?\d+)*)*(?:(?:\*|\/)?(?:\-)?\d+)*)"

    while True:
        eq_sub = re.sub(regex_right_parentheses, simplify_expression, eq)
        if eq_sub == eq:
            break
        eq = eq_sub
    while True:
        eq_sub = re.sub(regex_left_parentheses, simplify_expression, eq)
        if eq_sub == eq:
            break
        eq = eq_sub

    eq = remove_part(eq, "(", 1)
    eq = remove_part(eq, ")", 1)
    return eq


def parsing(eq_left, eq_right):
    print("Before:", eq_left, "=", eq_right)
    eq_left = solve_parentheses(eq_left)
    eq_right = solve_parentheses(eq_right)
    print("After:", eq_left, "=", eq_right)


def solve_linear_equation(eq):
    eq = remove_spaces(eq)
    eq = separate_variables(eq)
    eq = eq.split('=')
    before_equals_eq = eq[0]
    after_equals_eq = eq[1]
    parsing(before_equals_eq, after_equals_eq)


def get_input():
    equations = ["0 = 1 + 1x + 1x + 2", "1x = -1", "(1x+5)=-5", "((2+2)/2)*2+1x=1707", "((2+2)/2)*2+5*x/50=1707",
                 "(-1x)+5=(1x+2x)*-2*10/5*2+(2*(1+1*(5*0)))"]
    print("1- Predefined input")
    print("2- Custom input")
    choice = int(input())
    while True:
        if choice == 1:
            return equations
        elif choice == 2:
            return [input()]
        else:
            print("Invalid choice")


def main():
    equations = get_input()
    for eq in equations:
        solve_linear_equation(eq)


if __name__ == '__main__':
    main()
