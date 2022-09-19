# Importante: No modificar ni el nombre ni los argumetos que reciben las funciones, sólo deben escribir
# código dentro de las funciones ya definidas.

def ListaDivisibles(numero, tope):
    '''
    Esta función devuelve una lista ordenada de menor a mayor con los números divisibles 
    por el parámetro número entre uno (1) y el valor del parámetro "tope"
    Recibe dos argumentos:
        numero: Numero entero divisor
        tope: Máximo valor a evaluar a partir de uno (1)
    Ej:
        ListaDivisibles(6,30) debe retornar [6,12,18,24,30]
        ListaDivisibles(10,5) debe retornar []
        ListaDivisibles(7,50) debe retornar [7,14,21,28,35,42,49]
    '''
    Lista=[]
    for i in range(1,tope+1):
        if i%numero==0:
            Lista.append(i)
        else:
            continue
    return Lista

def Exponente(numero, exponente):
    '''
    Esta función devuelve el resultado de elevar el parámetro "numero" al parámetro "exponente"
    Recibe dos argumentos:
        numero: El número base en la operación exponencial
        exponente: El número exponente en la operación exponencial
    Ej:
        Exponente(10,3) debe retornar 1000
    '''
    resultado=numero**exponente
    return resultado

def ListaDeListas(lista):
    '''
    Esta función recibe una lista, que puede contener elementos que a su vez sean listas y
    devuelve esos elementos por separado en una lista única. 
    En caso de que el parámetro no sea de tipo lista, debe retornar nulo.
    Recibe un argumento:
        lista: La lista que puede contener otras listas y se convierte a una 
        lista de elementos únicos o no iterables.
    Ej:
        ListaDeListas([1,2,['a','b'],[10]]) debe retornar [1,2,'a','b',10]
        ListaDeListas(108) debe retornar el valor nulo.
        ListaDeListas([[1,2,[3]],[4]]) debe retornar [1,2,3,4]
    '''
    if type(lista)==list:
        lista2=[]
        while lista!=lista2:
            if lista2!=[]:
                lista=lista2
                lista2=[]
                continue
            for i in lista:
                if type(i)==list:
                    lista2.extend(i)
                else:
                    lista2.append(i)
    else:
        lista2=None

    return lista2

def Factorial(numero):
    '''
    Esta función devuelve el factorial del número pasado como parámetro.
    En caso de que no sea de tipo entero y/o sea menor que 0, debe retornar nulo.
    Recibe un argumento:
        numero: Será el número con el que se calcule el factorial
    Ej:
        Factorial(4) debe retornar 24
        Factorial(-2) debe retornar nulo
        Factorial(0) debe retornar 1
    '''
    if numero<0 or type(numero)==float:
        y=None
    elif numero in [0,1]:
        y=1
    else:
        y=1
        for i in range(1,numero+1):
            y=y*i
    return y

def ListaPrimos(desde, hasta):
    '''
    Esta función devuelve una lista con los números primos entre los valores "desde" y "hasta"
    pasados como parámetro, siendo ambos inclusivos.
    En caso de que alguno de los parámetros no sea de tipo entero y/o no sea mayor a cero, debe retornar nulo.
    En caso de que el segundo parámetro sea mayor al primero, pero ambos mayores que cero,
    debe retornar una lista vacía.
    Recibe un argumento:
        desde: Será el número a partir del cual se toma el rango
        hasta: Será el número hasta el cual se tome el rango
    Ej:
        ListaPrimos(7,15) debe retornar [7,11,13]
        ListaPrimos(100,99) debe retornar []
        ListaPrimos(1,7) debe retonan [1,2,3,5,7]
    '''
    if type(desde)==str or type(desde)==str:
        resultado=None
    elif desde<=0 or hasta <=0:
        resultado=None
    elif type(desde)!=int or type(hasta)!=int:
        resultado=None
    elif desde>hasta:
        resultado=[]
    else:
        resultado=[]
        for i in range(desde, hasta+1):
            if i<4:
                resultado.append(i)
            else:
                j=int(i**0.5)
                k=2
                while k<=j:
                    if i%k==0:
                        break
                    elif k<j:
                        k+=1
                    else:
                        resultado.append(i)
                        k+=1

    return resultado

