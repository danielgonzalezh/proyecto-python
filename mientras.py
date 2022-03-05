#importar libreria(recetas/codigos prefabricados)
import math

#declaro el bucle/ciclo /iteracion/repeticion/la vuelta/loop

print("Empanadas el machetico")
print("***")
print("0. Digita 0 para salir")
print("1. Digita 1 para calcular la raiz cuadrada de un #")
print("2. Digita 2 para calcular la potencia 2 de un #")
print("****")
#variable controladora
opcion=1
while(opcion != 0):
    
    ##variable controladora
    opcion=int(input("digita una opcion: "))

    # pregunta por la opcion

    if (opcion == 0):
        break
   
    elif(opcion==1):
        numero=int(input("Digita un numero "))
        raiz=math.sqrt(numero)
        print(f"la raiz de numero es {raiz}")
    elif(opcion==2):
        numero=int(input("Digita un numero "))
        potencia=math.pow(numero,2)
        print(f"La potencia del numero es{potencia}")
    else:
        print("digigta una valida ome")

