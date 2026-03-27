numero_secreto = 7

for tentativa in range(5):
    palpite = int(input("Tente adivinhar o número: "))

    if palpite == numero_secreto:
        print("Parabéns")
        break
    elif palpite > numero_secreto:
        print("O número é menor")
    else:
        print("O número é maior")
else:
    print(f"Você perdeu! O número era {numero_secreto}")
