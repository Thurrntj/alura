qnt_alunos = int(input("digite a quantidade de alunos"))
qnt_monitores = int(input("digite a quantidade de monitores"))
qnt_convidados = int(input("digite a quantidade de convidados"))

total = qnt_alunos + qnt_monitores + qnt_convidados

if total > 100:
    print("Excedeu o número de ingressos.")
elif qnt_convidados > 20:
    print("Número de convidados acima do limite.")
else:
    print("Tudo certo, evento pode acontecer.")
