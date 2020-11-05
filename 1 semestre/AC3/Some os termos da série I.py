n = int(input())
soma = 0
for i in range(1,n+1):
    soma = soma + (1/(i**2))
print(f'{soma:.6f}')
