# edad = int(input("Ingresa tu edad: "))
# print(f"Tu edad es {edad}, bienvenida a la programacion!")

# num1= float(input("Ingresa el primer numero: "))
# num2= float(input("Ingresa el segundo numero: "))
# suma= num1 + num2
# print(f"La suma de los dos numeros es {suma}")

# num1= float(input("Ingresa el primer numero: "))
# num2= float(input("Ingresa el segundo numero: "))
# num3= float(input("Ingresa el tercer numero: "))
# prom= num1 + num2 + num3 /3
# print(f"El promedio de los numeros es {prom}")

# temp_C= float(input("Ingresa la temperatura: "))
# F = temp_C * 9/5 + 32
# print(f"La temperatura en fahrenheit es {F}")

# num= int(input("Ingresa un numero: "))
# if num < 0:
#     print(f"El numero {num} es negativo")
# elif num > 0:
#     print(f"El numero {num} es positivo")
# else:
#     print(f"El numero {num} es igual a 0")

# num1= float(input("Ingresa la primera nota: "))
# num2= float(input("Ingresa la segunda nota: "))
# num3= float(input("Ingresa la tercera nota: "))
# prom= num1 + num2 + num3 /3
# if prom >= 3.5:
#     print(f"El alumno aprobo con un promedio de {prom}")
# else:
#     print(f"El alumno reprobo con un promedio de {prom}")

# Lista de pedidos (Cada pedido es un diccionario con 'monto' y 'estado')
# pedidos = [
#     {"monto": 600000, "estado": "Pagado"},
#     {"monto": 150000, "estado": "Pendiente"},
#     {"monto": 800000, "estado": "Pagado"},
#     {"monto": 450000, "estado": "Pagado"},
#     {"monto": 200000, "estado": "Cancelado"},
#     {"monto": 1000000, "estado": "Pagado"}
# ]

# # 1. Filtrar pedidos que están en estado "Pagado"
# pedidos_pagados = list(filter(lambda pedido: pedido["estado"] == "Pagado", pedidos))

# # 2. Calcular el total de ingresos de los pedidos pagados
# total_ingresos = sum(map(lambda pedido: pedido["monto"], pedidos_pagados))

# # 3. Aplicar un descuento del 5% a pedidos pagados con monto mayor a 500,000
# aplicar_descuento = lambda pedido: pedido["monto"] * 0.95 if pedido["monto"] > 500000 else pedido["monto"]
# pedidos_con_descuento = list(map(lambda pedido: {**pedido, "monto_final": aplicar_descuento(pedido)}, pedidos_pagados))

# # Mostrar los resultados
# print("Pedidos Pagados:")
# for pedido in pedidos_pagados:
#     print(pedido)

# print(f"\nTotal de ingresos antes del descuento: ${total_ingresos:.2f}")

# print("\nPedidos con descuento aplicado (si aplica):")
# for pedido in pedidos_con_descuento:
#     print(pedido)

# class Persona:
#     def __init__(self, nombre, edad):
#         self.nombre = nombre  # Atributo nombre
#         self.edad = edad      # Atributo edad

#     def mostrar_info(self):
#         print(f"Nombre: {self.nombre}, Edad: {self.edad}")

# # Creación de objetos
# persona1 = Persona("Carlos", 25)
# persona2 = Persona("Ana", 30)

# # Llamando a un método de la clase
# persona1.mostrar_info()
# persona2.mostrar_info()

# acumulador = 0  # Inicialización

# for i in range(1, 6):  # Iteración de 1 a 5
#     acumulador += i  # Suma acumulativa

# print("Suma total:", acumulador)

# total = 0  # Acumulador
# contador = 0  # Contador

# while contador < 5:
#     numero = float(input("Ingresa un número: "))
#     total += numero  # Sumar al acumulador
#     contador += 1  # Incrementar el contador

# promedio = total / contador  # Calcular promedio
# print("El promedio es:", promedio)
# numero = int(input("Escriba un número positivo: "))
# while numero < 0:
#     print("¡Ha escrito un número negativo! Inténtelo de nuevo")
#     numero = int(input("Escriba un número positivo: "))
# print("Gracias por su colaboración")

# dia = 0
# semana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo']
# while dia < 7:
#    print("Hoy es " + semana[dia])
#    dia += 1

#    while True:
#     dato = input("Ingrese 'salir' para terminar: ")
#     if dato == 'salir':
#         break