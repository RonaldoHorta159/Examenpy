import unittest

#  pruebas
class TestMCD(unittest.TestCase):
    
    def test_mcd_dos_numeros(self):
        self.assertEqual(mcd(48, 18), 6)
        self.assertEqual(mcd(1071, 462), 21)
    
    def test_mcd_cuatro_numeros(self):
        self.assertEqual(mcd_de_cuatro(48, 18, 24, 30), 6)
        self.assertEqual(mcd_de_cuatro(12, 24, 18, 30), 6)
        self.assertEqual(mcd_de_cuatro(14, 28, 35, 70), 7)

# Función para el MCD de dos números
def mcd(a, b):
    if b == 0:
        return a
    else:
        return mcd(b, a % b)

# Función para el MCD de cuatro números
def mcd_de_cuatro(a, b, c, d):
    return mcd(mcd(mcd(a, b), c), d)


if __name__ == "__main__":
    
    opcion = input("¿Quieres ejecutar las pruebas (T) o calcular MCD interactivo (M)? ").strip().lower()
    
    if opcion == 't':
        
        unittest.main()
    elif opcion == 'm':
       
        num1 = int(input("Ingresa el primer número: "))
        num2 = int(input("Ingresa el segundo número: "))
        
        
        mcd_actual = mcd(num1, num2)
        print(f"El MCD de {num1} y {num2} es: {mcd_actual}")
        
        
        num3 = int(input("Ingresa el tercer número: "))
        mcd_actual = mcd(mcd_actual, num3)
        print(f"El MCD ahora con {num3} es: {mcd_actual}")
        
        
        num4 = int(input("Ingresa el cuarto número: "))
        mcd_actual = mcd(mcd_actual, num4)
        print(f"El MCD final con {num4} es: {mcd_actual}")
    else:
        print("Opción no válida.")

