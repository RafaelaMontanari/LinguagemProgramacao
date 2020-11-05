nota1 = float(input())
nota2 = float(input())
nota3 = float(input())
frequencia = float(input())

frequenciaFinal = int(frequencia*100)
media = ((nota1*2) + (nota2*2) + (nota3*3))/7
mediaFinal = round(media,1)

print(f"Frequencia: {frequenciaFinal}%")
print(f"Media: {mediaFinal}")
if frequenciaFinal < 75:
    print("Aluno reprovado por faltas!")
else:
    if mediaFinal > 9:
        print("Aluno aprovado com louvor!")
    elif mediaFinal >= 6:
        print("Aluno aprovado!")
    elif mediaFinal >= 4:
        print("Aluno de rec!")
    else: 
        print("Aluno reprovado!")
