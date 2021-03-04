
"""Guarde en lista `naturales` los primeros 100 números naturales (desde el 1) 
usando el bucle while
"""

naturales =[]
cantidadNumeros = 100

i = 1
while i < (cantidadNumeros + 1 ):
  naturales.append(i)
  i += 1

"""Guarde en `acumulado` una lista con el siguiente patrón:

['1','1 2','1 2 3','1 2 3 4','1 2 3 4 5',...,'...47 48 49 50']

Hasta el número 50.
"""
acumulado = []
limite = 50
i=2
numeroAnterior = '1'
acumulado.append(numeroAnterior)
while i<=50:
  #numeroAnterior.strip()
  numeroAnterior = numeroAnterior +  ' ' + str(i) 
  acumulado.append(numeroAnterior )
  i = i+1
print(acumulado)

"""Guarde en `suma100` el entero de la suma de todos los números entre 1 y 100:
"""

suma100 = 0
sumaSiguiente = 0
cantidadNum = 100

i = 1
while i < (cantidadNum + 1 ):
  suma100 = suma100 + i
  sumaSiguiente = suma100
  sumaSiguiente = suma100 + sumaSiguiente 
  i+=1 


"""Guarde en `tabla100` un string con los primeros 10 múltiplos del número 134, 
separados por coma, así:

'134,268,...'

"""
i=1
x= 0
tabla100 = ""
valorComa = ','
while x<10:
  if i%134==0:
    x = x+1
    if x == 10:
      valorComa = ''
    tabla100 = tabla100 + str(i) + valorComa
  i = i+1
print(tabla100)


"""Guardar en `multiplos3` la cantidad de números que son múltiplos de 3 y 
menores o iguales a 300 en la lista `lista1` que se define a continuación (la lista 
está ordenada).
"""
lista1 = [12, 15, 20, 27, 32, 39, 42, 48, 55, 66, 75, 82, 89, 91, 93, 105, 123, 132, 150, 180, 201, 203, 231, 250, 260, 267, 300, 304, 310, 312, 321, 326]

listaLongitud = len(lista1)
i=0
multiplos3 = 0
residuo=0
valor = 0
while i<listaLongitud:
  valor = lista1[i]
  if  valor < 300:
    residuo = valor%3
    if residuo == 0 :
      multiplos3 = multiplos3 +1 
  i = i+1



"""Guardar en `regresivo50` una lista con la cuenta regresiva desde el número 
50 hasta el 1, así:

[
  '50 49 48 47...',
  '49 48 47 46...',
  ...
  '5 4 3 2 1',
  '4 3 2 1',
  '3 2 1',
  '2 1',
  '1'
]
"""
acumulado1 = []
limite = 50
regresivo50 = []
i=2
numeroAnterior = '1'
acumulado1.append(numeroAnterior)
while i<=50:
  numeroAnterior =  str(i) + ' ' + numeroAnterior 
  acumulado1.append(numeroAnterior )
  i = i+1

j=50
while j > 0:
  valor = acumulado1[j-1]
  regresivo50.append(valor )
  j = j -1
print(regresivo50)

"""Invierta la siguiente lista usando el bucle for y guarde el resultado en 
`invertido` (sin hacer uso de la función `reversed` ni del método `reverse`)
"""
lista2 = list(range(1, 70, 5))
longitud = 0
x= 0
invertido = []
for dia in lista2:
    x += 1
print(x)
while x > 0:
  valor = lista2[x-1]
  invertido.append(valor )
  x = x -1
print(invertido)

"""Guardar en `primos` una lista con todos los números primos desde el 37 al 300
Nota: Un número primo es un número entero que no se puede calcular multiplicando 
otros números enteros.
"""
primos = []
for x in range (37,300):
  for num in range (2,x):
    if x%num !=0:
      continue
    else: 
      break 
  else: 
    primos.append(x)


"""Guardar en `fibonacci` una lista con los primeros 60 términos de la serie de 
Fibonacci.
Nota: En la serie de Fibonacci, los 2 primeros términos son 0 y 1, y a partir 
del segundo cada uno se calcula sumando los dos anteriores términos de la serie.

[0, 1, 1, 2, 3, 5, 8, ...]

"""
fibonacci = []
a  = 0
b = 1
c = 0
cantidadTerminos = 58
fibonacci.append(a)
fibonacci.append(b)
for i in range(cantidadTerminos):
   # print(fibonacci)
    a =  b + c
    c = b
    b = a
    fibonacci.append(a)

"""Guardar en `factorial` el factorial de 30
El factorial (símbolo:!) Significa multiplicar todos los números enteros desde
el 1 hasta el número elegido.

Por ejemplo, el factorial de 5 se calcula así:

5! = 5 × 4 × 3 × 2 × 1 = 120
"""
valorfactorial = 30
factorial = 1
i = 1

while i <= valorfactorial:
   factorial = factorial * i 
   i = i + 1


"""Guarde en lista `pares` los elementos de la siguiente lista que esten 
presentes en posiciones pares, pero solo hasta la posición 80.
"""

lista3 = [941, 149, 672, 208, 99, 562, 749, 947, 251, 750, 889, 596, 836, 742, 512, 19, 674, 142, 272, 773, 859, 598, 898, 930, 119, 107, 798, 447, 348, 402, 33, 678, 460, 144, 168, 290, 929, 254, 233, 563, 48, 249, 890, 871, 484, 265, 831, 694, 366, 499, 271, 123, 870, 986, 449, 894, 347, 346, 519, 969, 242, 57, 985, 250, 490, 93, 999, 373, 355, 466, 416, 937, 214, 707, 834, 126, 698, 268, 217, 406, 334, 285, 429, 130, 393, 396, 936, 572, 688, 765, 404, 970, 159, 98, 545, 412, 629, 361, 70, 602]

pares = []
posicion = 80
valor = 0
valor = lista3[80]
#print(valor)
i = 0
while i <=posicion:
  valor = lista3[i]
  pares.append(valor)
  i = i+2
#print(pares)




"""Guarde en lista `cubos` el cubo (potencia elevada a la 3) de los números del 
1 al 100. 
"""
cubos = []
limite = 100
i = 1
while i <= limite:
  potencia = i**3
  cubos.append(potencia)
  i= i+1
#print(cubos)


"""Encuentre la suma de la serie 2 +22 + 222 + 2222 + .. hasta sumar 10 términos 
y guardar resultado en variable `suma_2s` 
"""

valorDos = "2"
i = 1
suma_2s = 2
while i<10: 
  i = i+1
  valorDos = valorDos + "2"
  suma_2s = suma_2s + int(valorDos)

"""Guardar en un string llamado `patron` el siguiente patrón llegando a una 
cantidad máxima de asteriscos de 30. 
*
**
***
****
*****
******
*******
********
*********
********
*******
******
*****
****
***
**
*
"""
i = 0 
asterisco = "*"
vuelta = ""
j = 0
listaAsterisco = []
k =0
patron = ""
while i < 29:
  listaAsterisco.append(asterisco)
  asterisco = "*" + asterisco
  i = i +1 
asterisco1 = asterisco
asterisco = asterisco1[:- 1]
while j < 30:
  listaAsterisco.append(asterisco1)
  asterisco1 = asterisco1[:- 1]
  j = j + 1

while k < 59:
  patron = patron + listaAsterisco[k] + "\n"
  k= k +1 
patron = patron[:-1]