def ListaRepetidos(lista):
    '''
    Esta función recibe como parámetro una lista y devuelve una lista de tuplas donde cada 
    tupla contiene un valor de la lista original y las veces que se repite. Los valores 
    de la lista original no deben estar repetidos. 
    Debe respetarse el orden original en el que aparecen los elementos.
    En caso de que el parámetro no sea de tipo lista debe retornar nulo.
    Recibe un argumento:
        lista: Será la lista que se va a evaluar.
    Ej:
        ListaRepetidos([]) debe retornar []
        ListaRepetidos(['hola', 'mundo', 'hola', 13, 14]) 
            debe retornar [('hola',2),('mundo',1),(13,1),(14,1)]
        ListaRepetidos([1,2,2,4]) debe retornar [(1,1),(2,1),(4,1)]
    '''
    resultado=[]
    tupla=()
    ya_contados=[]
    if type(lista)!=list:
        resultado=None
    else:
        for i in lista:
            if i in ya_contados:
                continue
            else:
                tupla=(i, lista.count(i))
                resultado.append(tupla)
                ya_contados.append(i)                
    return resultado

class ClaseVehiculo:
    def __init__(self,tipo,color):
        self.tipo=tipo
        self.color=color
        self.velocidad=0.0
        
    def Acelerar(self, aceleracion):
        self.velocidad+=aceleracion
        if self.velocidad<0:
            self.velocidad=0
        elif self.velocidad>100:
            self.velocidad=100
        return self.velocidad

def OrdenarDiccionario(diccionario_par, clave, descendente=True):
    '''
    Esta función recibe como parámetro un diccionario, cuyas listas de valores tienen el mismo
    tamaño y sus elementos enésimos están asociados. Y otros dos parámetros que indican
    la clave por la cual debe ordenarse y si es descendente o ascendente.
    La función debe devolver el diccionario ordenado, teniendo en cuenta de no perder la
    relación entre los elementos enésimos.
    Recibe tres argumentos:
        diccionario:    Diccionario a ordenar.
        clave:          Clave del diccionario recibido, por la cual ordenar.
        descendente:    Un valor booleano, que al ser verdadero indica ordenamiento ascendente y 
                        descendente si es falso. 
                        Debe tratarse de un parámetro por defecto en True.
    Si el parámetro diccionario no es un tipo de dato diccionario ó el parámetro clave no 
    se encuentra dentro de las claves del diccionario, debe devolver nulo.
    Ej:
        dicc = {'clave1':['c','a','b'],
                'clave2':['casa','auto','barco'],
                'clave3':[1,2,3]}
        OrdenarDiccionario(dicc, 'clave1')          debe retornar {'clave1':['a','b','c'],
                                                                'clave2':['auto','barco','casa'],
                                                                'clave3':[2,3,1]}
        OrdenarDiccionario(dicc, 'clave3', False)   debe retornar {'clave1':['b','a','c'],
                                                                'clave2':['barco','auto','casa'],
                                                                'clave3':[3,2,1]}
    '''
    if type(diccionario_par)!=dict:
        diccionario_par=None
    else:
        guia=clave
        lista1=diccionario_par[guia]
        descendente=not(descendente)
        for i in diccionario_par:
            if i!=guia:
                lista2=diccionario_par[i]
                parejas=list(zip(lista1,lista2))
                parejas.sort(reverse=descendente)
                lista3=[]
                for _,j in parejas:
                    lista3.append(j)
                    diccionario_par[i]=lista3
                else:
                    continue
        lista1.sort(reverse=descendente)
        diccionario_par[guia]=lista1        
        
    return diccionario_par
