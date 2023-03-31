def contar_divisores(n):
    contador = 0
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            if n/i == i:
                contador += 1
            else:
                contador += 2
    return contador

f1 = 1
f2 = 1
contador = 0

while contador  <= 1000:
    f1, f2 = f2, f1+f2
    contador = contar_divisores(f2)

print("El primer número de Fibonacci que tiene más de 1000 divisores es:", f2)
