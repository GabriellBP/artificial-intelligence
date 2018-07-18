OPERATIONS = ['*', '/', '+', '-']
#
# class SyntacticTree:
#     def __init__(self, left=None, right=None, element=None):
#         self.left = left
#         self.right = right
#         self.element = element
#
# def create_tree(equation):
#     root = SyntacticTree()
#     for e in equation:
#         if (e in OPERATIONS):
#         node = SyntacticTree(element=e)
#
#
#
# create_tree("5*x+5-30")

# def create_tree(equation):
#     tree = []
#     for e in equation:
#         if len(tree) == 0:
#             if e not in OPERATIONS:
#                 tree.append(float(e))
#             else:
#                 tree.append(float(e))
#         elif
#     print(tree)

# limpar left e right quando entra dentro de actual
def create_tree(equation):
    tree = []
    actual = tree
    left = ""
    # actual.append(5)
    # actual.append([])
    # actual = tree[1]
    # actual.append(3)
    # actual.append(5)
    for e in range(len(equation)):
        if (equation[e] in OPERATIONS) and e != 0:
            actual.append(equation[e])
            aux = [left]
            actual.append(aux)
            actual = aux
            left = ""
        else:
            left += equation[e]
        print(actual)
    print(tree)

create_tree("5*x+5-30")