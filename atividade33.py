# Mostre-me as seguintes listas, derivadas de:
# [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# Intervalo de 1 a 9
# Intervalo de 8 a 13
# Números pares
# Números ímpares
# Todos os múltiplos de 2, 3 e 4
# Lista reversa
# Razão entre a soma do intervalo de 10 a 15 pelo intervalo de 3 a 9 em float

lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
sublista = lista[1:9]
sublista = lista[8:13]
print(sublista)

números = list(range(0, 16))
pares = [n for n in números if n % 2 == 0]
ímpares = [n for n in números if n % 2 != 0]

print("Números pares:", pares)
print("Números ímpares:", ímpares)

números = list(range(0, 16))

múltiplos_2 = [n for n in números if n % 2 == 0]
múltiplos_3 = [n for n in números if n % 3 == 0]
múltiplos_4 = [n for n in números if n % 4 == 0]

print("Múltiplos de 2:", múltiplos_2)
print("Múltiplos de 3:", múltiplos_3)
print("Múltiplos de 4:", múltiplos_4)

lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
inversa = lista[::-1]
print(inversa)

números =  list(range(0, 16))
intervalo1 = números[10:16]
intervalo2 = números[3:10]

soma_intervalo1 = sum(intervalo1)
soma_intervalo2 = sum(intervalo2)

razão = float(soma_intervalo1) / float(soma_intervalo2)

print("Soma do intervalo 1:", soma_intervalo1)
print("Soma do intervalo 2:", soma_intervalo2)
print("Razão entre as somas:", razão)