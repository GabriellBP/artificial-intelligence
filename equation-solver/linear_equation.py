def solve_linear_equation(eq):
    print("solving a equation")


def main():
    equations = ["0 = 1 + 1x + 1x + 2", "1x = -1", "(1x+5)=-5", "((1+2)/2)*2+1x=1707", "((1+2)/2)*2+5*x/50=1707",
                 "(-1x)+5=(1x+2x)*-2*10/5*2+(2*(1+1*(5*0)))"]
    for eq in equations:
        solve_linear_equation(eq)
    # eq = input()
    # solve_linear_equation(eq)


if __name__ == '__main__':
    main()
