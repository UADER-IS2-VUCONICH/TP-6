# Descripción
Este programa implementa un sistema de procesamiento de pagos utilizando el patrón de diseño de cadena de responsabilidad. Permite realizar pagos a través de diferentes bancos, verificando el saldo disponible en cada uno de ellos.

# Uso
python programa.py <archivo_json> [opciones]

## Opciones
auto: Selecciona automáticamente un banco para procesar el pago proporcionando el monto del pago.

list: Realiza múltiples pagos y almacena los detalles en el historial de pagos.

# Ejemplo

python programa.py archivo.json auto 100.0

# Clases Principales

SingletonJsonReader: Implementa un patrón Singleton para leer un archivo JSON que contiene información sobre los bancos.

Bank: Representa un banco con su nombre, saldo inicial y token de seguridad.

Payment: Representa un pago realizado, almacenando el número de orden, el nombre del banco, el monto y el token.

PaymentHistory: Mantiene un historial de pagos realizados.

PaymentHandler: Maneja la cadena de responsabilidad para procesar los pagos a través de los bancos disponibles.

BankChain: Construye y maneja la cadena de responsabilidad de bancos.

Program: Representa el programa principal, maneja la interacción con el usuario y ejecuta las acciones correspondientes.

# Flujo del Programa

Inicialización: Lee el archivo JSON que contiene la información de los bancos y construye la cadena de responsabilidad de bancos.

Interacción con el Usuario: Según la opción seleccionada por el usuario, el programa realiza automáticamente un pago a través de un banco seleccionado o realiza múltiples pagos y los almacena en el historial de pagos.

# Versiones

Version 1.2