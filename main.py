from functions import *  # Importa funciones necesarias
from calculos import *    # Importa cálculos necesarios

print("Hola mundo")  # Imprime "Hola mundo"

def mostrar_menu():
    print("\n----- Menú Principal -----")
    print("1. Suma")
    print("2. Área del Triángulo")
    print("3. Área del Cuadrado")
    print("4. Salida")
    print("--------------------------")

def main():#funcion menu
    while True:
        mostrar_menu()  # Muestra el menú
        opcion = input("Elige la opción que desea visualizar: ")

        # Asegúrate de comparar con cadenas, ya que input() devuelve una cadena
        if opcion == "1":
            # Llama a la función suma y muestra el resultado
            resultado = suma() # Asegúrate de que suma() retorne un valor
            print(f"La suma de los números es: {resultado}")
        
        elif opcion == "2":
            # Llama a la función que calcula el área del triángulo
            resultado2 = triangulo()  # Asegúrate de que triangulo() retorne un valor
            print(f"El cálculo del área del triángulo es: {resultado2}")
        
        elif opcion == "3":
            # Llama a la función que calcula el área del cuadrado
            resultado3 = cuadrado() # Asegúrate de que cuadrado() retorne un valor
            print(f"El cálculo del área del cuadrado es: {resultado3}")
        
        elif opcion == "4":
            print("Gracias por su atención")
            break  # Salir del bucle
        
        else:
          print("Opción no válida. Intenta de nuevo.")# cuando se pone un numero invalido

if __name__ == "__main__": # para que nos ayude a inicar el menu
    main()#inicio del programa
        
        