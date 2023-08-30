from prt2 import DPLL

formulas = [
    [{1}, {1}],
    [{2, 1, 1}],
    [{1, 2, 3}, {2, 1, 3}],
    [{1, 2}, {2, 3}, {1, 3}, {2, 3}],
    [{1, 2, 3}, {2, 3, 1}, {1, 2, 3}],
    [{3}, {2, 3}, {1, 2, 3}, {2}],
]

print("\nEjemplo de fórmula insatisfacible:")
unsatisfiable_formula = [[1], [-1]]
result, assignment = DPLL(unsatisfiable_formula, [])

if result:
    print("La fórmula es satisfacible. Asignación:", assignment)
else:
    print("La fórmula es insatisfacible.")

print("\nEjemplos de fórmulas:")

for i, formula in enumerate(formulas):
    result, assignment = DPLL(formula, [])
    print(f"Fórmula {i + 1}:")
    if result:
        print("La fórmula es satisfacible. Asignación:", assignment)
    else:
        print("La fórmula es insatisfacible.")