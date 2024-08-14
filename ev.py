#En una emprea de  petroleo se requiere el  siguientee personal:
# 3 ingerieros de petroleo, que tienen un rango salarial entre los 5 y 6.5M
# 2 tecnologos de obra  con un rango salarial entre los 3 y 4M, de acuerdo a la magnitud de la obra se requiere
# X perforadores X obreros X inspectores de obra 
# que cuenten con un rango salarial entre los 3 y 4.5M
#Realizar un programa en el cual me de el valor total  a pagar por el valor total de nomina teniendo en cuenta que se trabaja 30 dias
#los donomilicales tiene un valor de hora extra de 6,5% h
#Descuento : 
#Para fiscales son 4%
#Salud 4,5%
#Pension 0,6% de CCF (Cajas de Compensación Familiar)
#Si el Rango salarial supera  el 4.5 SMLV (Salario mínimo legal mensual vigente), aplicar una rete fuente de 4%
#Adicional: agregar nombre apelllido profesion y año de experiencia
#Si Años de experiencia supera 5 aplicar bonificacion de el 15%
import os

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')
Nombres = []
Salario = []
AnosExp = []
Profesion = []
HorasTrabajadas = []
HorasExtra = []
DescuentoSalud=0.45
DescuentoFiscal=0.4
DescuentoPension=0.06
Bonificacion=0.15 # si supera 5 años de experiencia
RenteFuente=0.4
BonificacionAnos= 0.15 # si supera 5 años de experiencia
SMLV=5850000

from colorama import Fore, Style

def imprimir_logo_con_color():
    """Prints a colorful logo to the console using Colorama."""

    logo = """
 ██████╗ █████╗ ██╗      ██████╗██╗   ██╗██╗      █████╗ ██████╗  ██████╗ ██████╗  █████╗ 
██╔════╝██╔══██╗██║     ██╔════╝██║   ██║██║     ██╔══██╗██╔══██╗██╔═══██╗██╔══██╗██╔══██╗
██║     ███████║██║     ██║     ██║   ██║██║     ███████║██║  ██║██║   ██║██████╔╝███████║
██║     ██╔══██║██║     ██║     ██║   ██║██║     ██╔══██║██║  ██║██║   ██║██╔══██╗██╔══██║
╚██████╗██║  ██║███████╗╚██████╗╚██████╔╝███████╗██║  ██║██████╔╝╚██████╔╝██║  ██║██║  ██║
 ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝
    """

    print(Fore.RED + Style.BRIGHT + logo + Style.RESET_ALL)

imprimir_logo_con_color()

print("Ingrese el numero de empleados especiales:")
emp = int(input())
limpiar_pantalla()

for i in range(0, emp):
    print("===============Empleados Especiales===============")
    print("Ingrese el nombre del empleado:")
    Nombres.append(input())
    print("Ingrese el salario del empleado:")
    Salario.append(int(input()))
    print("Ingrese los años de experiencia del empleado:")
    AnosExp.append(int(input()))
    print("Ingrese la profesión del empleado:")
    Profesion.append(input())
    print("Ingrese la cantidad de horas trabajadas:")
    HorasTrabajadas.append(int(input()))
    print("Ingrese la cantidad de horas extra(si no realiza horas extra, ingrese 0):")
    HorasExtra.append(int(input()))
    limpiar_pantalla()  

print("===============Personal de perforadores===============")
print("Ingrese el numero de perforadores:")
num = int(input())

for i in range(0, num):
    print("Ingrese el nombre del perforador:")
    Nombres.append(input())
    print("Ingrese el salario del perforador:")
    Salario.append(int(input()))
    limpiar_pantalla()  

print("===============Personal de obreros===============")

print("Ingrese el numero de obreros:")
num2 = int(input())

for i in range(0, num2):
    print("Ingrese el nombre del obrero:")
    Nombres.append(input())
    print("Ingrese el salario del obrero:")
    Salario.append(int(input()))
    limpiar_pantalla()  
    
print("===============Personal de inspectores===============")

print("Ingrese el numero de inspectores:")
num3 = int(input())

for i in range(0, num3):
    print("Ingrese el nombre del inspector:")
    Nombres.append(input())
    print("Ingrese el salario del inspector:")
    Salario.append(int(input()))
    limpiar_pantalla()

# Cálculo del salario total para cada empleado
BonificacionHorasExtra= (HorasExtra[i]* 0.65) #por hora
anos_exp = AnosExp[i]
salario= Salario[i]
horas_extra= HorasExtra[i]
for i in range(len(Salario)):
    # Cálculo de descuentos
    descuentos = Salario[i] * (DescuentoSalud + DescuentoFiscal + DescuentoPension)

    # Cálculo de bonificaciones
    bonificacion_anos = salario * BonificacionAnos if anos_exp > 5 else 0
    bonificacion_horas_extra = horas_extra * salario * BonificacionHorasExtra

    # Salario bruto
    salario_bruto = salario - descuentos + bonificacion_anos + bonificacion_horas_extra

    # Retención en la fuente
    salario_neto = salario_bruto * (1 - RenteFuente) if salario_bruto > SMLV else salario_bruto

    print(f"El salario total del empleado {i+1} es: {salario_neto}")


# Informmacion general

print("===============Informacion de los empleados===============")

indices_especiales = list(range(emp))

InfoEmpleadosEspeciales = len(indices_especiales)

for i in indices_especiales:
    print("Información del empleado especial:")
    print("Nombre:", Nombres[i])
    print("Profesión:", Profesion[i])
    print("Salario:", Salario[i])
    print("Años de experiencia:", AnosExp[i])

inicio_perforadores = emp
fin_perforadores = inicio_perforadores + num
inicio_obreros = fin_perforadores
fin_obreros = inicio_obreros + num2
inicio_inspectores = fin_obreros
fin_inspectores = inicio_inspectores + num3

print("===============Informacion de los perforadores===============")
for i in range(inicio_perforadores, fin_perforadores):
    print("Información del perforador:")
    print("Nombre:", Nombres[i])
    print("Salario:", Salario[i])

print("===============Informacion de los obreros===============")
for i in range(inicio_obreros, fin_obreros):
    print("Información del obrero:")
    print("Nombre:", Nombres[i])
    print("Salario:", Salario[i])

print("===============Informacion de los inspectores===============")
for i in range(inicio_inspectores, fin_inspectores):
    print("Información del inspector:")
    print("Nombre:", Nombres[i])
    print("Salario:", Salario[i])
