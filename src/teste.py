import random as rd


num = int(input("tente descobrir um número entre 0 e 100: "))
shot = 1
shots = []

aleat = rd.randint(0, 100)

while num != aleat:
    if num > aleat:
        print("menor")
        num = int(input("tente descobrir um número entre 0 e 100: "))
        shot += 1
    elif num < aleat:
        print("maior")
        num = int(input("tente descobrir um número entre 0 e 100: "))
        shot += 1
    shots.append(num)

print("acertou o número em {} tentativas".format(shot))
print("você tentou os seguintes numeros: {}".format(shots))
