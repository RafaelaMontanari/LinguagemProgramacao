r = int(input())
n = int(input())
contador = 1
soma = 1
while contador < n:
    contador = contador + r
    soma = soma + contador
print(f"A somatoria da PA eh: {soma}")
