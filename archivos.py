resp = True
while resp:
    num = input('Ingrese número:  ')
    if num == '':
        resp = False
    else:
        a = open ("almacen.mio","a")
        a.write(num+',')
        a.close()
a = open("almacen.mio")
print(a.read())
a.close()