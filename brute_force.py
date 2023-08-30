from itertools import product

def evaluate_clause(clause, assignment):
    for var in clause:
        if var[0] == '~':
            if not assignment[var[1]]:
                return True
        else:
            if assignment[var]:
                return True
    return False

def is_satisfiable(clauses):
    variables = {var for clause in clauses for var in clause if var[0] != '~'}
    for values in product([True, False], repeat=len(variables)):
        assignment = dict(zip(variables, values))
        if all(evaluate_clause(clause, assignment) for clause in clauses):
            return True, assignment
    return False, {}
