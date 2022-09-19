total_preguntas = 12
lista_respuestas = []

archivo_math = open("test_math.csv","r")
encabezado = True
for linea in archivo_math:
    if (not encabezado):
        lista_respuestas.append(linea.split(sep=',')[1].replace('\n',''))
    else:
        encabezado = False
archivo_math.close()

if(len(lista_respuestas) != total_preguntas):
    i = 0
    while(i < total_preguntas):
        lista_respuestas.append('') 
        i+=1

opciones_esperadas = ['1a','1b','1c','1d','1e','2a','2b','3a','3b','3c','3d','4a','5']
continuar = True
while(continuar):
    print('HENRY CHALLENGE - MATEMÁTICA')
    print('****************************')
    print('Tus respuestas:')
    print('* 1a:', lista_respuestas[0])
    print('* 1b:', lista_respuestas[1])
    print('* 1c:', lista_respuestas[2])
    print('* 1d:', lista_respuestas[3])
    print('* 1e:', lista_respuestas[4])
    print('* 2a:', lista_respuestas[5])
    print('* 2b:', lista_respuestas[6])
    print('* 3a:', lista_respuestas[7])
    print('* 3b:', lista_respuestas[8])
    print('* 3c:', lista_respuestas[9])
    print('* 3d:', lista_respuestas[10])
    print('* 4a:', lista_respuestas[11])
    print('* 5 - Para terminar')
    op = input('Por favor, ingresa la opción que quieras cargar: ')
    if(op == '1a'):
        r = input('Ingresa tu respuesta: ')
        try:
            if(r!='NULL'):
                r = float(r)
                lista_respuestas[0] = str(r)
            else:
                lista_respuestas[0] = 'NULL'
        except:
            r = ''
            print('Por favor, ingresar un formato correcto')
    elif(op == '1b'):
        r = input('Ingresa tu respuesta: ')
        try:
            if(r!='NULL'):
                r = float(r)
                lista_respuestas[1] = str(r)
            else:
                lista_respuestas[1] = 'NULL'
        except:
            r = ''
            print('Por favor, ingresar un formato correcto')
    elif(op == '1c'):
        r = input('Ingresa tu respuesta: ')
        try:
            if(r!='NULL'):
                r = float(r)
                lista_respuestas[2] = str(r)
            else:
                lista_respuestas[2] = 'NULL'
        except:
            r = ''
            print('Por favor, ingresar un formato correcto')
    elif(op == '1d'):
        r = input('Ingresa tu respuesta: ')
        try:
            if(r!='NULL'):
                r = float(r)
                lista_respuestas[3] = str(r)
            else:
                lista_respuestas[3] = 'NULL'
        except:
            r = ''
            print('Por favor, ingresar un formato correcto')
    elif(op == '1e'):
        r = input('Ingresa tu respuesta: ')
        try:
            if(r!='NULL'):
                r = float(r)
                lista_respuestas[4] = str(r)
            else:
                lista_respuestas[4] = 'NULL'
        except:
            r = ''
            print('Por favor, ingresar un formato correcto')
    elif(op == '2a'):
        r = input('Ingresa tu respuesta: ')
        try:
            if(r!='NULL'):
                r = float(r)
                lista_respuestas[5] = str(r)
            else:
                lista_respuestas[5] = 'NULL'
        except:
            r = ''
            print('Por favor, ingresar un formato correcto')
    elif(op == '2b'):
        r = input('Ingresa tu respuesta: ')
        try:
            if(r!='NULL'):
                r = float(r)
                lista_respuestas[6] = str(r)
            else:
                lista_respuestas[6] = 'NULL'
        except:
            r = ''
            print('Por favor, ingresar un formato correcto')
    elif(op == '3a'):
        r = input('Ingresa tu respuesta: ')
        if (r in ('Verdadero','Falso')):
            lista_respuestas[7] = r
        else:
            print('Por favor, ingresar Verdadero o Falso')
    elif(op == '3b'):
        r = input('Ingresa tu respuesta: ')
        if (r in ('Verdadero','Falso')):
            lista_respuestas[8] = r
        else:
            print('Por favor, ingresar Verdadero o Falso')
    elif(op == '3c'):
        r = input('Ingresa tu respuesta: ')
        if (r in ('Verdadero','Falso')):
            lista_respuestas[9] = r
        else:
            print('Por favor, ingresar Verdadero o Falso')
    elif(op == '3d'):
        r = input('Ingresa tu respuesta: ')
        if (r in ('Verdadero','Falso')):
            lista_respuestas[10] = r
        else:
            print('Por favor, ingresar Verdadero o Falso')
    elif(op == '4a'):
        r = input('Ingresa tu respuesta: ')
        try:
            if(r!='NULL'):
                r = float(r)
                lista_respuestas[11] = str(r)
            else:
                lista_respuestas[11] = 'NULL'
        except:
            r = ''
            print('Por favor, ingresar un formato correcto')
    elif(op == '5'):
        continuar = False
    else:
        print('Debes ingresar una de las opciones esperadas. Gracias.')

archivo_math = open("test_math.csv","w")
archivo_math.write('punto,pregunta\n')
i = 0
while (i < total_preguntas):
    archivo_math.write(opciones_esperadas[i]+','+str(lista_respuestas[i])+'\n')
    i+=1
archivo_math.close()
