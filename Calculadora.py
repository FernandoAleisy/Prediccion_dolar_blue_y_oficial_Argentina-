import pandas as pd
import numpy as np
import requests

import datetime
from datetime import date

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

from tkinter import *

ventana = Tk()
ventana.title('Calculadora')
ventana.geometry('320x200')
ventana.resizable(0,0)
ventana.title('DolarPrediction')

# Variables
px=4
py=4

#Entrada de texto
label = Label(ventana,font=('calibri 10'),text='Fecha (AAAA-MM-DD)')
label.grid(row=0,columnspan=3, column=0)

e_texto = Entry(ventana,font=('calibri 20'),width=10)
e_texto.grid(row=0,column=3,columnspan=4,padx=px,pady=py)

#Funciones
ig=False

def numero(valor):
    global ig
    if ig==False:
        e_texto.insert(END,valor)
    else:
        e_texto.delete(0,END)
        e_texto.insert(END,valor)
        ig=False

def borrar():    
    global ig
    texto=e_texto.get()
    if texto[0]=='0':
        texto=texto[1:]
    e_texto.delete(0,END)
    e_texto.insert(0,texto[:-1])
    ig=False    

def borrarTodo():    
    global ig
    texto=e_texto.get()
    if texto[0]=='0':
        texto=texto[1:]
    e_texto.delete(0,END)
    ig=False 

def click_boton(valor):
    global ig
    texto=e_texto.get()
    if valor=='(' and not(texto[-1] in ['+','-','*','/']):
        e_texto.insert(END,'*')
    e_texto.insert(END,valor)
    ig=False


Url_DO = "https://api.estadisticasbcra.com/usd_of"
Url_DB = "https://api.estadisticasbcra.com/usd"
token = {"Authorization": "BEARER eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTA5MjAxMDgsInR5cGUiOiJleHRlcm5hbCIsInVzZXIiOiJmZXJuYW5kby5hbGVpc3lAaG90bWFpbC5jb20ifQ.zxzDuRQr0T8uu4yiryLpYpZGLCNUhwGz3FhKNK469GXq-xhThKve8h8rJwqHU_F31iR3yXBHw9-bYR_NQj9pGA"}

def Guardar_Json (url_DO, url_DB, token, anio):
    '''
    Guardar los archivos json de la url en un DataFrame para cada valor de dolar
    '''
    dias = anio*246

    data1=requests.get(url=Url_DO,headers=token)
    if data1.status_code == 200:
        data1 = pd.DataFrame(data1.json())
    else:
        print("No se pudo realizar la operacion para los registros del Dolar Oficial")

    data2=requests.get(url=Url_DB,headers=token)
    if data2.status_code == 200:
        data2 = pd.DataFrame(data2.json())
    else:
        print("No se pudo realizar la operacion para los registros del Dolar Oficial")
    
    if max(data1['d']) > max(data2['d']):
        dolar_oficial = data1.tail(dias+1)
        dolar_oficial = dolar_oficial[:-1]
        dolar_blue = data2.tail(dias)
    else:
        dolar_oficial = data1.tail(dias)
        dolar_blue = data2.tail(dias)
    
    df_Dolares = pd.merge(dolar_oficial,dolar_blue, on=['d','d'],how='outer')
    df_Dolares.rename(columns={'d':'Fecha', 'v_x':'DolarOficial', 'v_y':'DolarBlue'}, inplace=True)
    return df_Dolares

cache = Guardar_Json(Url_DO,Url_DB,token,4)
dfDolares4 = cache.copy()
dfDolares4 = dfDolares4.dropna()

def actualizar():
    global ig
    global cache
    global dfDolares4
    global Url_DO
    global Url_DB
    global token
    cache = Guardar_Json(Url_DO,Url_DB,token,4)
    dfDolares4 = cache.copy()
    dfDolares4 = dfDolares4.dropna()

def regresionLineal(df, tipoDolar):
    '''
    df = DataFrame, tipo = 'DolarOficial' o 'DolarBlue'
    '''
    model = LinearRegression(fit_intercept=True)
    df['Fecha'] = df['Fecha'].astype('datetime64')
    try:
        df.insert(1, 'FechaNumero',df['Fecha'].map(date.toordinal))
    except:
        True
    X = np.array(df['FechaNumero']).astype('float')
    y = np.array(df[tipoDolar])
    X = X[:, np.newaxis]
    model.fit(X, y)
    global X_train
    global X_test
    global y_train
    global y_test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=35)
    lr = LinearRegression(fit_intercept = True)
    lr.fit(X_train, y_train)
    
    return lr

