
rangox = int(input("Ingrese la cantidad de filas que va a tener la matriz: "))
rangoy = int(input("Ingrese la cantidad de columnas que va a tener la matriz: "))

list = []
suma = 0
max = 0
lower = 0
sum = 0

for x in range(0,rangoy):
    list.append([])

for z in list:
    for x in range(0,rangoy):
        z.append([])

for cantx, x in enumerate(list):
    sumfila = 0
    for canty, z in enumerate(range(1,len(x)+1)):
        num = int(input(f"ingrese el dato {z} de la fila {cantx+1}: "))
        suma += num 
        x[canty].append(num)
        
        sumfila += num
        
        if num > max:
            max = num
    
    print(f"La suma de la fila {cantx+1} es:",sumfila)

lower = max
for x in list:
    
    for z in x:

        dato = z[0]
        if dato < lower:
            lower = dato

col = int(input("Ingrese la fila a sumar: "))

for x in range(rangox):
    for y in range(rangoy):
        if x==col-1:
            sum=sum+list[x][y][0]




for x in list:
    print(x)

print("Esta es la suma de toda la matriz: " , suma)
print("Este es el dato mas grande: " , max)
print("Este es el dato mas pequeño: " , lower)
print(f"La suma de la fila {col} es:" , sum)