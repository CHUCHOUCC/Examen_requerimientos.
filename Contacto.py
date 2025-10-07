

class Contacto:
    
    contactos = {}

    contactos_listados = []

    def __init__(self, nombre, email, telefono):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email
    def interfaz(self,opcion):
        print("Bienvenido a la agenda de contactos")
        print("Seleccione una opción:")
        print("1. Registrar contacto")
        print("2. Encontrar contacto por nombre")
        print("3. Encontrar contacto por email")
        print("4. Listar contactos")
        print("5. Eliminar contacto")

        opcion = input("Ingrese el número de la opción deseada: ")
            

        def registrar_contacto(self):
            # Programa que permite registrar un contacto
            print("Registro de Contacto")
            self.nombre = input("Ingrese el nombre: ")
            self.telefono = input("Ingrese el teléfono: ")
            self.email = input("Ingrese el email: ")
            print("Contacto registrado exitosamente.")

        def encontrar_contacto_por_nombre(self, nombre):
            # Programa que permite encontrar un contacto por su nombre
            for nombre in Contacto.contactos.keys():
                nombre = input("Ingrese el nombre del contacto a buscar: ")
                if self.nombre.lower() == nombre.lower():
                    print("Contacto encontrado:")
                    print(Contacto.contactos[nombre])
                else:
                    print("Contacto no encontrado.")

        def encontrar_contacto_por_email(self, email):
            # Programa que permite encontrar un contacto por su teléfono
            for email, telefono in Contacto.contactos.values():
                email = input("Ingrese el email del contacto a buscar: ")
                if self.email == email:
                    for nombre, (email,telefono) in Contacto.contactos.items():
                        if self.email == email:

                            print("Contacto encontrado:")
                            print(nombre)
                else:
                    print("Contacto no encontrado.")

        def listar_contactos(self,contactos_listados):
            # Programa que permite listar todos los contactos
            print("Lista de Contactos:")
            for nombre in Contacto.contactos.keys():
                nombre = input("Ingrese el nombre del contacto a listar: ")
                if nombre not in contactos_listados:
                    contactos_listados.append(nombre)
                    print("contacto listado exitosamente.")

                else:
                    print("El contacto ya ha sido listado.")

        def eliminar_contacto(self, nombre):
            # Programa que permite eliminar un contacto
            nombre = input("Ingrese el nombre del contacto a eliminar: ")
            if nombre in Contacto.contactos:
                del Contacto.contactos[nombre]
                print("Contacto eliminado exitosamente.")
            else:
                print("Contacto no encontrado.")


        if opcion == '1':
            return registrar_contacto(self)
        
        elif opcion == '2':
            return encontrar_contacto_por_nombre(self, self.nombre)
        
        elif opcion == '3':
            return encontrar_contacto_por_email(self, self.email)
        
        elif opcion == '4':
            return listar_contactos(self, Contacto.contactos_listados)
        
        elif opcion == '5':
            return eliminar_contacto(self, self.nombre)
        
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")





    

    
    