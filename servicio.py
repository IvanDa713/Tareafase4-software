# Clase abstracta Servicio y servicios especializados
# Aquí se aplica herencia, polimorfismo y sobrecarga simulada.

from abc import ABC, abstractmethod
from excepciones import DatosInvalidosError, ServicioNoDisponibleError


class Servicio(ABC):
    """Clase abstracta que define la estructura de un servicio."""

    def __init__(self, codigo, nombre, costo_base, disponible=True):
        self._codigo = codigo
        self._nombre = nombre
        self._disponible = disponible
        self.costo_base = costo_base  # usa el setter para validar

    @property
    def codigo(self):
        return self._codigo

    @property
    def nombre(self):
        return self._nombre

    @property
    def disponible(self):
        return self._disponible

    @property
    def costo_base(self):
        return self._costo_base

    @costo_base.setter
    def costo_base(self, valor):
        try:
            valor = float(valor)
        except (TypeError, ValueError) as e:
            # Encadenamiento de excepción
            raise DatosInvalidosError("El costo base debe ser un número válido.") from e
        if valor <= 0:
            raise DatosInvalidosError("El costo base debe ser mayor que cero.")
        self._costo_base = valor

    def validar_disponibilidad(self):
        """Valida si el servicio está disponible."""
        if not self._disponible:
            raise ServicioNoDisponibleError(f"El servicio '{self.nombre}' no está disponible.")
        return True

    @abstractmethod
    def calcular_costo(self, horas, impuesto=0, descuento=0):
        """Calcula el costo del servicio. Método polimórfico."""
        pass

    @abstractmethod
    def describir_servicio(self):
        """Describe el servicio. Método polimórfico."""
        pass


class ReservaSala(Servicio):
    """Servicio especializado: reserva de salas."""

    def describir_servicio(self):
        return f"Reserva de Sala: {self.nombre} | Costo base por hora: {self.costo_base}"

    def calcular_costo(self, horas, impuesto=0, descuento=0):
        # Sobrecarga simulada: puede recibir solo horas, o también impuesto y descuento
        if horas <= 0:
            raise DatosInvalidosError("Las horas deben ser mayores que cero.")
        subtotal = self.costo_base * horas
        total = subtotal + (subtotal * impuesto) - (subtotal * descuento)
        if total < 0:
            raise DatosInvalidosError("El cálculo del costo no puede ser negativo.")
        return total


class AlquilerEquipo(Servicio):
    """Servicio especializado: alquiler de equipos."""

    def describir_servicio(self):
        return f"Alquiler de Equipo: {self.nombre} | Costo base por hora: {self.costo_base}"

    def calcular_costo(self, horas, impuesto=0, descuento=0):
        if horas <= 0:
            raise DatosInvalidosError("Las horas deben ser mayores que cero.")
        # Costo con recargo por logística del equipo
        subtotal = (self.costo_base * horas) + 5000
        total = subtotal + (subtotal * impuesto) - (subtotal * descuento)
        if total < 0:
            raise DatosInvalidosError("El cálculo del costo no puede ser negativo.")
        return total


class AsesoriaEspecializada(Servicio):
    """Servicio especializado: asesoría."""

    def describir_servicio(self):
        return f"Asesoría Especializada: {self.nombre} | Costo base por hora: {self.costo_base}"

    def calcular_costo(self, horas, impuesto=0, descuento=0):
        if horas <= 0:
            raise DatosInvalidosError("Las horas deben ser mayores que cero.")
        # La asesoría tiene una tarifa profesional adicional
        subtotal = (self.costo_base * horas) + 20000
        total = subtotal + (subtotal * impuesto) - (subtotal * descuento)
        if total < 0:
            raise DatosInvalidosError("El cálculo del costo no puede ser negativo.")
        return total
