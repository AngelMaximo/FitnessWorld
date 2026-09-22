# Fitness World

Aplicación de escritorio desarrollada en Python con Tkinter para registrar, consultar y eliminar medidas corporales del usuario.

## Descripción

Fitness World permite llevar un control semanal de las medidas del cuerpo, almacenándolas en una base de datos SQLite. La aplicación facilita la gestión de información como:

- Peso
- Cintura
- Bíceps
- Pierna
- Glúteos
- Fecha de registro

El programa ofrece una interfaz gráfica simple con tres opciones principales:

- Introducir medidas
- Consultar medidas
- Eliminar medidas

Este proyecto también tiene como objetivo poner en práctica conceptos
de programación orientada a objetos, manejo de bases de datos, control
de versiones con Git y GitHub y manejo de inteligencia artificial como herramienta de apoyo.

## Funcionalidades

### 1. Insertar medidas
Desde la ventana principal, el usuario puede abrir un formulario para registrar una nueva medición del día actual.

Campos disponibles:
- Fecha: se rellena automáticamente con la fecha actual
- Weight
- Waist
- Biceps
- Leg
- Gluteus

Antes de guardar, se valida que todos los campos estén completos y que los valores sean numéricos.

### 2. Consultar medidas
La sección de consulta permite elegir una fecha registrada y mostrar todas las medidas guardadas para ese día en una tabla.

La tabla muestra:

- Fecha
- Peso
- Cintura
- Bíceps
- Pierna
- Glúteos

### 3. Eliminar medidas
La opción de eliminación permite seleccionar una fecha y borrar todos los registros asociados a esa fecha.

Antes de eliminar, la aplicación solicita confirmación al usuario.

## Tecnologías utilizadas

- Python 3
- Tkinter
- SQLite3
- datetime
- os
- Inteligencia artificial como herramienta de apoyo.
## Estructura principal del proyecto

El archivo principal es:

- `MyProject.py`

Este archivo contiene:

- La interfaz principal
- Las clases para acceder a la base de datos
- Los formularios de inserción, consulta y borrado
- La lógica de validación de datos
- La conexión con SQLite

## Base de datos

La aplicación usa una base de datos SQLite llamada:

- `MedidasSemanales.db`

La conexión se realiza mediante la clase `ConexionDB`, que define la ruta del archivo en la misma carpeta del proyecto.

La tabla utilizada debe tener este formato:

```sql
CREATE TABLE medidas (
    date TEXT,
    weight REAL,
    waist REAL,
    biceps REAL,
    leg REAL,
    gluteus REAL
);
```

## Clases principales

### `ConexionDB`
Se encarga de construir la ruta de la base de datos y crear la conexión SQLite.

### `ventanaPrincipal`
Crea la ventana principal con los tres botones:

- Introduce measures
- Consul measures
- Delete mensures

### `MedidasDB`
Obtiene las fechas disponibles almacenadas en la base de datos para cargar los menús desplegables.

### `Insertar`
Abre una nueva ventana con los campos para introducir las medidas del día.

### `Consultar`
Muestra un selector de fechas y una tabla con los registros correspondientes.

### `Borrar`
Permite seleccionar una fecha y eliminar todos los registros asociados.

## Flujo de uso

1. Ejecutar el programa:
   ```bash
   python MyProject.py
   ```

2. En la pantalla principal, elegir una opción:
   - Insertar medidas
   - Consultar medidas
   - Borrar medidas

3. Registrar los datos y guardar.
4. La aplicación valida los campos y añade la información a la base de datos.
5. Los datos se pueden consultar posteriormente por fecha.

## Requisitos

- Python 3.x instalado
- Tkinter disponible en la instalación de Python
- SQLite3 incluido con Python

## Ejecución

Desde la terminal, sitúate en la carpeta del proyecto y ejecuta:

```bash
python MyProject.py
```

## Observaciones

- La aplicación usa `date.today().isoformat()` para rellenar automáticamente la fecha actual.
- Si los campos están vacíos, la aplicación muestra un aviso.
- Si un valor no es numérico, muestra un error y no guarda el registro.
- Si la base de datos o la tabla no existe, es necesario crearla antes de ejecutar la aplicación.

## Licencia

Este proyecto es un ejemplo educativo para gestionar medidas corporales con Python y SQLite.

## Autor
Angel Maximo
Proyecto desarrollado como ejercicio de programación con interfaz gráfica en Python.