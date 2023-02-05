#Tarea 3, Calculadora Python de terminal

# Se añade interacción con terminal

print("")
print("Seleccionar opercación a realizar:")
print("")
print("1.Sumar")
print("2.Resta")
print("3.Multiplicación")
print("4.Dividir")
print("5.Factorial")
print("6.Potencia")
print("")

operation=input()


if operation == "1":
   suma=0
   cantidad=0
   n=input("Ingrese el primer número que desee sumar: ")

   while(n!=""):
       suma=suma+int(n)
       cantidad=cantidad+1
       n=input("Ingrese el siguiente número: ")    
   print("El total de la suma es: ", suma)    
   print("cantidad de elementos: ",cantidad)
    
elif operation == "2":
 num1 = input("inserte primer número: ")
 num2 = input("inserte segundo número: ")
 print("El resultado de la resta es: " + str(int(num1) - int(num2)))
    
elif operation == "3":
 mult=1
 cantidad=0
 n=input("Ingrese el primer número que desee multiplicar: ")

 while(n!=""):
       mult=mult*int(n)
       cantidad=cantidad+1
       n=input("Ingrese el siguiente número: ")    
 print("El resultado de la multiplicacion: ", mult)    
 print("cantidad de elementos: ",cantidad)
    
elif operation == "4":  
    num1 = input("inserte primer número: ")
    num2 = input("inserte segundo número: ")
    print("El resultado de la división es: " + str(int(num1) / int(num2)))
    
elif operation == "5":
 num1 = int(input("Inserte el primer número: "))
 factorial=1
 if num1<=0:
        print("Error número negativo, por favor ingrese un número entero")
 if num1>=0:
        for i in range(1, num1+1):    
         factorial=factorial*i       
 print("El factorial es: ", factorial)
 
elif operation == "6":
   num1 =int(input("Inserte primer número: "))
   num2 = int(input ("Ingrese la potencia: "))
   Potencia= pow(num1,num2)
   print("El resultado de la potencia es:", Potencia)

else:
    print ("Error de numero ingresado")  