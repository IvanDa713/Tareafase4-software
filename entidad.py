# Clase abstracta base del sistema
# Define atributos y métodos comunes para las entidades.

from abc import ABC, abstractmethod


class Entidad(ABC):
    """Clase abstracta que representa una entidad general del sistema."""

    def __init__(self, identificador, nombre):
        # Encapsulación: atributos protegidos
        self._identificador = identificador
        self._nombre = nombre

    @property
    def identificador(self):
        """Retorna el identificador de la entidad."""
        return self._identificador

    @property
    def nombre(self):
        """Retorna el nombre de la entidad."""
        return self._nombre

    @abstractmethod
    def mostrar_informacion(self):
        """Método abstracto que deben implementar las clases hijas."""
        pass
