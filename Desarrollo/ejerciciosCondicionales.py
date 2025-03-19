print("1° Consigna: Escribir un programa que a partir de un número entero positivo muestre por la pantalla si es par o impar\n")
num=int(input("Introduce un número entero positivo: "));
if num >= 1:
    if num % 2 == 0:
        print("Es un número par");
    else:
        print("Es un número impar");
else:
    print("Debe ser un número entero positivo")

#print("2° Consigna: Escribe un programa que a partir de un n°entero positivo muestra por pantalla si es primo o no\n")
#numprimo = int(input("Introduce un número entero positivo: "))
#if numprimo <= 0:
#    print("Debe ser un número entero positivo");
#else:
#    break;


print("3° Consigna: Escribe un programa que permita realizar la división de 2 números siempre y cuando el denominador no sea 0\n")
numerador = int(input("Introduce el numerador: "));
denominador = int(input("Introduce el denominador: "));
if denominador == 0:
    print("No se puede dividir por 0")
else:
    print("El resultado es " + str(numerador/denominador));

print("Desafio: Escribe un programa que solicite 3 números enteros positivos y muestre por pantalla el menor\n")
num1 = int(input("1° > "));
num2 = int(input("2° > "));
num3 = int(input("3° > "));
if num1 < num2 and num1 <= num3:
    print(str(num1) + " es el número más chico.")
elif num2 < num1 and num2 <= num3:
    print(str(num2) + " es el número más chico.")
elif num3 < num2 and num3 <= num1:
    print(str(num3) + " es el número más chico.")
else:
    print("Los números son iguales o inválidos")
