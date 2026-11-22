# Archivo principal
# Simula al menos 10 operaciones completas del sistema Software FJ.
# Incluye casos válidos e inválidos para demostrar manejo de excepciones.

from cliente import Cliente
from servicio import ReservaSala, AlquilerEquipo, AsesoriaEspecializada
from reserva import Reserva
from sistema import SistemaGestion
from excepciones import SoftwareFJError


def ejecutar_operacion(nombre, funcion, sistema):
    """Ejecuta una operación controlando errores para que el sistema continúe."""
    print(f"\n=== {nombre} ===")
    try:
        resultado = funcion()
        if resultado is not None:
            print(resultado)
        sistema.registrar_evento(f"Operación exitosa: {nombre}")
    except SoftwareFJError as e:
        sistema.registrar_error(f"{nombre}: {e}")
    except Exception as e:
        # Captura cualquier error inesperado
        sistema.registrar_error(f"Error inesperado en {nombre}: {e}")
    else:
        # Se ejecuta si no hubo excepción
        print("Resultado: operación completada sin errores.")
    finally:
        # Siempre se ejecuta
        print("Fin de la operación.")


def main():
    sistema = SistemaGestion()

    print("==============================================")
    print("   SISTEMA INTEGRAL - SOFTWARE FJ")
    print("==============================================")

    # 1. Registrar cliente válido
    ejecutar_operacion(
        "Operación 1 - Registrar cliente válido",
        lambda: sistema.agregar_cliente(Cliente("C001", "Ana Pérez", "ana@correo.com", "3001234567")),
        sistema
    )

    # 2. Registrar cliente inválido (correo malo)
    ejecutar_operacion(
        "Operación 2 - Registrar cliente inválido",
        lambda: sistema.agregar_cliente(Cliente("C002", "Carlos Ruiz", "correo-malo", "3001234567")),
        sistema
    )

    # 3. Registrar servicio válido
    sala = ReservaSala("S001", "Sala de Reuniones", 50000)
    ejecutar_operacion(
        "Operación 3 - Registrar servicio válido",
        lambda: sistema.agregar_servicio(sala),
        sistema
    )

    # 4. Registrar servicio inválido (costo negativo)
    ejecutar_operacion(
        "Operación 4 - Registrar servicio inválido",
        lambda: sistema.agregar_servicio(AlquilerEquipo("S002", "Proyector", -10000)),
        sistema
    )

    # 5. Registrar otros servicios válidos
    equipo = AlquilerEquipo("S003", "Portátil Empresarial", 30000)
    asesoria = AsesoriaEspecializada("S004", "Asesoría en Software", 80000, disponible=True)
    ejecutar_operacion(
        "Operación 5 - Registrar servicios adicionales",
        lambda: [sistema.agregar_servicio(equipo), sistema.agregar_servicio(asesoria)],
        sistema
    )

    # 6. Crear reserva exitosa
    reserva1 = None

    def crear_reserva_exitosa():
        nonlocal reserva1
        cliente = sistema.buscar_cliente("C001")
        servicio = sistema.buscar_servicio("S001")
        reserva1 = Reserva("R001", cliente, servicio, 2)
        sistema.crear_reserva(reserva1)
        return reserva1.mostrar_detalle()

    ejecutar_operacion("Operación 6 - Crear reserva exitosa", crear_reserva_exitosa, sistema)

    # 7. Confirmar y procesar reserva exitosa (sobrecarga: impuesto y descuento)
    def procesar_reserva_exitosa():
        reserva1.confirmar()
        total = reserva1.procesar(impuesto=0.19, descuento=0.10)
        return f"Reserva procesada. Total a pagar: ${total:.2f}"

    ejecutar_operacion("Operación 7 - Procesar reserva exitosa", procesar_reserva_exitosa, sistema)

    # 8. Crear reserva fallida por cliente inexistente
    def reserva_cliente_inexistente():
        cliente = sistema.buscar_cliente("C999")
        servicio = sistema.buscar_servicio("S003")
        reserva = Reserva("R002", cliente, servicio, 1)
        sistema.crear_reserva(reserva)
        return reserva.mostrar_detalle()

    ejecutar_operacion("Operación 8 - Reserva fallida por cliente inexistente", reserva_cliente_inexistente, sistema)

    # 9. Crear reserva fallida por horas inválidas
    def reserva_horas_invalidas():
        cliente = sistema.buscar_cliente("C001")
        servicio = sistema.buscar_servicio("S003")
        reserva = Reserva("R003", cliente, servicio, 0)
        sistema.crear_reserva(reserva)
        return reserva.mostrar_detalle()

    ejecutar_operacion("Operación 9 - Reserva fallida por horas inválidas", reserva_horas_invalidas, sistema)

    # 10. Intentar procesar una reserva no confirmada
    def procesar_sin_confirmar():
        cliente = sistema.buscar_cliente("C001")
        servicio = sistema.buscar_servicio("S004")
        reserva = Reserva("R004", cliente, servicio, 1)
        sistema.crear_reserva(reserva)
        total = reserva.procesar()  # debe fallar porque no está confirmada
        return f"Total: {total}"

    ejecutar_operacion("Operación 10 - Procesar reserva sin confirmar", procesar_sin_confirmar, sistema)

    # 11. Servicio no disponible
    def servicio_no_disponible():
        servicio = AsesoriaEspecializada("S005", "Asesoría VIP", 100000, disponible=False)
        sistema.agregar_servicio(servicio)
        cliente = sistema.buscar_cliente("C001")
        reserva = Reserva("R005", cliente, servicio, 2)
        sistema.crear_reserva(reserva)
        return reserva.mostrar_detalle()

    ejecutar_operacion("Operación 11 - Reserva con servicio no disponible", servicio_no_disponible, sistema)

    print("\n==============================================")
    print("   RESUMEN FINAL DEL SISTEMA")
    print("==============================================")
    print("\nClientes registrados:")
    sistema.listar_clientes()
    print("\nServicios registrados:")
    sistema.listar_servicios()
    print("\nReservas registradas:")
    sistema.listar_reservas()
    print("\nRevise el archivo logs/sistema.log para ver los eventos y errores registrados.")


if __name__ == "__main__":
    main()
