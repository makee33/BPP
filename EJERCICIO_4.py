import pdb

#EJERCICIO 1
print("------------------------------------------------------------------------------")
print("EJERCICIO 1")
print("------------------------------------------------------------------------------")

# LA LISTA PROPUESTA
lista_ej4 = [[2,4,1],[1,2,3,4,5,6,7,8],[100,250,43]]

# PRIMERO LO HACEMOS AL MODO ARCAICO
lista_mayores = []

for sublista in lista_ej4:
    maxi = 0
    for numero in sublista:
        if numero > maxi:
            maxi = numero

    lista_mayores.append(maxi)

print("Lista original: ")
print(lista_ej4)
print("Lista filtrada: ")
print(lista_mayores)


#CON COMPRENSION DE LISTAS
lista_mayores2 = []
lista_mayores2 = [numero for numero in [max(sublista) for sublista in lista_ej4]]
print("Lista filtrada con comprension: ")
print(lista_mayores2)



#EJERCICIO 2
print("------------------------------------------------------------------------------")
print("EJERCICIO 2")
print("------------------------------------------------------------------------------")

lista_ej4_2 = [3, 4, 8, 5, 5, 22, 13]

#FUNCION PRIMOS, TIENE QUE DEVOLVER TRUE
def primos(n):
    if n<= 1: return False
    elif n==2: return True
    for i in range (2,n):
       if n%i == 0:
        return False
    else: return True


primos=list(filter(primos,lista_ej4_2))

print("Lista original: ")
print(lista_ej4_2)
print("Lista filtrada primos: ")
print(primos)