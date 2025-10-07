

class Contacto:
    contactos = {}

    def __init__(self, nombre, email, telefono):
        self.nombre = nombre
        self.email = email
        self.telefono = telefono

    @classmethod
    def registrar_contacto(cls, nombre, email, telefono):
        if nombre in cls.contactos:
            print("El contacto ya existe.")
        else:
            cls.contactos[nombre] = Contacto(nombre, email, telefono)
            print("Contacto registrado exitosamente.")

    @classmethod
    def encontrar_contacto_por_nombre(cls, nombre):
        contacto = cls.contactos.get(nombre)
        if contacto:
            print(f"Nombre: {contacto.nombre}, Email: {contacto.email}, Teléfono: {contacto.telefono}")
        else:
            print("Contacto no encontrado.")

    @classmethod
    def encontrar_contacto_por_email(cls, email):
        for contacto in cls.contactos.values():
            if contacto.email == email:
                print(f"Nombre: {contacto.nombre}, Email: {contacto.email}, Teléfono: {contacto.telefono}")
                return
        print("Contacto no encontrado.")

    @classmethod
    def listar_contactos(cls):
        if not cls.contactos:
            print("No hay contactos registrados.")
        else:
            for contacto in cls.contactos.values():
                print(f"Nombre: {contacto.nombre}, Email: {contacto.email}, Teléfono: {contacto.telefono}")

    @classmethod
    def eliminar_contacto(cls, nombre):
        if nombre in cls.contactos:
            del cls.contactos[nombre]
            print("Contacto eliminado exitosamente.")
        else:
            print("Contacto no encontrado.")

    @classmethod
    def interfaz(cls):
        while True:
            print("\n--- Agenda de Contactos ---")
            print("1. Registrar contacto")
            print("2. Buscar contacto por nombre")
            print("3. Buscar contacto por email")
            print("4. Listar contactos")
            print("5. Eliminar contacto")
            print("6. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == '1':
                nombre = input("Nombre: ")
                email = input("Email: ")
                telefono = input("Teléfono: ")
                cls.registrar_contacto(nombre, email, telefono)
            elif opcion == '2':
                nombre = input("Nombre a buscar: ")
                cls.encontrar_contacto_por_nombre(nombre)
            elif opcion == '3':
                email = input("Email a buscar: ")
                cls.encontrar_contacto_por_email(email)
            elif opcion == '4':
                cls.listar_contactos()
            elif opcion == '5':
                nombre = input("Nombre a eliminar: ")
                cls.eliminar_contacto(nombre)
            elif opcion == '6':
                print("Saliendo...")
                break
            else:
                print("Opción no válida.")



Contacto.interfaz()    # Iniciar la interfaz de usuario
    

    
    