"""
Métodos

Estos son algunos ejemplos diseñados para que los estudiantes entiendan e implementen 
varios métodos de representación:

Representación estática

Escenario: Registro de estudiantes universitarios.

Tarea: Crear un programa utilizando una estructura de datos estática (como una lista o un 
diccionario) para almacenar información sobre los estudiantes. El programa 
debe permitir a los usuarios:

Añadir nuevos estudiantes: incluye el nombre, el CI, la carrera. 
Búsqueda de estudiantes: por nombre, ci y registro. Mostrar todos los estudiantes: De forma formateada. 
"""
#Diccionario para almacenar los datos de los estudiantes

students = {}

#Funcion para agregar estudiantes

def add_student(id, name, ci, university_degree ):
    students[id] = {'name': name, 'ci':ci, 'university_degree':university_degree}

def search_student(query):
    result = [] #lista
    for id, student_info in students.items():
        if query in student_info['name'] or query in student_info['ci'] or query == id:
            result.append(student_info)
    return result

def display_students():
    for id, student_info in students.items():
        print(f"ID: {id}, CI: {student_info['ci']}, Name: {student_info['name']}, University Dagree: {student_info['university_degree']}")
    
    
# Agregar estudiantes universitarios
add_student("221089748", "PAOLA ANDREA MURGUIA DURAN", "13434744", "Ingeniería en Sistemas")
add_student("221089749", "MARIA CRISTINA DURAN PEINADO", "3232244", "Ingeniería Informatica")

search_result = search_student("3232244")
print(search_result)

display_students()


"""
Dinámico

Representación Escenario: Simulación de una cuenta bancaria.

Tarea: Cree un programa que utilice una estructura de datos dinámica (como una lista) 
para representar el historial de transacciones de un estudiante al adicionar y retirar 
materias. El programa debe permitir a los usuarios:

Adicionar materia: Agregue un registro de transacción con la materia a adicionar. 
Retirar materia: Agregue un registro de transacción con la materia a retirar. 
Ver historial de transacciones: muestra todas las transacciones en orden cronológico. 
Verificar boleta de inscripcion: Muestra que materias el estudiante tine inscritas.
"""
transactions = []

def add_subject(subject):
  transactions.append({'type': 'add', 'subject': subject})

def withdraw_subject(subject):
  transactions.append({'type': 'withdrawal', 'subject': subject})

def view_history():
  for transaction in transactions:
    print(f"{transaction['type'].capitalize()}: {transaction['subject']}")
    #capitalize convierte la primera letra en mayuscula
def check_ticket():
  Registration_Slip = []
  for transaction in transactions:
    if transaction['type'] == 'add':
        Registration_Slip.append( transaction['subject'])
    elif transaction['type'] == 'withdrawal':
        Registration_Slip.remove(transaction['subject'])
  return Registration_Slip

# Example usage
add_subject("ESTRUCTURA DE DATOS I")
withdraw_subject("ESTRUCTURA DE DATOS I")
add_subject("BASE DE DATOS I")
add_subject("PROBABILIDAD Y ESTADISTICA II")


view_history()
print(f"Registration Slip: {check_ticket()}")

"""Persistente

Representación Escenario: Creación de una aplicación de agenda de contactos persistente,.

Tarea: Desarrollar un programa que almacene una lista de agenda de contactos de forma 
persistente utilizando un archivo JSON. 
El programa debe permitir a los usuarios:

Agregar contacto: Agregar un contacto con nombre, teléfono y correo.
Buscar un contacto por nombre.
Mostrar todos los contactos guardados.
Guardar y cargar los contactos desde un archivo JSON (contacts.json).
"""
filename = "D:/Materias/Semestre 1-2025/ESTRUCTURA DE DATOS I/INF220-SI/Tareas/TAREA_2/contacts.txt"

def load_contacts():
    """Carga los contactos desde un archivo de texto."""
    global filename
    contacts = []
    try:
        with open(filename, "r") as file:
            for line in file:
                name, phone, email = line.strip().split("|")
                contacts.append({"name": name, "phone": phone, "email": email})
    except FileNotFoundError:
        pass  # Si el archivo no existe, retorna una lista vacía
    return contacts

