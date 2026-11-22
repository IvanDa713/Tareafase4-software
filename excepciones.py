# Excepciones personalizadas del sistema
# Se crean para identificar errores específicos del negocio.


class SoftwareFJError(Exception):
    """Excepción base para todos los errores del sistema Software FJ."""
    pass


class DatosInvalidosError(SoftwareFJError):
    """Se usa cuando un dato ingresado no es válido."""
    pass


class ClienteNoEncontradoError(SoftwareFJError):
    """Se usa cuando se busca un cliente que no existe."""
    pass


class ServicioNoDisponibleError(SoftwareFJError):
    """Se usa cuando un servicio no está disponible o no existe."""
    pass


class ReservaInvalidaError(SoftwareFJError):
    """Se usa cuando una reserva tiene datos incorrectos o no se puede procesar."""
    pass


class OperacionNoPermitidaError(SoftwareFJError):
    """Se usa cuando se intenta hacer una operación no permitida."""
    pass
