#Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.
horas_trabajadas = float(input("¿Cuantas horas has trabajado?\n"))
coste_horas = float(input("¿Cuanto es el precio de la hora?\n"))
operación = horas_trabajadas*coste_horas
redondeado = round(operación, 2)
print("La paga que le corresponde es la siguiente:", redondeado, "€")