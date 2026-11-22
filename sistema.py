# Clase principal del sistema
# Administra clientes, servicios y reservas sin base de datos.

from excepciones import (
    ClienteNoEncontradoError,
    DatosInvalidosError,
    ServicioNoDisponibleError,
)
from logger_config import configurar_logger


class SistemaGestion:
    """Sistema integral de gestión para Software FJ."""

    def __init__(self):
        self.clientes = []
        self.servicios = []
        self.reservas = []
        self.logger = configurar_logger()

    def registrar_evento(self, mensaje):
        """Registra un evento informativo en el log."""
        self.logger.info(mensaje)
        print(f"[EVENTO] {mensaje}")

    def registrar_error(self, mensaje):
        """Registra un error en el log."""
        self.logger.error(mensaje)
        print(f"[ERROR] {mensaje}")

    def agregar_cliente(self, cliente):
        """Agrega un cliente validando duplicados."""
        try:
            for c in self.clientes:
                if c.identificador == cliente.identificador:
                    raise DatosInvalidosError(f"Ya existe un cliente con ID {cliente.identificador}.")
            self.clientes.append(cliente)
            self.registrar_evento(f"Cliente registrado: {cliente.nombre}")
        except Exception as e:
            self.registrar_error(f"Error al registrar cliente: {e}")
            raise

    def agregar_servicio(self, servicio):
        """Agrega un servicio al sistema."""
        try:
            for s in self.servicios:
                if s.codigo == servicio.codigo:
                    raise DatosInvalidosError(f"Ya existe un servicio con código {servicio.codigo}.")
            self.servicios.append(servicio)
            self.registrar_evento(f"Servicio registrado: {servicio.nombre}")
        except Exception as e:
            self.registrar_error(f"Error al registrar servicio: {e}")
            raise

    def buscar_cliente(self, cliente_id):
        """Busca un cliente por ID."""
        for cliente in self.clientes:
            if cliente.identificador == cliente_id:
                return cliente
        raise ClienteNoEncontradoError(f"No se encontró el cliente con ID {cliente_id}.")

    def buscar_servicio(self, codigo_servicio):
        """Busca un servicio por código."""
        for servicio in self.servicios:
            if servicio.codigo == codigo_servicio:
                return servicio
        raise ServicioNoDisponibleError(f"No se encontró el servicio con código {codigo_servicio}.")

    def crear_reserva(self, reserva):
        """Crea y guarda una reserva."""
        try:
            self.reservas.append(reserva)
            self.registrar_evento(f"Reserva creada: {reserva.id_reserva}")
            return reserva
        except Exception as e:
            self.registrar_error(f"Error al crear reserva: {e}")
            raise

    def listar_clientes(self):
        for cliente in self.clientes:
            print(cliente.mostrar_informacion())

    def listar_servicios(self):
        for servicio in self.servicios:
            print(servicio.describir_servicio())

    def listar_reservas(self):
        for reserva in self.reservas:
            print(reserva.mostrar_detalle())
