print("------------Cuantos numeros son impares e impares-----------")
print("------------------------------------------------------------")
print("------------------------------------------------------------")

#input
n = int(input("Digite el numero "))
Numeros_impares = 0
Numeros_pares = 0

#Processing

for i in range(1, n+1):
    if i%2 == 0:
        Numeros_pares +=1

    else:
        Numeros_impares +=1 
print("Hasta " + str(n) + " hay " + str(Numeros_impares) + " numeros impares ")
print("Hasta " + str(n) + " hay " + str(Numeros_pares) + " numeros pares ")
 

    