def prediccion(fecha,tipoDolar):
    '''
    fecha = 'AAAA-MM-DD', tipoDolar = 'DolarOficial' o 'DolarBlue'
    '''
    f = list([fecha])
    f = pd.DataFrame(f)
    f = f.astype('datetime64')
    fn = int(f[0].map(date.toordinal)[0]) # Fecha como número
    fn = np.array(fn)
    fn = fn.reshape(-1,1)
    if tipoDolar == 'DolarOficial':
        prediccion = round(float(str(lrDO.predict(fn))[1:-1]),2)
    elif tipoDolar == 'DolarBlue':
        prediccion = round(float(str(lrDB.predict(fn))[1:-1]),2)
    return prediccion

def DO():
    global lrDO
    lrDO = regresionLineal(dfDolares4, 'DolarOficial')
    texto=e_texto.get()
    if texto[0]=='0':
        pred=texto[1:]
    else:
        pred = prediccion(texto,'DolarOficial')
    e_texto.delete(0,END)
    e_texto.insert(0,pred)

def DB():
    global lrDB
    lrDB = regresionLineal(dfDolares4,'DolarBlue')
    texto=e_texto.get()
    if texto[0]=='0':
        pred=texto[1:]
    else:
        pred = prediccion(texto,'DolarBlue')
    e_texto.delete(0,END)
    e_texto.insert(0,pred)


#Botones
boton0=Button(ventana,text='0',width=5,height=2, command=lambda: numero('0'))
boton1=Button(ventana,text='1',width=5,height=2, command=lambda: numero('1'))
boton2=Button(ventana,text='2',width=5,height=2, command=lambda: numero('2'))
boton3=Button(ventana,text='3',width=5,height=2, command=lambda: numero('3'))
boton4=Button(ventana,text='4',width=5,height=2, command=lambda: numero('4'))
boton5=Button(ventana,text='5',width=5,height=2, command=lambda: numero('5'))
boton6=Button(ventana,text='6',width=5,height=2, command=lambda: numero('6'))
boton7=Button(ventana,text='7',width=5,height=2, command=lambda: numero('7'))
boton8=Button(ventana,text='8',width=5,height=2, command=lambda: numero('8'))
boton9=Button(ventana,text='9',width=5,height=2, command=lambda: numero('9'))

boton_punt=Button(ventana,text='.',width=5,height=2, command=lambda: click_boton('.'))
boton_=Button(ventana,text='-',width=5,height=2, command=lambda: numero('-'))

boton_borrar=Button(ventana,text='◁',width=5,height=2, command=lambda: borrar())
boton_borrarTodo=Button(ventana,text='AC',width=5,height=2, command=lambda: borrarTodo())

boton_actualizar=Button(ventana,text='↓',width=5,height=2, command=lambda: actualizar(),bg='#aaaaaa')
boton_DO=Button(ventana,text='DO',width=5,height=2, command=lambda: DO(),bg='#aaaaaa')
boton_DB=Button(ventana,text='DB',width=5,height=2, command=lambda: DB(),bg='#aaaaaa')


boton0.grid(row = 1,column = 0,padx=px,pady=py)
boton1.grid(row = 1,column = 1,padx=px,pady=py)
boton2.grid(row = 1,column = 2,padx=px,pady=py)
boton3.grid(row = 1,column = 3,padx=px,pady=py)
boton_borrar.grid(row = 1,column = 4,padx=px,pady=py)
boton_borrarTodo.grid(row = 1,column = 5,padx=px,pady=py)

boton4.grid(row = 2,column = 0,padx=px,pady=py)
boton5.grid(row = 2,column = 1,padx=px,pady=py)
boton6.grid(row = 2,column = 2,padx=px,pady=py)
boton7.grid(row = 2,column = 3,padx=px,pady=py)
boton_DO.grid(row = 2,column = 4,padx=px,pady=py)
boton_actualizar.grid(row = 2,column = 5,padx=px,pady=py)

boton8.grid(row = 3,column = 0,padx=px,pady=py)
boton9.grid(row = 3,column = 1,padx=px,pady=py)
boton_punt.grid(row = 3,column = 2,padx=px,pady=py)
boton_.grid(row = 3,column = 3,padx=px,pady=py)
boton_DB.grid(row = 3,column = 4,padx=px,pady=py)

ventana.mainloop()


