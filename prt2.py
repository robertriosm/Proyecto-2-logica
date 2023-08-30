def DPLL(B, I):
    if not B:  # Si no quedan cláusulas, la fórmula es satisfacible
        return True, I

    if any(clause == [] for clause in B):  # Si hay alguna cláusula vacía, la fórmula es insatisfacible
        return False, None
    
    # Seleccionar una literal no asignada en la asignación parcial I
    for clause in B:
        for literal in clause:
            if literal not in I and -literal not in I:
                L = literal
                break

    # Intentar asignar L como verdadero
    B_true = [clause for clause in B if L not in clause]
    B_true = [list(filter(lambda x: x != -L, clause)) for clause in B_true]
    I_true = I + [L]
    result_true, I1 = DPLL(B_true, I_true)

    if result_true:
        return True, I1

    # Intentar asignar L como falso
    B_false = [clause for clause in B if -L not in clause]
    B_false = [list(filter(lambda x: x != L, clause)) for clause in B_false]
    I_false = I + [-L]
    result_false, I2 = DPLL(B_false, I_false)

    if result_false:
        return True, I2

    return False, None

# Ejemplo de uso
if __name__ == "__main__":
    formulas = [
        [{1}, {1}],
        [{2, 1, 1}],
        [{1, 2, 3}, {2, 1, 3}],
        [{1, 2}, {2, 3}, {1, 3}, {2, 3}],
        [{1, 2, 3}, {2, 3, 1}, {1, 2, 3}],
        [{3}, {2, 3}, {1, 2, 3}, {2}],
    ]

    print("\nEjemplo de fórmula insatisfacible:")
    unsatisfiable_formula = [[1], [-1]]  # Contiene una cláusula con p y su negación
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