contador = 0
numero=0
units=['one','two','three','four','five','six','seven','eight',
'nine','ten','eleven','twelve','thirteen','fourteen','fifteen',
'sixteen','seventeen','eighteen','nineteen']
tens=['twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']

listado=open('listado.txt','w')

digitos=[]
limite=int(input('>> '))
alphanumber=''

while numero < limite:
    numero += 1
    tran=numero
    digitos=[]

    for posicion in range (1,5):
        digitos.append(tran%10)
        tran=tran//10


    if digitos[3] != 0:
        alphanumber=alphanumber+'onethousand'

    if digitos[2] != 0:
        if digitos[1] != 0 or digitos[0] != 0:
            alphanumber= alphanumber+units[digitos[2]-1]+'hundredand'
        else:
            alphanumber= alphanumber+units[digitos[2]-1]+'hundred'
      
    if digitos[1]==1:
        id=digitos[1]*10+digitos[0]-1
        alphanumber=alphanumber+units[id]
    elif digitos[1] != 0:
        alphanumber= alphanumber+tens[digitos[1]-2]
        if digitos[0] != 0:
            alphanumber= alphanumber+units[digitos[0]-1]
    else:
        if digitos[0] != 0:
            alphanumber= alphanumber+units[digitos[0]-1]
    linea=(str(numero)+' - '+alphanumber+' - '+str(len(alphanumber))+'\n')
    listado.write(linea)

    contador=contador+len(alphanumber)
    alphanumber=''
listado.close()
print (contador)