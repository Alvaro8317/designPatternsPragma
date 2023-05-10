from abc import ABC, abstractmethod

# Interfaz de Subject
class Subject(ABC):
    """
    La interfaz Subject define las operaciones que el Proxy y el RealSubject
    deben implementar.
    """

    @abstractmethod
    def request(self) -> None:
        pass

# RealSubject
class RealSubject(Subject):
    """
    La clase RealSubject define el objeto real que el Proxy representa.
    """

    def request(self) -> None:
        print("RealSubject: Manejando la petición.")

# Proxy
class Proxy(Subject):
    """
    La clase Proxy tiene una referencia al objeto RealSubject y actúa como un
    intermediario entre el cliente y el RealSubject.
    """

    def __init__(self, real_subject: RealSubject) -> None:
        self._real_subject = real_subject

    def request(self) -> None:
        if self.check_access():
            self._real_subject.request()
            self.log_access()

    def check_access(self) -> bool:
        print("Proxy: Verificando el acceso antes de enviar la petición al RealSubject.")
        return True

    def log_access(self) -> None:
        print("Proxy: Registrando el momento de la petición.")

# Cliente
def client_code(subject: Subject) -> None:
    """
    El código del cliente puede interactuar con el Proxy o el RealSubject a
    través de la interfaz Subject.
    """
    subject.request()

if __name__ == "__main__":
    real_subject = RealSubject()
    proxy = Proxy(real_subject)

    # El cliente utiliza el Proxy en lugar del RealSubject directamente.
    client_code(proxy)
