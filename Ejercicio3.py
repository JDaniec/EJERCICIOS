print("------------------Dados----------------")
print("---------------------------------------")
print("---------------------------------------")
import random

n = int(input("Digite el numero de lanzamientos del dado: "))

c1 = 0
c2 = 0
c3 = 0
c4 = 0
c5 = 0
c6 = 0

for i in range(n):
 
 cara = random.randint(1,6)

 if cara == 1:
  c1 = c1 + 1
  print("Cara 1" + "*" * c1 )
  
 elif cara == 2:
  c2 = c2 + 1
  print("Cara 2" + "*" * c2 )

 elif cara == 3:
  c3 = c3 + 1
  print("Cara 3" + "*" * c3 )

 elif cara == 4:
  c4 = c4 + 1
  print("Cara 4" + "*" * c4 )

 elif cara == 5:
  c5 = c5 + 1
  print("Cara 5" + "*" * c5 )

 elif cara == 6:
  c6 = c6 + 1
  print("Cara 6" + "*" * c6 )


  



 








  

 



 

