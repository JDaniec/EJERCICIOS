print("-------Multiplos de 7 entre 1000 y 5000")
print("---------------------------------------")
print("---------------------------------------")
#input
MUltiplos_de_7 = 0
MUltiplos_de_9 = 0
#Processing
for i in range(1000,5000):
    if i%7 == 0:
        MUltiplos_de_7 = MUltiplos_de_7 + 1
print("Entre 1000 y 5000 hay " + str(MUltiplos_de_7) + " multiplos de 7")

for i in range(1000,5000):
    if i%9 == 0:
        MUltiplos_de_9 = MUltiplos_de_9 + 1
print("Entre 1000 y 5000 hay " + str(MUltiplos_de_9) + " multiplos de 9")


