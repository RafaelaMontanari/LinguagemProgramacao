salario = float(input())
if salario <= 1751.81:
    desconto = salario * 0.08
elif 1751.82 <= salario <= 2919.72:
    desconto = salario * 0.09
elif 2919.73 <= salario <= 5839.45:
    desconto = salario * 0.11
else:
    desconto = 5839.45 * 0.11
print(f"Desconto do INSS: R$ {desconto:.2f}")
