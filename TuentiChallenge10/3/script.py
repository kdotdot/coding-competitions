fi=open("libro.txt", "r")
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'á', 'é', 'í', 'ó', 'ú', 'ü']

f1 = fi.readlines()

#Elimina caracteres no permitidos
filtro1 = []
for line in f1:
    nuevaLinea = ""
    for car in line:
        nCar = car.lower()
        nuevaLinea += nCar if nCar in letters else ' '
    nuevaLinea+='\n'
    filtro1.append(nuevaLinea)
#print(filtro1)
#f1=open("filtro1.txt","w+")
#for line in filtro1:
#    f1.write(line)
#exit()

#Separa por palabras y elimina las que tienen 2 o 1 letra
asd = set()
palabras = []
for line in filtro1:
    for word in line.split():
        if len(word)>2:
            palabras.append(word)
        else:
            asd.add(word)
#print(palabras)
#print(asd)
#f2=open("palabras.txt","w+")
#for line in palabras:
#    f2.write(line+'\n')
#exit()

#Cuenta las palabras
fo=open("wordcount.txt","w+")
while(len(palabras)>0):
    word = palabras[0]
    cuenta = palabras.count(word)
    palabras = [x for x in palabras if x != word]
    fo.write("{} {}\n".format(word,cuenta))

#fo.write("Case #{}: {}\n".format(case+1,best.pop()))
