import random as rd


num = int(input("insira um número entre 0 e 100: "))
shot = 0
shots = []
minimum = 0
maximum = 100
aleat = rd.randint(minimum, maximum)

while (aleat != num):
    if aleat > num:
        maximum = aleat
        aleat = rd.randint(minimum+1, maximum-1)
        shot += 1
    elif aleat < num:
        minimum = aleat
        aleat = rd.randint(minimum+1, maximum-1)
        shot += 1
    shots.append(aleat)

print("o número foi acertado em {} tentativas".format(shot))
print("a máquina tentou os seguintes numeros: {}".format(shots))
