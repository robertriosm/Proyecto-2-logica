from dpll import DPLL
from brute_force import *


print("\n################## BRUTE FORCE ##################\n")
test_cases_bruteforce = [
    [["A", "B"], ["B", "~C"], ["A", "C"]],  # Sat
    [["A", "B"], ["~A", "~B"], ["A", "~B"], ["~A", "B"]],  # Insat
    [["~A", "B"], ["A", "~B"]],  # Sat
    [["A", "~B"], ["B", "~C"], ["C", "~D"], ["D", "~A"]],  # Insat
    [["A"], ["~A"]],  # Insat
    [['A', 'B'], ['B', '~C'], ['A', 'C']]  # Sat
]

for formula in test_cases_bruteforce:
    result, assignment = is_sat(formula)
    if result:
        print(f"La fórmula es satisfacible. Asignación: {assignment}")
    else:
        print(f"La fórmula es insatisfacible. Asignación:{assignment}")




print("\n################## DPLL ##################\n")
formulas = [
    [{1}, {1}],
    [{2, 1, 1}],
    [{1, 2, 3}, {2, 1, 3}],
    [{1, 2}, {2, 3}, {1, 3}, {2, 3}],
    [{1, 2, 3}, {2, 3, 1}, {1, 2, 3}],
    [{3}, {2, 3}, {1, 2, 3}, {2}],
    [[1, 2], [2, -3], [1, 3]],  # Sat
    [[1, 2], [-1, -2], [1, -2], [-1, 2]],  # Insat
    [[-1, 2], [1, -2]],  # Sat
    [[1], [-1]] # Insat
]

print("Ejemplos de fórmulas:")
for formula in formulas:
    result, assignment = DPLL(formula, [])
    if result:
        print(f"La fórmula es satisfacible. Asignación: {assignment}")
    else:
        print(f"La fórmula es insatisfacible. Asignación:{assignment}")


