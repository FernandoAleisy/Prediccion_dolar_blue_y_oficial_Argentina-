import unittest
import os
import checkpoint as ch

class HenryChallenge(unittest.TestCase):
    
    def test_ListaDivisibles_01(self):
      lista_test = ch.ListaDivisibles(12, 10)
      lista_esperada = []
      self.assertEqual(lista_test, lista_esperada)

    def test_ListaDivisibles_02(self):
      lista_test = ch.ListaDivisibles(12, 100)
      lista_esperada = [12,24,36,48,60,72,84,96]
      self.assertEqual(lista_test, lista_esperada)

    def test_ListaDivisibles_03(self):
      lista_test = ch.ListaDivisibles(3, 9)
      lista_esperada = [3,6,9]
      self.assertEqual(lista_test, lista_esperada)

    def test_Exponente_01(self):
      valor_test = ch.Exponente(10, 2)
      valor_esperado = 100
      self.assertEqual(valor_test, valor_esperado)

    def test_Exponente_02(self):
      valor_test = ch.Exponente(49, 0.5)
      valor_esperado = 7
      self.assertEqual(valor_test, valor_esperado)

    def test_Exponente_03(self):
      valor_test = ch.Exponente(3, 0)
      valor_esperado = 1
      self.assertEqual(valor_test, valor_esperado)

    def test_ListaDeListas_01(self):
      lista_test = ch.ListaDeListas(100)
      lista_esperada = None
      self.assertEqual(lista_test, lista_esperada)

    def test_ListaDeListas_02(self):
      lista_test = ch.ListaDeListas([1,[2,3],[[4,5],6],[[7]]])
      lista_esperada = [1,2,3,4,5,6,7]
      self.assertEqual(lista_test, lista_esperada)

    def test_ListaDeListas_03(self):
      lista_test = ch.ListaDeListas(['a','b',1,2,['a1','b3'],[['a'],2]])
      lista_esperada = ['a','b',1,2,'a1','b3','a',2]
      self.assertEqual(lista_test, lista_esperada)

    def test_ListaDeListas_04(self):
      lista_test = ch.ListaDeListas([[[1]],2,[[[[3]]]]])
      lista_esperada = [1,2,3]
      self.assertEqual(lista_test, lista_esperada)

    def test_Factorial_01(self):
      valor_test = ch.Factorial(5)
      valor_esperado = 120
      self.assertEqual(valor_test, valor_esperado)

    def test_Factorial_02(self):
      valor_test = ch.Factorial(1)
      valor_esperado = 1
      self.assertEqual(valor_test, valor_esperado)

    def test_Factorial_03(self):
      valor_test = ch.Factorial(0)
      valor_esperado = 1
      self.assertEqual(valor_test, valor_esperado)

    def test_Factorial_04(self):
      valor_test = ch.Factorial(9)
      valor_esperado = 362880
      self.assertEqual(valor_test, valor_esperado)

    def test_ListaPrimos_01(self):
      lista_test = ch.ListaPrimos(1,11)
      lista_esperada = [1,2,3,5,7,11]
      self.assertEqual(lista_test, lista_esperada)
      
    def test_ListaPrimos_02(self):
      lista_test = ch.ListaPrimos('0',0)
      lista_esperada = None
      self.assertEqual(lista_test, lista_esperada)

    def test_ListaPrimos_03(self):
      lista_test = ch.ListaPrimos(66,77)
      lista_esperada = [67, 71, 73]
      self.assertEqual(lista_test, lista_esperada)

    def test_ListaPrimos_04(self):
      lista_test = ch.ListaPrimos(0,'66')
      lista_esperada = None
      self.assertEqual(lista_test, lista_esperada)

    def test_ListaRepetidos_01(self):
      lista_test = ch.ListaRepetidos(['hola', 'mundo', 'hola']) 
      lista_esperada = [('hola',2),('mundo',1)]
      self.assertEqual(lista_test, lista_esperada)

    def test_ListaRepetidos_02(self):
      lista_test = ch.ListaRepetidos([10,11,11,12,15,17,20,20])
      lista_esperada = [(10,1),(11,2),(12,1),(15,1),(17,1),(20,2)]
      self.assertEqual(lista_test, lista_esperada)

    def test_ListaRepetidos_03(self):
      lista_test = ch.ListaRepetidos((1,2,3,3))
      lista_esperada = None
      self.assertEqual(lista_test, lista_esperada)

    def test_ClaseVehiculo_01(self):
      a = ch.ClaseVehiculo('auto','verde')
      valor_test = a.Acelerar(10)
      valor_test = a.Acelerar(100)
      valor_test = a.Acelerar(-20)
      valor_esperado = 80
      self.assertEqual(valor_test, valor_esperado)

    def test_ClaseVehiculo_02(self):
      a = ch.ClaseVehiculo('camioneta','azul')
      valor_test = a.Acelerar(20)
      valor_test = a.Acelerar(-30)
      valor_esperado = 0
      self.assertEqual(valor_test, valor_esperado)

    def test_ClaseVehiculo_03(self):
      a = ch.ClaseVehiculo('moto','negra')
      valor_test = a.Acelerar(10)
      valor_test = a.Acelerar(100)
      valor_esperado = 100
      self.assertEqual(valor_test, valor_esperado)

