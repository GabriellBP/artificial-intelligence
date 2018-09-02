import os


def clear():
    if os.name in ('nt', 'dos'):
        os.system("cls")
    elif os.name in ('linux', 'osx', 'posix'):
        os.system("clear")
    else:
        print("\n" * 120)
    # os.system('cls' if os.name == 'nt' else 'clear')


def main():
    print("obs.:For negatives use '!' like !B\n")
    knowledge_base = {}
    rules = {}

    while True:
        print("Enter the knowledge base:")
        while True:
            a = input("The element:")
            b = input("The value:")
            knowledge_base[a] = bool(b)
            choice = int(input("Any more element? 1-Yes 2-No"))
            if choice == 2:
                break
                
        print("Enter the production rules:")
        while True:
            c = input("The consequence:")
            rules[c] = []
            print("Insert the clauses conditions separate by enters: \n    -1 to stop")
            while True:
                cc = input()
                if cc == "-1":
                    break
                rules[c].append(cc)
            choice = int(input("Any more rule? 1-Yes 2-No"))
            if choice == 2:
                break

        print("What kind of method do you want?")
        print("1- Forward chaining")
        print("2- Backward  chaining")
        print("3- Hybrid")
        choice = int(input())

        if choice == 1:
            print("Not yet implemented")
        elif choice == 2:
            print("Not yet implemented")
        elif choice == 3:
            print("Not yet implemented")
        else:
            print("Invalid choice!")
        print("Do you want to try again? 1-Yes 2-No")
        choice = int(input())
        if choice == 1:
            clear()
            continue
        else:
            break


if __name__ == '__main__':
    main()
