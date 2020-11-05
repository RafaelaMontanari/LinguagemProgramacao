n = int(input())
soma = 0
for i in range(1,n+1):
    if i%2 != 0:
        soma = soma - (1/i)
    else:
        soma = soma + (1/i)
print(f'{soma:.6f}')