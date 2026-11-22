# Clase Cliente
# Representa un cliente de la empresa Software FJ.

from entidad import Entidad
from excepciones import DatosInvalidosError


class Cliente(Entidad):
    """Clase que gestiona la información de un cliente con validaciones."""

    def __init__(self, identificador, nombre, correo, telefono):
        super().__init__(identificador, nombre)
        # Usamos setters para validar los datos
        self.correo = correo
        self.telefono = telefono

    @property
    def correo(self):
        return self._correo

    @correo.setter
    def correo(self, valor):
        # Validación simple de correo
        if not isinstance(valor, str) or "@" not in valor or "." not in valor:
            raise DatosInvalidosError("El correo del cliente no es válido.")
        self._correo = valor.strip()

    @property
    def telefono(self):
        return self._telefono

    @telefono.setter
    def telefono(self, valor):
        # Validación: el teléfono debe tener solo dígitos y mínimo 7 caracteres
        valor = str(valor).strip()
        if not valor.isdigit() or len(valor) < 7:
            raise DatosInvalidosError("El teléfono debe contener solo números y tener al menos 7 dígitos.")
        self._telefono = valor

    def mostrar_informacion(self):
        """Retorna la información del cliente."""
        return f"Cliente ID: {self.identificador} | Nombre: {self.nombre} | Correo: {self.correo} | Tel: {self.telefono}"
