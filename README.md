# Sistema de Gestión de Productos (CLI)

Un sistema de gestión de inventario interactivo por línea de comandos (CLI) desarrollado en Python, diseñado para la administración básica de productos. Este proyecto fue desarrollado como pre-entrega para el programa Talento Tech, demostrando el dominio de estructuras de datos nativas y control de flujo fundamental.

## 🚀 Características Principales

El sistema permite realizar las operaciones fundamentales de gestión de datos en memoria:

1. **Agregar Producto**: Registro de nuevos ítems con validación estricta de entrada (nombre no vacío, categoría no vacía, precio como entero estrictamente positivo).
2. **Mostrar Productos**: Visualización detallada de todo el inventario registrado con formato legible para el usuario.
3. **Buscar Producto**: Búsqueda de alta flexibilidad, insensible a mayúsculas/minúsculas, basada en coincidencia parcial del nombre (substring matching).
4. **Eliminar Producto**: Eliminación segura y precisa basada en el índice posicional (ID) del producto en el inventario.
5. **Interfaz Cíclica**: Menú interactivo que mantiene la ejecución continua hasta que el usuario decida salir explícitamente.

## 🛠️ Stack Tecnológico y Arquitectura

- **Lenguaje**: Python 3.x
- **Estructura de Datos Principal**: Lista de Diccionarios (`List[Dict]`)
- **Interfaz**: Command Line Interface (CLI)
- **Dependencias**: Ninguna (Uso exclusivo de Built-in functions y tipos nativos de Python)

### Enfoque Técnico (Requisitos del Proyecto)
El código fue diseñado para cumplir con especificaciones técnicas particulares que evalúan la lógica algorítmica pura:
- **Flujo Centralizado**: Toda la lógica del negocio y la interfaz de usuario se manejan secuencialmente dentro de un único bucle `while` principal (State Machine básica).
- **Zero-Dependency**: No se requieren módulos externos ni de la biblioteca estándar (como `os` o `sys`), garantizando máxima portabilidad.
- **Validación Manual Predictiva**: Todo el manejo de tipos y sanitización de inputs (ej. `.strip()`, `.lower()`, `.isdigit()`) se realiza preventivamente mediante lógica condicional, asegurando que no ocurran excepciones (TypeErrors/ValueErrors) durante la ejecución normal sin usar bloques `try/except`.

## 💾 Modelo de Datos

Los registros se mantienen en memoria viva dentro de una lista global. Cada producto (entidad) es representado por un diccionario (objeto JSON-like) con el siguiente esquema (Schema):

```json
{
  "nombre": "String (Ej: 'Laptop Dell')",
  "categoria": "String (Ej: 'Electrónica')",
  "precio": "Integer (Ej: 1500)"
}
```

## ⚙️ Cómo Ejecutar

 Para ejecutarlo localmente, solo necesitas tener Python instalado.

1. Clona el repositorio o descarga el archivo `main.py`.
2. Abre una terminal o consola de comandos en el directorio del archivo.
3. Inicia la aplicación ejecutando:

```bash
python main.py
```

## 👤 Contexto del Desarrollo

Desarrollado por **Jenifer Cruz**.
Este repositorio representa la pre-entrega práctica del curso intensivo de programación de **Talento Tech**, evidenciando la aplicación práctica de conceptos de programación estructurada, manipulación de colecciones y experiencia de usuario en consola.
