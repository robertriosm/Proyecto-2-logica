"""
Grupo 5.
Este archivo contiene la implementacion del algoritmo de DPLL (Davis-Putnam-Logemann-Loveland).
"""

def DPLL(B: list[int], I: list[int]):
    """
    Implementacion del algoritmo DPLL para determinar la satisfacibilidad de una fórmula booleana.
    
    1. Si B es vacía, entonces regresar True e I.
    2. Si hay alguna disyunción vacía en B, entonces regresar False y asignación vacía o nula.
    3. L => seleccionar literal(B)
    4. Elimina todas las cláusulas que contienen la literal L en B y elimina las ocurrencias en las cláusulas 
       de la literal complementaria de L en B, construyendo B' I' = I U {valor de L es verdadero}
    5. Resultado e I1 => DPLL(B', I')
    6. Si el resultado es verdadero, entonces regresar True e I1.
    7. Elimina todas las cláusulas que contienen la literal complementaria L en B y elimina las ocurrencias en las cláusulas de la literal L en B, construyendo B'.
    5. Resultado e I1 => DPLL(B', I')
    6. Si el resultado es verdadero, entonces regresar True e I1.
    7. I' = I U {valor de L es falso}
    8. Resultado e I2 => DPLL(B', I')
    9. Si el resultado es verdadero, entonces regresar True e I2.
    10. Regresar False y la asignación vacía o nula.
    """

    if not B:
        return True, I

    if any(clausula == [] for clausula in B):
        return False, None
    
    for clausula in B:
        for literal in clausula:
            if literal not in I and -literal not in I:
                L = literal
                break

    B_true = [clausula for clausula in B if L not in clausula]
    B_true = [list(filter(lambda x: x != -L, clausula)) for clausula in B_true]
    I_true = I + [L]
    result_true, I1 = DPLL(B_true, I_true)

    if result_true:
        return True, I1

    B_false = [clausula for clausula in B if -L not in clausula]
    B_false = [list(filter(lambda x: x != L, clausula)) for clausula in B_false]
    I_false = I + [-L]
    result_false, I2 = DPLL(B_false, I_false)

    if result_false:
        return True, I2

    return False, None
