def validar_edad(edad_str):
    try:
        edad = int (edad_str)
        return edad > 0
    except ValueError:
     return False
    
def validacion_nombre(nombre):
    return len(nombre.strip())>0

def validacion_nota(nota_str):
    try:
        nota = float("nota_str")
        return 1.0 <= nota <= 7.0
    except ValueError:
        return False


def menu():
    while True:
      print ("========== MENÚ PRINCIPAL ==========")
      print ("1. Agregar estudiante")
      print ("2. buscar estudiante")
      print ("3. eliminar estudiante")
      print ("4. actualizar estados")
      print ("5. mostrar estudiante")
      print ("6. salir")
      print("=====================================")

def opciones():
   while True:
    try:
        opcion = int(input(" ingrese la opcion que desea (1-6)"))
        if 1 <= opcion <= 6:
                return opcion
        else:
                print(" Error opcion no valida , escoga una existente")
    except ValueError:
        print("error debe colocar un numero entero")

def agregar(lista_de_estudiante):
    print(" Agrega a un estudiante")
    nombre_str = input(" ingrese el nombre del estudiante")
    edad_str = input(" ingrese la edad del estudiante")
    nota_str = input("ingrese la nota del estudiante")

    if not validacion_nombre (nombre_str):
        print(" error el nombre no puede tener espacios o estar vacio")
    if not validar_edad (edad_str):
        print("error debe ingresa una edad valida")
    if not validacion_nota (nota_str):
        print("error debe poner una nota valida")

def validar_nombre(nombre):
 return len(nombre.strip()) > 0



def validar_edad(edad_str):

  try:
    edad = int(edad_str)
    return edad > 0
  except ValueError:
    return False



def validar_nota(nota_str):
  try:
    nota = float(nota_str)
    return 1.0 <= nota <= 7.0
  except ValueError:
    return False

def mostrar_menu():
  print("\n========== MENÚ PRINCIPAL ==========")
  print("1. Agregar estudiante")
  print("2. Buscar estudiante")
  print("3. Eliminar estudiante")
  print("4. Actualizar estados")
  print("5. Mostrar estudiantes")
  print("6. Salir")
  print("=====================================")



def leer_opcion():
  while True:
    try:
      opcion = int(input("Ingrese su opción (1-6): "))
      if 1 <= opcion <= 6:
        return opcion
      else:
        print("Opción inválida. Ingrese un número entre 1 y 6.")

    except ValueError:
      print("Error: Por favor ingrese un número entero.")





def agregar_estudiante(lista_estudiantes):
  print("\n--- Agregar Nuevo Estudiante ---")
  nombre = input("Ingrese el nombre completo: ")
  edad_str = input("Ingrese la edad: ")
  nota_str = input("Ingrese la nota (1.0 a 7.0): ")

  if not validar_nombre(nombre):
    print("Error: El nombre no puede estar vacío ni contener solo espacios.")
    return
  if not validar_edad(edad_str):
    print("Error: La edad debe ser un número entero mayor que cero.")
    return
  if not validar_nota(nota_str):
    print("Error: La nota debe ser un número decimal entre 1.0 y 7.0.")
    return

  nuevo_estudiante = {
    "nombre": nombre,
    "edad": int(edad_str),
    "nota": float(nota_str),
    "aprobado": False 
  }

  lista_estudiantes.append(nuevo_estudiante)
  print("Estudiante registrado con éxito.")

def buscar_estudiante(lista_estudiantes, nombre_buscado):
  for i in range(len(lista_estudiantes)):
    if lista_estudiantes[i]["nombre"].lower() == nombre_buscado.lower():
      return i
  return -1

def actualizar_estados(lista_estudiantes):
  for estudiante in lista_estudiantes:
    if estudiante["nota"] >= 4.0:
      estudiante["aprobado"] = True

    else:
      estudiante["aprobado"] = False

def mostrar_estudiantes(lista_estudiantes):
  if len(lista_estudiantes) == 0:
    print("No hay estudiantes registrados actualmente.")
    return
  actualizar_estados(lista_estudiantes)

  print("\n=== LISTA DE ESTUDIANTES ===")
  for estudiante in lista_estudiantes:
    print(f"Nombre: {estudiante['nombre']}")
    print(f"Edad: {estudiante['edad']}")
    print(f"Nota: {estudiante['nota']}")

    estado_texto = "APROBADO" if estudiante["aprobado"] else "REPROBADO"
    print(f"Estado: {estado_texto}")
    print("********************************************")

def main():

  estudiantes = []
  while True:
    mostrar_menu()
    opcion = leer_opcion()

    if opcion == 1:
      agregar_estudiante(estudiantes)

    elif opcion == 2:
      nombre_a_buscar = input("\nIngrese el nombre del estudiante a buscar: ")
      posicion = buscar_estudiante(estudiantes, nombre_a_buscar)

      if posicion != -1:
        est = estudiantes[posicion]
        print(f"\n¡Estudiante encontrado en la posición {posicion} de la lista!")
        print(f"Datos -> Nombre: {est['nombre']} | Edad: {est['edad']} | Nota: {est['nota']} | Aprobado: {est['aprobado']}")
      else:
        print(f"\nEl estudiante '{nombre_a_buscar}' no se encuentra registrado.")

    elif opcion == 3:
      nombre_a_eliminar = input("\nIngrese el nombre del estudiante a eliminar: ")
      posicion = buscar_estudiante(estudiantes, nombre_a_eliminar)

      if posicion != -1:
        estudiantes.pop(posicion)
        print(f"Estudiante '{nombre_a_eliminar}' eliminado del sistema con éxito.")
      else:
        print(f"\nEl estudiante '{nombre_a_eliminar}' no se encuentra registrado.")

    elif opcion == 4:
      actualizar_estados(estudiantes)
      print("\nLos estados de aprobación han sido actualizados en base a las notas.")

    elif opcion == 5:
      mostrar_estudiantes(estudiantes)



    elif opcion == 6:
      print("\nGracias por usar el sistema. Vuelva Pronto")
      break

if __name__ == "__main__":

  main()





  




       


    
