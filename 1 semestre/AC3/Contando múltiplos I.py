x = int(input())
n = int(input())
mult = 1
multiplo = 0
contador = 0
while multiplo < n:
    multiplo = x * mult
    mult = mult + 1
    if multiplo < n:
        contador = contador + 1
print(f"O numero {x} tem {contador} multiplos menores que {n}.")