# -*- coding: utf-8 -*-
"""
@author:     JorgeZaldivar
Fecha:       Sun Nov 17 22:59:01 2019
Descripción: Concurso O19
             I - Separador de residuos
"""

S = input()
R = {"1": 0, "2": 0, "3": 0, "4": 0, "X": 0}
for c in S:
    if c in "1234":
        R[c] += 1
    else:
        R["X"] += 1
r = [str(R[c]) for c in "1234X"]
r = " ".join(r)
print(r)
    