resultado_test = unittest.main(argv=[''], verbosity=2, exit=False)

hc_tests = resultado_test.result.testsRun
hc_fallas = len(resultado_test.result.failures)
hc_errores = len(resultado_test.result.errors)
hc_ok = hc_tests - hc_fallas - hc_errores

class HenryChallenge_ExtraCredit(unittest.TestCase):

    def test_OrdenarDiccionario_01(self):
      dicc = {'clave1':['c','a','b'], 'clave2':['casa','auto','barco'], 'clave3':[1,2,3]}
      valor_test = ch.OrdenarDiccionario(dicc, 'clave1')
      valor_esperado = {'clave1':['a','b','c'], 'clave2':['auto','barco','casa'], 'clave3':[2,3,1]}
      self.assertEqual(valor_test, valor_esperado)

    def test_OrdenarDiccionario_02(self):
      dicc = ['c','a','b']
      valor_test = ch.OrdenarDiccionario(dicc, 'clave1', True)
      valor_esperado = None
      self.assertEqual(valor_test, valor_esperado)

    def test_OrdenarDiccionario_03(self):
      dicc = {'clave1':['c','a','b'], 'clave2':['casa','auto','barco'], 'clave3':[3,1,2]}
      valor_test = ch.OrdenarDiccionario(dicc, 'clave3', False)
      valor_esperado = {'clave1':['b','a','c'], 'clave2':['barco','auto','casa'], 'clave3':[3,2,1]}
      self.assertEqual(valor_test, valor_esperado)

resultado_test = unittest.main(argv=[''], verbosity=2, exit=False)
hce_tests = resultado_test.result.testsRun - hc_tests
hce_fallas = len(resultado_test.result.failures) - hc_fallas
hce_errores = len(resultado_test.result.errors) - hc_errores
hce_ok = hce_tests - hce_fallas - hce_errores

archivo_test = open('resultado_test.csv', 'w')
archivo_test.write('Tipo,Total_Tests,Total_Fallas,Total_Errores,Total_Correctos\n')
archivo_test.write('Credit,'+str(hc_tests)+','+str(hc_fallas)+','+str(hc_errores)+','+str(hc_ok)+'\n')
archivo_test.write('ExtraCredit,'+str(hce_tests)+','+str(hce_fallas)+','+str(hce_errores)+','+str(hce_ok)+'\n')
archivo_test.close()

print('Resumen')
print('Total Tests:', str(hc_tests))
print('Total Fallas:', str(hc_fallas))
print('Total Errores:', str(hc_errores))
print('Total Correctos:', str(hc_ok))

print('Resumen Extra Credit')
print('Total Tests:', str(hce_tests))
print('Total Fallas:', str(hce_fallas))
print('Total Errores:', str(hce_errores))
print('Total Correctos:', str(hce_ok))