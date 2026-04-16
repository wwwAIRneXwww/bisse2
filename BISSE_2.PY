def PowerA234(n):
    return n**2, n**3, n**4

# Sinov
A, B, C = 2.0, 3.0, 5.0
for s in [A, B, C]:
    d2, d3, d4 = PowerA234(s)
    print(f"{s} ning darajalari: kvadrat={d2}, kub={d3}, to'rtinchi={d4}")