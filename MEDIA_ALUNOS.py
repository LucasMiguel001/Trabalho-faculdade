def calcular_media(notas):
    total = sum(notas)
    media = total / len(notas)
    return media

def verificar_aprovacao(media):
    if media >= 6.0:
        return "Aprovado"
    else:
        return "Reprovado"

def main():
    notas = []
    while True:
        nota_str = input("Digite a nota do aluno (ou digite 'fim' para terminar): ")
        if nota_str.lower() == 'fim':
            break
        nota = float(nota_str)
        notas.append(nota)

    if len(notas) == 0:
        print("Nenhuma nota foi inserida.")
    else:
        media = calcular_media(notas)
        situacao = verificar_aprovacao(media)
        print(f"A média do aluno é {media:.2f}. Situação: {situacao}")

if __name__ == "__main__":
    main()