def save_contacts(contacts):
    global filename
    """Guarda los contactos en un archivo de texto."""
    with open(filename, "w") as file:
        for contact in contacts:
            file.write(f"{contact['name']}|{contact['phone']}|{contact['email']}\n")

def add_contact(contacts, name, phone, email):
    """Añade un nuevo contacto a la lista."""
    contacts.append({"name": name, "phone": phone, "email": email})

def search_contact(contacts, name):
    """Busca un contacto por nombre."""
    results = [contact for contact in contacts if name.lower() in contact["name"].lower()]
    return results

def view_contacts(contacts):
    """Muestra todos los contactos guardados."""
    if not contacts:
        print("No hay contactos guardados.")
        return
    for index, contact in enumerate(contacts, start=1):
        print(f"{index}. {contact['name']} - {contact['phone']} - {contact['email']}")

# Ejemplo de uso
contacts = load_contacts()

add_contact(contacts, "Juan Pérez", "555-1234", "juan@example.com")
add_contact(contacts, "María López", "555-5678", "maria@example.com")

view_contacts(contacts)

found_contacts = search_contact(contacts, "Juan")
print("\nResultados de búsqueda:")
for contact in found_contacts:
    print(f"{contact['name']} - {contact['phone']} - {contact['email']}")

save_contacts(contacts)


"""Simulado

Representación Escenario: Modelado de una intersección de tráfico.

Tarea: Crear un programa que simule una intersección de tráfico con semáforos y coches. 
Utilizar objetos para representar coches y semáforos. El programa debe:

Crear coches: Con horarios de llegada y direcciones aleatorios. Controle los semáforos: 
Cambie los semáforos a intervalos regulares. Mover coches: Basado en las señales de los 
semáforos y las posiciones de los coches. Mostrar la intersección: represente visualmente 
los coches y los semáforos (por ejemplo, utilizando una salida basada en texto). 
Ejemplo (simplificado):

Funcionalidades:
Coches llegan aleatoriamente con direcciones al azar.
Semáforos cambian de color cada ciertos segundos.
Coches se mueven solo cuando el semáforo está en verde.
Se muestra el estado de la intersección en consola.
"""

import random
import time

class Car:
    def __init__(self, direction):
        self.direction = direction
        self.position = 0  # Posición inicial en la intersección
    
    def move(self):
        self.position += 1  # Avanza si el semáforo está en verde

class TrafficLight:
    def __init__(self):
        self.color = "red"
    
    def change_color(self):
        self.color = "green" if self.color == "red" else "red"

def display_intersection(cars, traffic_light):
    """Muestra el estado de la intersección en la consola."""
    print("\n--- Estado de la Intersección ---")
    print(f"🚦 Semáforo: {traffic_light.color.upper()}")
    if not cars:
        print("🚗 No hay coches en la intersección.")
    else:
        for i, car in enumerate(cars):
            print(f"🚗 Coche {i+1}: Dirección {car.direction}, Posición {car.position}")

# Inicializar semáforo y lista de coches
traffic_light = TrafficLight()
cars = []

# Simulación de 10 ciclos de tráfico
for _ in range(10):
    time.sleep(1)  # Simula el paso del tiempo
    
    # Posibilidad de que un coche llegue a la intersección (50% de probabilidad)
    if random.random() < 0.5:
        direction = random.choice(["Norte", "Sur", "Este", "Oeste"])
        cars.append(Car(direction))
    
    # Cambiar el semáforo cada 3 ciclos
    if _ % 3 == 0:
        traffic_light.change_color()
    
    # Mover los coches si el semáforo está en verde
    if traffic_light.color == "green":
        for car in cars:
            car.move()
    
    # Mostrar el estado de la intersección
    display_intersection(cars, traffic_light)
    
    # Eliminar coches que han cruzado la intersección
    cars = [car for car in cars if car.position < 3]  # Se elimina cuando llega a 3

print("\n🔚 Fin de la simulación.")
