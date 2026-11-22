# Clase Reserva
# Integra cliente, servicio, duración y estado.

from datetime import datetime
from excepciones import DatosInvalidosError, OperacionNoPermitidaError, ReservaInvalidaError


class Reserva:
    """Clase que representa una reserva realizada por un cliente."""

    def __init__(self, id_reserva, cliente, servicio, horas):
        self._id_reserva = id_reserva
        self._cliente = cliente
        self._servicio = servicio
        self._horas = horas
        self._estado = "Pendiente"
        self._fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.validar_reserva()

    @property
    def id_reserva(self):
        return self._id_reserva

    @property
    def estado(self):
        return self._estado

    def validar_reserva(self):
        """Valida los datos básicos de la reserva."""
        if self._cliente is None:
            raise ReservaInvalidaError("La reserva debe tener un cliente válido.")
        if self._servicio is None:
            raise ReservaInvalidaError("La reserva debe tener un servicio válido.")
        try:
            horas = float(self._horas)
        except (TypeError, ValueError) as e:
            raise DatosInvalidosError("La duración de la reserva debe ser numérica.") from e
        if horas <= 0:
            raise ReservaInvalidaError("La duración de la reserva debe ser mayor que cero.")
        self._horas = horas
        # También valida disponibilidad del servicio
        self._servicio.validar_disponibilidad()

    def confirmar(self):
        """Confirma la reserva si está pendiente."""
        if self._estado != "Pendiente":
            raise OperacionNoPermitidaError("Solo se pueden confirmar reservas pendientes.")
        self._estado = "Confirmada"
        return f"Reserva {self._id_reserva} confirmada."

    def cancelar(self):
        """Cancela la reserva si no ha sido procesada."""
        if self._estado == "Procesada":
            raise OperacionNoPermitidaError("No se puede cancelar una reserva ya procesada.")
        self._estado = "Cancelada"
        return f"Reserva {self._id_reserva} cancelada."

    def procesar(self, impuesto=0, descuento=0):
        """Procesa la reserva y calcula el costo total."""
        try:
            if self._estado != "Confirmada":
                raise OperacionNoPermitidaError("Solo se pueden procesar reservas confirmadas.")
            # Polimorfismo: cada servicio calcula el costo a su manera
            total = self._servicio.calcular_costo(self._horas, impuesto=impuesto, descuento=descuento)
            self._estado = "Procesada"
            return total
        except Exception as e:
            # Encadenamiento de excepción para dar contexto
            raise ReservaInvalidaError(f"No se pudo procesar la reserva {self._id_reserva}.") from e

    def mostrar_detalle(self):
        return (
            f"Reserva {self._id_reserva} | Cliente: {self._cliente.nombre} | "
            f"Servicio: {self._servicio.nombre} | Horas: {self._horas} | "
            f"Estado: {self._estado} | Fecha: {self._fecha}"
        )
