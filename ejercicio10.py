i=1

n = int(input("Digite el valor para num: "))
suma_notas=0
while i<=n:
    nota = float(input("Digite su nota {0}: ".format(i)))
    suma_notas += nota
    i+=1

print("El promedio total es: ", suma_notas/n)
