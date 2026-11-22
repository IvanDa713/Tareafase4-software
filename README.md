# Sistema Integral de Gestión - Software FJ

Proyecto colaborativo de la Fase 4 - Prácticas simuladas (Programación 213023).

## Descripción
Sistema integral orientado a objetos en Python para gestionar clientes, servicios y reservas de la empresa Software FJ. No usa base de datos; utiliza objetos, listas y archivo de logs.

## Requisitos del problema
- Clases abstractas: `Entidad`, `Servicio`.
- Clase `Cliente` con validaciones y encapsulación.
- Servicios especializados: `ReservaSala`, `AlquilerEquipo`, `AsesoriaEspecializada`.
- Clase `Reserva` con confirmar, cancelar y procesar.
- Polimorfismo, métodos sobrescritos y sobrecarga simulada en `calcular_costo`.
- Manejo de excepciones: personalizadas, `try/except`, `try/except/else`, `try/except/finally`, encadenamiento.
- Registro de eventos y errores en `logs/sistema.log`.
- Simulación de al menos 10 operaciones válidas e inválidas.

## Estructura
- `main.py`: ejecución y simulación de operaciones.
- `sistema.py`: gestión central.
- `entidad.py`: clase abstracta base.
- `cliente.py`: cliente con validaciones.
- `servicio.py`: servicios abstracto y especializados.
- `reserva.py`: reserva con estados y procesamiento.
- `excepciones.py`: excepciones personalizadas.
- `logger_config.py`: configuración de logs.

## Ejecución
```bash
python main.py
```

## Evidencia
Al ejecutar `main.py` se muestran operaciones exitosas y fallidas, y se genera/actualiza `logs/sistema.log`.
