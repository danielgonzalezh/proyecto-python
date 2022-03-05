# ejemplo de estaciones

mes = input("Digita un mes del año ").lower()

print(f"El Mes digitado fue {mes}")

if(mes == "diciembre" or mes =="enero" or mes =="febrero" or mes =="marzo"):
    print("Estas en INVIERNO")
elif( mes == "junio" or mes == "julio" or mes == "agosto"):
    print("Estas en VERANO")
elif( mes == "abril" or mes == "mayo"):
    print("Estas en PRIMAVERA")
elif( mes == "septiembre" or mes == "octubre" or mes == "noviembre"):
    print("Estas en OTOÑO")
else:
    print ("NO EXISTE")

