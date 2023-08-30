def DPLL(B, I):
    if not B:
        return True, I

    if any(clause == [] for clause in B):
        return False, None
    
    for clause in B:
        for literal in clause:
            if literal not in I and -literal not in I:
                L = literal
                break

    B_true = [clause for clause in B if L not in clause]
    B_true = [list(filter(lambda x: x != -L, clause)) for clause in B_true]
    I_true = I + [L]
    result_true, I1 = DPLL(B_true, I_true)

    if result_true:
        return True, I1

    B_false = [clause for clause in B if -L not in clause]
    B_false = [list(filter(lambda x: x != L, clause)) for clause in B_false]
    I_false = I + [-L]
    result_false, I2 = DPLL(B_false, I_false)

    if result_false:
        return True, I2

    return False, None
