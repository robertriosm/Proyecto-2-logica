"""
Grupo 5.
Este archivo contiene la implementacion del algoritmo de fuerza bruta.
"""

from itertools import product

def evaluate_clause(clause: list[str], assignment: dict[str, bool]) -> bool:
    """
    Esta función toma una cláusula y una asignación de variables, y evalúa si la cláusula es verdadera bajo esa asignación.
    """
    for var in clause:
        if var[0] == '~':
            if not assignment[var[1]]:
                return True
        else:
            if assignment[var]:
                return True
    return False

def is_sat(clauses: list[list[str]]):
    """
    Esta función toma un conjunto de cláusulas y verifica si son satisfacibles utilizando fuerza bruta.
    """
    variables = {var for clause in clauses for var in clause if var[0] != '~'}
    for values in product([True, False], repeat=len(variables)):
        assignment = dict(zip(variables, values))
        if all(evaluate_clause(clause, assignment) for clause in clauses):
            return True, assignment
    return False, {}
