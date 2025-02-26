#LAMBDA
# num=[1,2,3,4,5,6,7,8]
# evens= filter(lambda x: x%2 == 0, num)
# print(list(evens))

# fruits=["apple", "banana", "cherry"]
# lenghts= list(map(lambda x: len(x), fruits))
# print(lenghts)

# num=[3,1,4,1,5,9,2,6]
# print(sorted(num))

# personas = {
#     {"nombre": "Carlos", "Edad": 35},
#     {"nombre": "Ana", "Edad": 25},
#     {"nombre": "Luis", "Edad": 40},
# }
# ordenado=sorted(personas, key=lambda p: p["edad"])
# print(ordenado)

# num=[1,2,3,4,5]
# def cuadrado (n):
#     return n ** 2
# resultado=map(cuadrado, num)
# print(list(resultado))

# num=[1,2,3,4,5]
# resultado=map(lambda n: n**2, num)
# print(list(resultado))

# num=[8,12,3,7,50]
# print(sorted(num))

# personas = [
#     {"nombre": "Fabian", "nota": 3.5},
#     {"nombre": "Mauricio", "nota": 2.5},
#     {"nombre": "Luisa", "nota": 4.0},
# ]

# ordenado = sorted(personas, key=lambda p: p["nota"])
# print(ordenado)

# num=[1,4,6,8,3,9]
# resulado=filter(lambda n: n < 5, num)
# print(list(resulado))

# doble= lambda n: n * 2 
# num=int(input("Ingresa un numero: "))
# print(f"El doble de {num} es: {doble(num)}")

# par= lambda n: "Par" if n % 2 == 0 else "Impar"
# num= int(input("Ingresa un numero: "))
# print(f"El numero {num} es {par(num)}")

# celsius= lambda c: c*9/5+32
# grados=float(input("Ingresa una temperatura: "))
# print(f"La temperatura en grados farenheit es: {celsius(grados)}")

# calcular_matricula = lambda promedio, matricula: matricula * (0.8 if promedio >= 4.5 else 0.9 if 4.0 <= promedio < 4.5 else 1)
# promedio = float(input("Ingrese el promedio del estudiante: "))
# matricula = float(input("Ingrese el costo original de la matrícula: "))

# valor_final = calcular_matricula(promedio, matricula)
# print(f"El valor final a pagar es: {valor_final:.2f}")

