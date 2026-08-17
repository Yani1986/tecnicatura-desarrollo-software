ingresos = float(input("ingrese su ingreso mensual: "))
vivienda = float(input("ingrese el costo de su vivienda: "))
alimentos = float(input("ingrese el costo de sus alimentos: "))
transporte = float(input("ingrese el costo de su transporte: "))
servicios = float(input("ingrese el costo de sus servicios: "))
otros_gastos = float(input("ingrese el costo de otros gastos: "))
gastos_totales = vivienda + alimentos + transporte + servicios + otros_gastos
saldo = ingresos - gastos_totales
print("Gastos totales:" , gastos_totales)
print("Saldo:" , saldo)