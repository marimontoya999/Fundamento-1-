# a=200
# b=33
# if b > a:
#     print("b is greater than a")
# elif a==b:
#     print("a and b are equal")
# else:
#     print("a is greater than b")

# edad=int(input("Que edad tienes? "))
# if edad >=18:
#     print("Eres mayor de edad")
# else: 
#     print("Eres menor de edad")

# num=int(input("Ingresa un numero: "))
# if num % 2 == 0:
#     print("El numero es par")
# else:
#     print("El nuero es impar")

# nota=int(input("Cual fue tu nota? "))
# if nota >= 90:
#     print("Excelente!")
# elif nota >= 70: 
#     print("Aprobado")
# else:
#     print("Reprobado")

# num=int(input("Ingresa un numero: "))
# if num > 0:
#     print("El numero es positivo")
# elif num == 0:
#     print("EL numero es igual a cero")
# else:
#     print("El numero es negtivo")

# compr_total= float(input("Ingresa el monto total de tu compra: "))
# if compr_total > 100.000:
#     descuento= compr_total*0.1 
#     total= compr_total - descuento
#     print(f"El precio final con descuento es {total} ")
# elif compr_total <= 100.000:
#     print(f"El precio es {compr_total} ")

# nota1=int(input("Ingresa la primra nota: "))
# nota2=int(input("Ingresa la segunda nota: "))
# nota3=int(input("Ingresa la tercera nota: "))
# prom = (nota1+nota2+nota3)/3
# print(prom)

# if prom > 5.0:
#     print("Las notas no deben superar 5")
# elif prom >= 3.0:
#     print("Aprueba!")
# else:
#     print("Reprobado")

# stock_act=float(input("Ingresa el stock actual del producto: "))
# cantidad_vendida=float(input("Ingresa la cantidad vendida: "))
# stock_restante= stock_act - cantidad_vendida
# print(f"el stock restante es {stock_restante} unidades")
# if stock_restante <= 0:
#     print("El inventario se debe restablecer")
# else:
#     print("No se requiere restableer el stock")


# velocidad_vehiculo=int(input("La velocidad del carro es: "))
# print(velocidad_vehiculo)
# if velocidad_vehiculo > 100:
#     print("¡PELIGRO!🔥 exceso de velocidad‼")
# elif velocidad_vehiculo >= 81:
#     print("Precaucion, veocidad alta😬")
# elif velocidad_vehiculo >= 40:
#     print("Velocidad adecuada💕")
# elif velocidad_vehiculo <= 40:
#     print("Velocidad muy baja😴, acelere con precaucion ")

# gastos = float(input("Ingresa su gasto mensual: "))
# if gastos <100:
#     print("Cliente basico")
# elif 100 <= gastos <= 500:
#     print("Cliente frecuente") 
# elif 501 <= gastos <=1000:
#     print("Cliente premium")
# else:
#     print("Cliente VIP")

# edad=int(input("Que edad tienes? "))
# if edad < 18:
#     print("Se sugiere revisar la seccion juvenil")
# else: 
#     print("Se le informa sobre sus beneficios adicionales")

# es_mayor = False 
# if not es_mayor:
#     print("La persona es menor de edad.")

# contraseña_correcta=300708
# contraseña_ingresada=int(input("Ingrese la contraseña"))
# if not contraseña_ingresada==contraseña_correcta:
#     print("Contraseña incorrecta")
# else:
#     print("Acceso permitido")

# usuario=input("Ingrese el usuario")
# clave=("Ingrese la clave")

# if usuario == "Admin" and clave == "1234":
#     print("Acceso permitido")
# else:
#     print("Acceso denegado.")

# edad=int(input("Ingresa tu edad"))
# if edad >= 18 and edad < 65:
#     print("Estas en edad laboral")
# else:
#     print("No estas en edad laboral")

# membresia = input("¿Tienes membresia? (si/no): ").lower()
# total_compra =float(input("Ingree el total de su compra: "))
# if membresia == "si" or total_compra >100:
#     print("Descuento aplicado")
# else:
#     print("No aplica descuento")

# edad=int(input("Ingresa tu edad: "))
# es_vip=input("Tienes pase VIP? (si/no)")

# if edad >= 18 or es_vip == "si":
#     print("Puede ingresar a la zona VIP.")
# else:
#     print("No tiene acceso.")


# tipo_usuario= input("Ingrese su tipo de usuario (Administrador / Invitado / Usuario registrado)")
# if tipo_usuario == "administrador":
#     print("Tiene acceso a todas las opciones")
# elif tipo_usuario == "usuarioregistrado":
#     print("Puede acceder a las opciones basicas")
# else:
#     print("Solo tiene acceso a visualizar el contenido")

# promedio=int(input("Ingrese su promedio: "))
# nivel=int(input("Ingrese su nivel socio-economico: "))
# if promedio >= 90 or nivel >= 1 and nivel <= 2:
#     print("Eres apto para la beca")
# else:              xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
#     print("No eres apto para la beca")

# num=int(input("Ingrese un numero: "))
# par_o_inpar = "par" if num % 2 == 0 else "impar"
# positivo_o_negativo = "positivo" if num > 0 else "neutro" if num == 0 else "negativo"

# print(f"El numero es {par_o_inpar} y {positivo_o_negativo}")

# contador = 1
# while contador <= 5:
#     print("Numero:", contador)
#     contador += 1

# acumulador = 0
# for i in range(1, 6):
#     acumulador += i
# print("Suma total:", acumulador)

# total = 0
# contador = 0

# while contador < 5:
#     numero = float(input("Ingrese un numero: "))
#     total += numero 
#     contador += 1
# promedio = total / contador
# print("El promedio es:", promedio)

# num = int(input("Escribe un numero positivo: "))
# while num < 0:
#     print("Escribiste un numero negativo! Vuelve a intentar")
#     num = int(input("Escriba un numero positivo: "))
# print("Gracias💕")

# num = 2
# while num <= 20:
#     print("El numero es: ", num)
#     num += 2

# contraseña_ingresada= int(input("Ingresa tu contraseña: "))

# while contraseña_ingresada != 1234:
#     print("Acceso denegado")
#     contraseña_ingresada= int(input("Ingresa tu contraseña: "))
# print("Acceso permitido")

# num1 = int(input("Ingresa el primer numero:"))
# num2 = int(input("Ingresa el segundo numero:"))
# suma = num1 + num2
# while suma < 100:
#     num1 = int(input("Ingresa el primer numero:"))
#     num2 = int(input("Ingresa el segundo numero:"))
# print(f"El numero es: ", suma)

num , multilpicacion = 0, 0

while num < 70:
    num += 7
    multilpicacion +=1
    print(f"7 * {multilpicacion} es igual a {num}" )