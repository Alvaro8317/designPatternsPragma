from abc import ABC, abstractmethod

# Clase Target
class Conexion:

    def __init__(self, url):
        self.url = url

    def conectar(self):
        print(f"Conectando con {self.url}")


# Clase Adaptee//Adaptado
class ConexionLDAP:

    def __init__(self, servidor, puerto):
        self.servidor = servidor
        self.puerto = puerto

    def conectar_ldap(self):
        print(f"Conectando con servidor LDAP {self.servidor}:{self.puerto}")


# Clase Adapter
class AdaptadorLDAP(Conexion):

    def __init__(self, servidor, puerto):
        self.ldap = ConexionLDAP(servidor, puerto)

    def conectar(self):
        self.ldap.conectar_ldap()


# Ejemplo de uso del patrón Adapter
if __name__ == '__main__':
    # Crear una conexión a una URL utilizando la clase Target
    conexion = Conexion("http://www.ejemplo.com")
    conexion.conectar()

    # Crear una conexión a un servidor LDAP utilizando la clase Adapter
    conexion_ldap = AdaptadorLDAP("ldap.ejemplo.com", 389)
    conexion_ldap.conectar()
